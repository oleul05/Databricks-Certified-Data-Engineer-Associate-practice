"""Build a traceable unique collection from the two downloaded JSON banks."""
import collections
import copy
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "downloads"


def normalize(text):
    text = html.unescape(unicodedata.normalize("NFKC", text)).casefold()
    text = re.sub(r"^\s*(?:question\s*)?\d+\s*[:.\\-]?\s*", "", text)
    text = text.replace("which of the following", "which").replace("start up", "startup")
    return re.sub(r"\W+", " ", text).strip()


# Manually reviewed source item numbers (one-based). Each line represents the
# same question/decision, including abbreviated, renumbered, or reworded copies.
# Similar topics with different conditions stay separate (e.g. FAIL vs DROP,
# table vs database privileges, once vs availableNow vs processingTime).
REVIEWED_GROUPS = """
1 6
2 10 582
3 11 581
4 12 580
5 43 541
7 578
8 577
9 583
13 579
14 90 248 411 576
15 575
16 574
17 573
18 572
19 519 571
21 566
22 515 565
23 564
24 563
25 569
26 568
27 567
28 555
29 562
31 560
33 125 558 601
34 557
36 554
37 553
38 552
39 551
41 549
42 543
44 512 548
45 54 547
46 546
47 545
48 189 544
49 299
50 135 600
51 149 395 610
59 403
60 423 585
52 61 158 283 483
62 481
63 556
64 449
65 99 142 207 322 590
67 447
68 290
69 592
70 599
71 103 365 439
72 192 477
73 421 593
75 162
76 106 178 371 429
78 397
79 594
80 110
82 531
83 175 307 441
84 608
85 596
86 459
87 587
88 586
89 302
91 137
92 473 474
93 157 607
98 271
102 405
104 191 475
108 172 256 435 436
109 163 413
115 343 467
117 184
121 471
123 469
126 550
127 226 443
128 589
130 451
132 455
138 213 328 609
139 419 595
141 604
147 591
148 401
153 605
155 196 399 603
164 294
165 409
166 597
169 433
170 611
174 300
177 305 370 437 438 606
179 263 559
185 457
193 282 598
228 453
235 479
55 588
272 463
274 461
491 516
502 522
524 538
"""

# Next-button downloads are reworded copies of these Real Exam entries.
NEXT_MATCHES = {1: 80, 2: 176, 3: 134, 4: 93, 5: 78, 6: 155,
                7: 70, 8: 153, 9: 84, 10: 77, 11: 51, 12: 148}


def build():
    real = json.loads((ROOT / "real-exam-questions.json").read_text(encoding="utf-8"))
    extra = json.loads((ROOT / "questions.json").read_text(encoding="utf-8"))
    records = real + extra
    parent = list(range(len(records)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def merge(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[max(a, b)] = min(a, b)

    seen = {}
    for i, q in enumerate(records):
        key = normalize(q["stem"])
        assert key, f"Empty question: {i + 1}"
        if key in seen:
            merge(seen[key], i)
        else:
            seen[key] = i
    normalized_count = len({find(i) for i in range(len(real))})
    for line in REVIEWED_GROUPS.strip().splitlines():
        ids = [int(s) - 1 for s in line.split()]
        for i in ids[1:]:
            merge(ids[0], i)
    for extra_item, real_item in NEXT_MATCHES.items():
        merge(len(real) + extra_item - 1, real_item - 1)

    groups = collections.defaultdict(list)
    for i in range(len(records)):
        groups[find(i)].append(i)

    result, mapping = [], []
    for number, indices in enumerate(groups.values(), 1):
        # Prefer a full stem with actual option text, a marked answer, and an
        # explanation. Source content is never rewritten or silently corrected.
        def quality(i):
            q = records[i]
            missing = sum(not o.get("text", "").strip() or "no code block shown" in o.get("text", "").lower() for o in q["options"])
            correct = any(o.get("correct") and o.get("text", "").strip() for o in q["options"])
            return (-missing, correct, bool(q.get("explanation")), "\ufffd" not in q["stem"], -i)
        selected = max(indices, key=quality)
        entry = copy.deepcopy(records[selected])
        entry["id"] = f"lqd-{number:03d}"
        entry["sourceCount"] = len(indices)
        entry["sources"] = []
        entry["variants"] = []
        variants = {}
        for i in indices:
            q = records[i]
            source = {"file": "real-exam-questions.json" if i < len(real) else "questions.json",
                      "item": i + 1 if i < len(real) else i - len(real) + 1,
                      "url": q["url"], "page": q.get("page")}
            entry["sources"].append(source)
            key = json.dumps({k: v for k, v in q.items() if k not in ("url", "page", "next")}, ensure_ascii=False, sort_keys=True)
            if key not in variants:
                variants[key] = copy.deepcopy(q)
                variants[key]["sourceItems"] = []
                entry["variants"].append(variants[key])
            variants[key]["sourceItems"].append(source)
            mapping.append({**source, "uniqueId": entry["id"]})
        entry["answerVariants"] = sorted({" | ".join(normalize(o.get("text", "")) for o in v["options"] if o.get("correct")) for v in entry["variants"]} - {""})
        entry["sourceAnswerVaries"] = len(entry["answerVariants"]) > 1
        result.append(entry)

    assert sum(q["sourceCount"] for q in result) == len(records)
    assert len(mapping) == len(records)
    assert len({(m["file"], m["item"]) for m in mapping}) == len(records)
    assert len({normalize(q["stem"]) for q in result}) == len(result)
    dump = lambda p, data: p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    dump(ROOT / "unique-questions.json", result)
    audit = {"inputFiles": {"real-exam-questions.json": len(real), "questions.json": len(extra)},
             "sourceItems": len(records), "realExamNormalizedUniqueStems": normalized_count,
             "uniqueQuestions": len(result), "duplicateCopiesGrouped": len(records) - len(result),
             "method": "Normalized stems, then manually reviewed reworded copies. Different conditions and operations retained. All source variants preserved; source answers are not fact-checked.",
             "inputSha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in ("real-exam-questions.json", "questions.json")},
             "groupsWithDifferentAnswerText": [q["id"] for q in result if q["sourceAnswerVaries"]],
             "sourceMapping": sorted(mapping, key=lambda m: (m["file"], m["item"]))}
    dump(ROOT / "unique-questions-audit.json", audit)
    render(result, audit)
    print(json.dumps({k: v for k, v in audit.items() if k not in ("sourceMapping", "inputSha256", "groupsWithDifferentAnswerText")}, indent=2))


def answer(q):
    return ", ".join(o["key"] for o in q["options"] if o.get("correct")) or "Not marked in source"


def render(result, audit):
    esc = html.escape
    intro = f"{len(result)} unique questions from {audit['sourceItems']} downloaded entries ({audit['duplicateCopiesGrouped']} duplicate copies grouped). Reworded copies are grouped; all source versions remain in the JSON collection and original downloads. Source answers and explanations are preserved without fact-checking or syllabus filtering."
    md = ["# LeetQuiz — unique downloaded questions", "", intro, ""]
    articles = []
    for n, q in enumerate(result, 1):
        md.extend([f"## {n}. {q['id']}", "", q["stem"], ""])
        for o in q["options"]:
            md.extend([f"{o['key']}. {o.get('text', '')}", ""])
        md.extend([f"**Source answer: {answer(q)}**", "", q.get("explanation", ""), "",
                   f"Source copies: {q['sourceCount']}; distinct source versions: {len(q['variants'])}.", ""])
        if q["sourceAnswerVaries"]:
            md.extend(["Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.", ""])
        md.extend([f"Source: {q['url']}", ""])
        options = "".join(f'<li class="{"correct" if o.get("correct") else ""}"><b>{esc(o["key"])}.</b><pre>{esc(o.get("text", ""))}</pre></li>' for o in q["options"])
        versions = []
        for v in q["variants"]:
            opts = "".join(f'<li><b>{esc(o["key"])}.</b><pre>{esc(o.get("text", ""))}</pre></li>' for o in v["options"])
            versions.append(f'<section><pre>{esc(v["stem"])}</pre><ul>{opts}</ul><p>Source answer: {esc(answer(v))}</p><pre>{esc(v.get("explanation", ""))}</pre></section>')
        links = "".join(f'<li><a href="{esc(s["url"], quote=True)}">{esc(s["file"])} item {s["item"]}</a></li>' for s in q["sources"])
        note = '<p class="note">Source versions mark different answer text; inspect the versions below.</p>' if q["sourceAnswerVaries"] else ""
        articles.append(f'<article id="{q["id"]}"><h2>{n}. {q["id"]}</h2><pre>{esc(q["stem"])}</pre><ul>{options}</ul><p><b>Source answer: {esc(answer(q))}</b></p>{note}<details><summary>Source explanation</summary><pre>{esc(q.get("explanation", ""))}</pre></details><details><summary>{q["sourceCount"]} source copies · {len(q["variants"])} versions</summary><ul>{links}</ul>{"".join(versions)}</details></article>')
    (ROOT / "unique-questions.md").write_text("\n".join(md), encoding="utf-8")
    page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>LeetQuiz — unique downloaded questions</title><style>body{font:16px/1.6 system-ui;max-width:960px;margin:32px auto;padding:16px;background:#f5f7fa;color:#172033}article{background:white;border:1px solid #ddd;border-radius:12px;padding:24px;margin:24px 0}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit}ul{list-style:none;padding:0}li{padding:8px}.correct{background:#dcfce7}.note{background:#fff3cd;padding:10px}a{color:#2563eb}input{font:inherit;padding:12px;width:100%;box-sizing:border-box}section{border-top:1px solid #ddd;margin-top:16px}summary{cursor:pointer;padding:8px 0}[hidden]{display:none}</style></head><body>'
    page += f'<h1>LeetQuiz — {len(result)} unique questions</h1><p>{esc(intro)}</p><label for="search">Search questions and answers</label><input id="search" type="search" placeholder="Search this collection"><p id="count">{len(result)} questions</p>' + "\n".join(articles)
    page += '<script>const articles=[...document.querySelectorAll("article")];const texts=articles.map(a=>a.textContent.toLowerCase());document.getElementById("search").addEventListener("input",e=>{const term=e.target.value.toLowerCase().trim();let count=0;articles.forEach((a,i)=>{a.hidden=!texts[i].includes(term);if(!a.hidden)count++;});document.getElementById("count").textContent=count+" questions";});</script></body></html>'
    (ROOT / "unique-questions.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    build()
