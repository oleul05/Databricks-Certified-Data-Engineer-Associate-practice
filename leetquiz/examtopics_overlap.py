"""Reviewed matches between LeetQuiz questions and the syllabus ExamTopics bank.

Matches include exact copies, reworded copies, and corrected modernizations of
the same source question. Sharing a topic or correct answer alone is insufficient.
Each removed entry has a surviving ExamTopics question and an audit snapshot.
"""

import hashlib
import html
import json
import re
from pathlib import Path

ORIGINAL_MATCHES = {
    'lq-quality': 'et-9', 'lq-gold': 'et-119', 'lq-delta': 'et-4',
    'lq-concurrency': 'et-130', 'lq-usage': 'et-45', 'lq-delete': 'et-6',
    'lq-expectFail': 'et-80', 'lq-autostop': 'et-40', 'lq-truth': 'et-29',
    'lq-externalDrop': 'et-23', 'lq-gitBranches': 'et-94',
    'lq-tempCreate': 'et-10', 'lq-pull': 'et-46', 'lq-qualityTool': 'et-25',
    'lq-mergeAvoid': 'et-20', 'lq-web': 'et-3', 'lq-owner': 'et-22',
    'lq-tableCreate': 'et-24', 'lq-autoWorkloads': 'et-7', 'lq-storage': 'et-5',
    'lq-salesPy': 'et-12', 'lq-grantSelect': 'et-197', 'lq-except': 'et-258',
    'lq-createEmpty': 'et-99', 'lq-streamRead': 'et-34', 'lq-optimize': 'et-51',
    'lq-pool': 'et-92', 'lq-bronze': 'et-50', 'lq-streamingVsMV': 'et-33',
    'lq-autoStrings': 'et-71', 'lq-goldSource': 'et-73', 'lq-csv': 'et-108',
    'lq-checkpoint': 'et-118', 'lq-copyIdempotent': 'et-19',
    'lq-vacuumTimeTravel': 'et-52',
}

DOWNLOAD_PAIRS = """
3 77
5 197
10 99
17 278
27 78
29 17
40 41
45 23
46 9
47 83
49 13
50 82
51 54
53 47
54 12
55 45
56 50
57 118
59 44
60 36
61 46
63 4
65 40
66 16
68 49
69 108
70 52
71 92
72 27
73 65
74 73
75 80
77 6
78 25
79 71
80 30
81 10
82 58
83 39
84 130
85 29
86 42
87 78
88 96
90 111
91 100
93 43
94 34
95 129
96 37
97 32
98 31
99 7
100 119
102 24
103 21
104 19
105 2
107 11
108 94
109 35
110 5
111 3
112 51
113 98
114 15
116 8
117 107
118 20
120 67
121 76
123 22
124 33
127 28
128 79
129 81
170 186
174 197
178 263
180 189
182 183
183 232
187 267
190 82
197 28
"""
DOWNLOAD_MATCHES = {f'lqd-{int(a):03d}': f'et-{int(b)}' for a, b in
                    (line.split() for line in DOWNLOAD_PAIRS.strip().splitlines())}

# Additional evidence for less literal matches. Historical source variants are
# retained in the raw JSON, so corrected answers need not equal a legacy answer.
MATCH_NOTES = {
    'lq-usage': 'Modernized version of the same source metadata-discovery grant question; the retained LeetQuiz version uses BROWSE while ExamTopics still shows the legacy USAGE formulation.',
    'lqd-055': 'Same source metadata-discovery grant question, corrected to Unity Catalog BROWSE in LeetQuiz.',
    'lq-externalDrop': 'Same external-table DROP behavior: registration is removed while external files remain, asked as effect versus explanation.',
    'lq-web': 'Same association between the Databricks web application and the control plane, with the question direction reversed.',
    'lq-grantSelect': 'Same read-only SELECT grant, with different table and principal names.',
    'lqd-005': 'Same read-only SELECT grant; LeetQuiz makes parent privileges and table qualification explicit.',
    'lq-except': 'Same customers-with-no-orders exclusion result; SQL EXCEPT and left anti join are equivalent here for customer IDs.',
    'lqd-003': 'Same choice of job compute for scheduled production workloads rather than interactive all-purpose compute.',
    'lqd-017': 'Same requirement to retain only records whose key occurs in both tables, using an inner join.',
    'lqd-027': 'Same batch-to-streaming read API change, with a different source format.',
    'lqd-109': 'Corrected modernization of the same source Git merge question; the obsolete outside-the-workspace restriction was removed in LeetQuiz.',
    'lqd-170': 'Same shuffle-partition tuning to address disk spilling in a slow Spark workload.',
    'lqd-174': 'Same SELECT privilege for read access without granting modification rights.',
    'lqd-178': 'Same native managed Lakeflow Connect ingestion from Salesforce.',
    'lqd-180': 'Same definition of a bundle as YAML configuration containing project resources and settings.',
    'lqd-182': 'Same Silver-layer purpose: clean and validate ingested data.',
    'lqd-183': 'Same choice of file-notification discovery for a large file population and ongoing ingestion.',
    'lqd-187': 'Same large-fact/small-lookup join scenario requiring a broadcast join to avoid a large shuffle.',
    'lqd-190': 'Same fast-startup benefit of serverless SQL, asked as its benefit versus remedy for cold-start delays.',
    'lqd-197': 'Same SQL-query execution into a PySpark DataFrame using spark.sql.',
}


def audit_and_filter(original, downloaded, home):
    root = Path(__file__).resolve().parent.parent
    pages = json.loads(re.search(r'^const PAGES = (.*);$', home, re.M).group(1))
    examtopics = {}
    for page in pages:
        if page.get('group') == 'et' and not page.get('oos'):
            text = (root / page['file']).read_text(encoding='utf-8')
            questions = json.loads(re.search(r'^const QUESTIONS = (.*);$', text, re.M).group(1))
            for index, question in enumerate(questions):
                assert question['uid'] not in examtopics
                examtopics[question['uid']] = {**question, 'file': page['file'], 'index': index}
    originals = {q['uid']: q for q in original}
    downloads = {q['id']: q for q in downloaded}
    assert ORIGINAL_MATCHES.keys() <= originals.keys()
    assert DOWNLOAD_MATCHES.keys() <= downloads.keys()
    assert set(ORIGINAL_MATCHES.values()) | set(DOWNLOAD_MATCHES.values()) <= examtopics.keys()
    plain = lambda text: html.unescape(re.sub('<[^>]+>', ' ', text)).strip()
    rows = []
    for matches, source, group in [(ORIGINAL_MATCHES, originals, 'original'), (DOWNLOAD_MATCHES, downloads, 'downloaded')]:
        for uid, target in matches.items():
            q, other = source[uid], examtopics[target]
            rows.append({'removedUid': uid, 'bank': group, 'removedStem': plain(q['stem']),
                         'retainedUid': target, 'retainedStem': plain(other['stem']),
                         'retainedFile': other['file'], 'retainedIndex': other['index'],
                         'reason': MATCH_NOTES.get(uid, 'Same source question or reworded question testing the same requirement and decision; source identifiers, product names, and disclosed corrections can differ.')})
    kept_original = [q for q in original if q['uid'] not in ORIGINAL_MATCHES]
    kept_downloaded = [q for q in downloaded if q['id'] not in DOWNLOAD_MATCHES]
    audit = {'examtopicsCompared': len(examtopics), 'leetquizCompared': len(original) + len(downloaded),
             'originalRemoved': len(ORIGINAL_MATCHES), 'downloadedRemoved': len(DOWNLOAD_MATCHES),
             'duplicatesRemoved': len(rows), 'originalRemaining': len(kept_original),
             'downloadedRemaining': len(kept_downloaded),
             'policy': 'Reviewed question-level matches, including exact copies, paraphrases, and modernizations of the same source question. Same-topic questions with different conditions, operations, or required details are retained. ExamTopics is the retained bank; its source answers are not changed by this operation.',
             'examtopicsFileSha256': {p['file']: hashlib.sha256((root / p['file']).read_bytes()).hexdigest()
                                     for p in pages if p.get('group') == 'et' and not p.get('oos')},
             'removedQuestions': rows,
             'remainingOriginalIds': [q['uid'] for q in kept_original],
             'remainingDownloadedIds': [q['id'] for q in kept_downloaded]}
    output = root / 'leetquiz'
    (output / 'examtopics-deduplication-audit.json').write_text(json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    md = ['# LeetQuiz overlap with syllabus ExamTopics', '', audit['policy'], '',
          f"Compared {audit['leetquizCompared']} LeetQuiz entries with {audit['examtopicsCompared']} ExamTopics questions. Removed {audit['duplicatesRemoved']} overlapping LeetQuiz entries ({audit['originalRemoved']} original-bank and {audit['downloadedRemoved']} downloaded-bank entries).", '',
          f"Remaining: {audit['originalRemaining']} original-bank questions and {audit['downloadedRemaining']} downloaded questions. Archived source JSON and PDFs are preserved.", '',
          'The count is removed LeetQuiz entries. Multiple LeetQuiz entries may match the same retained ExamTopics question.', '',
          '## Removed questions and retained counterparts', '', '| Removed LeetQuiz ID | Retained ExamTopics question | Reason |', '| --- | --- | --- |']
    for row in rows:
        md.append('| ' + row['removedUid'] + ' | [' + row['retainedUid'] + '](../' + row['retainedFile'] + ') | ' + row['reason'] + ' |')
    md.extend(['', '## Differences deliberately retained', '',
               '- Single micro-batch (`once`) versus all available input in multiple batches (`availableNow`) versus repeated five-second processing.',
               '- Temporary/session views versus persistent views, and choosing a join type versus evaluating an existing join result.',
               '- Default expectation behavior versus dropping invalid rows versus failing an update.',
               '- Bundle configuration file identification versus the target/variable override structure.',
               '- Reading nested fields, parsing JSON into STRUCT, and extracting scalar JSON fields.',
               '- Table storage configuration, schema evolution, ownership privileges, and metadata discovery at different securable levels when the requirements differ.', ''])
    (output / 'examtopics-deduplication-audit.md').write_text('\n'.join(md), encoding='utf-8')
    (output / 'examtopics-unique-questions.json').write_text(json.dumps(kept_original, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (output / 'downloads/examtopics-unique-questions.json').write_text(json.dumps(kept_downloaded, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return kept_original, kept_downloaded, audit
