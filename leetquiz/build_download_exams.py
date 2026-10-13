"""Publish the unique download bank as three existing-style practice exams."""
import html
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def text_block(text):
    return '<div style="white-space: pre-wrap">' + html.escape(text) + '</div>'


def read_constant(page, name):
    return json.loads(re.search(r'^const ' + name + r' = (.*);$', page, re.M).group(1))


def replace_constant(page, name, value):
    line = 'const ' + name + ' = ' + json.dumps(value, ensure_ascii=False) + ';'
    page, count = re.subn(r'^const ' + name + r' = .*;$', lambda _: line, page, count=1, flags=re.M)
    assert count == 1
    return page


def build():
    from refine_downloads import build as refine, GUIDE, SECTIONS
    from examtopics_overlap import audit_and_filter
    refine()
    bank = json.loads((ROOT / 'leetquiz/downloads/syllabus-questions.json').read_text(encoding='utf-8'))
    assert bank and len({q['id'] for q in bank}) == len(bank)
    template = (ROOT / 'questions/leetquiz/leetquiz.html').read_text(encoding='utf-8')
    home_path = ROOT / 'Databricks_Home.html'
    home = home_path.read_text(encoding='utf-8')
    originals = json.loads((ROOT / 'leetquiz/refined-questions.json').read_text(encoding='utf-8'))
    originals, bank, overlap = audit_and_filter(originals, bank, home)
    # Rebuild the original active page from its preserved source bank. Keeping
    # the source JSON intact makes removal traceable and the build repeatable.
    original_page = replace_constant(template, 'QUESTIONS', originals)
    for index, question in enumerate(originals):
        question['sourceN'] = question['n']
        question['n'] = index + 1
        question['label'] = question['label'].replace('LeetQuiz #', 'LeetQuiz source #')
    original_page = replace_constant(original_page, 'QUESTIONS', originals)
    original_subtitle = f'May 2026 syllabus · {len(originals)} questions · ExamTopics duplicates removed · updated names in yellow'
    original_page = re.sub(r'<div class="brand">LeetQuiz<small class="bn">.*?</small></div>',
                           lambda _: '<div class="brand">LeetQuiz<small class="bn">' + original_subtitle + '</small></div>', original_page, count=1)
    original_signature = hashlib.sha256(json.dumps([[q['uid'], q['answer']] for q in originals]).encode()).hexdigest()[:12]
    original_page = re.sub(r'^const TIMER_KEY = .*;$',
                          lambda _: 'const TIMER_KEY = "dbx-set-timer-v1:" + PAGE_ID + ":' + original_signature + '";', original_page, count=1, flags=re.M)
    (ROOT / 'questions/leetquiz/leetquiz.html').write_text(original_page, encoding='utf-8')
    pages = [p for p in read_constant(home, 'PAGES') if not p['id'].startswith('leetquiz-download-exam-')]
    reviews = [q for q in read_constant(home, 'REVIEW_QUESTIONS') if not q['uid'].startswith(('lq-', 'lqd-'))]
    original_metadata = next(p for p in pages if p['id'] == 'leetquiz')
    original_legacy = {q[0]: q for q in original_metadata['qs']}
    original_metadata['subtitle'] = original_subtitle
    original_metadata['qs'] = [original_legacy[q['uid']] for q in originals]
    reviews.extend({**q, 'setTitle': 'LeetQuiz', 'file': 'questions/leetquiz/leetquiz.html', 'index': i} for i, q in enumerate(originals))
    new_pages, new_reviews = [], []
    manifest = []
    for set_index in range(3):
        page_id = f'leetquiz-download-exam-{set_index + 1}'
        title = f'LeetQuiz Download Exam {set_index + 1}'
        file = f'questions/leetquiz/LeetQuiz_Download_Exam_{set_index + 1}.html'
        # Round-robin allocation mixes the source collection across the exams.
        source_questions = bank[set_index::3]
        questions = []
        for index, source in enumerate(source_questions):
            options = [{'k': o['key'], 'html': o['displayHtml']} for o in source['options']]
            answer = [o['key'] for o in source['options'] if o.get('correct')]
            assert answer and all(a in {o['k'] for o in options} for a in answer)
            collection_link = '../../leetquiz/downloads/unique-questions.html#' + source['id']
            explanation = '<p class="ans">Answer: ' + ', '.join(answer) + '</p>'
            if source['corrections']:
                explanation += '<h3>Source correction</h3><ul>' + ''.join('<li>' + html.escape(note) + '</li>' for note in source['corrections']) + '</ul>'
            explanation += '<h3>Explanation</h3>' + source['displayExplanation']
            if source['sourceAnswerVaries']:
                explanation += '<p class="syllabus-note">Downloaded source versions mark different answer text. Original versions are preserved in the unique collection; disclosed corrections above take precedence.</p>'
            explanation += '<p>May 2026 guide: ' + html.escape(source['guideObjective']) + '</p>'
            for documentation in source['documentation']:
                explanation += '<p><a href="' + html.escape(documentation, quote=True) + '" target="_blank" rel="noopener noreferrer">Databricks documentation</a></p>'
            explanation += '<p><a href="' + html.escape(source['url'], quote=True) + '" target="_blank" rel="noopener noreferrer">Original question</a> · <a href="' + collection_link + '" target="_blank" rel="noopener noreferrer">All source versions</a></p>'
            question = {'uid': source['id'], 'n': index + 1, 'label': title + ' · ' + source['id'] + ' · ' + SECTIONS[source['sec']],
                        'stem': source['displayStem'], 'options': options, 'sec': source['sec'],
                        'answer': answer, 'explain': explanation, 'oos': False}
            questions.append(question)
            new_reviews.append({**question, 'setTitle': title, 'file': file, 'index': index})
        duration = len(questions) * 70
        subtitle = f'May 2026 syllabus · {len(questions)} questions · {duration // 60}m {duration % 60:02d}s · updated terms in yellow'
        page = replace_constant(template, 'QUESTIONS', questions)
        page = page.replace('<title>LeetQuiz</title>', '<title>' + title + '</title>')
        page = re.sub(r'<div class="brand">LeetQuiz<small class="bn">.*?</small></div>',
                      lambda _: '<div class="brand">' + title + '<small>' + subtitle + '</small><small>Source corrections are disclosed in explanations.</small></div>', page, count=1)
        page = page.replace('const PAGE_ID = "leetquiz";', 'const PAGE_ID = "' + page_id + '";')
        signature = hashlib.sha256(json.dumps([[q['uid'], q['answer']] for q in questions]).encode()).hexdigest()[:12]
        page = re.sub(r'^const TIMER_KEY = .*;$',
                      lambda _: 'const TIMER_KEY = "dbx-set-timer-v1:" + PAGE_ID + ":' + signature + '";', page, count=1, flags=re.M)
        (ROOT / file).write_text(page, encoding='utf-8')
        new_pages.append({'id': page_id, 'file': file, 'title': title, 'subtitle': subtitle,
                          'oos': False, 'group': 'leetquiz',
                          'qs': [[q['uid'], ''.join(sorted(q['answer'])), 'dbx-' + page_id + '-v1', i] for i, q in enumerate(questions)]})
        manifest.append({'id': page_id, 'file': file, 'count': len(questions), 'timerSeconds': duration, 'guide': GUIDE,
                         'questionIds': [q['uid'] for q in questions]})
    position = next(i for i, p in enumerate(pages) if p['id'] == 'leetquiz') + 1
    pages[position:position] = new_pages
    home = replace_constant(home, 'PAGES', pages)
    home = replace_constant(home, 'REVIEW_QUESTIONS', reviews + new_reviews)
    home_path.write_text(home, encoding='utf-8')
    assert len(new_reviews) == len(bank) and len({q['uid'] for q in new_reviews}) == len(bank)
    (ROOT / 'leetquiz/downloads/exam-sets-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{k: v for k, v in p.items() if k != 'questionIds'} for p in manifest], indent=2))
    print(f"Removed {overlap['duplicatesRemoved']} ExamTopics duplicates; {len(originals)} original and {len(bank)} downloaded questions remain.")


if __name__ == '__main__':
    build()
