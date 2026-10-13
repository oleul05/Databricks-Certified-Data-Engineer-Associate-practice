from pathlib import Path
import json,re,html,shutil,collections
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether,PageBreak
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
root=Path(__file__).resolve().parents[2]
qs=json.loads((root/'leetquiz/refined-questions.json').read_text())
audit=json.loads((root/'leetquiz/refinement-audit.json').read_text())
# Reuse the established ExamTopics quiz engine and its Bangla explanations/review/timer behavior.
template=(root/'questions/examtopics/Databricks_ExamTopics_Extra_Practice.html').read_text()
page=re.sub(r'const QUESTIONS = .*?;\n',lambda m:'const QUESTIONS = '+json.dumps(qs,ensure_ascii=False)+';\n',template,count=1)
page=page.replace('const PAGE_ID = "etx";','const PAGE_ID = "leetquiz";').replace('ExamTopics Extra Practice','LeetQuiz')
page=re.sub(r'(<div class="brand">LeetQuiz<small class="bn">).*?(</small>)',r'\g<1>May 2026 syllabus · ৭৬টি unique প্রশ্ন · updated নাম হলুদ রঙে\2',page,count=1)
page=page.replace('--rn-bg: #6b5500; --rn-ink: #ffe680;','--rn-bg: #ffe866; --rn-ink: #3b2f00;')
count=len(qs)
bn_count=str(count).translate(str.maketrans('0123456789','০১২৩৪৫৬৭৮৯'))
page=page.replace('৭৬টি unique প্রশ্ন',bn_count+'টি unique প্রশ্ন')
# Source provenance shown in the existing question label.
for q in qs:
 if q.get('origin_pdf') and 'original page' not in q['label']:
  q['label']+=f' · PDF {q["origin_pdf"]}, original page {q["sourcePage"]}'
page=re.sub(r'const QUESTIONS = .*?;\n',lambda m:'const QUESTIONS = '+json.dumps(qs,ensure_ascii=False)+';\n',page,count=1)
page=page.replace('<div class="wrap">','<div style="max-width:1180px;margin:16px auto 0;padding:0 16px;font-size:14px">76 unique syllabus questions from 158 source pages. <span class="rn-new">Yellow = updated name</span>. <a href="../../leetquiz/refinement-audit.md">Refinement audit</a> · <a href="../../leetquiz/refined-questions.json">Question data</a>. This is a practice bank, not a claim of complete syllabus coverage.</div>\n<div class="wrap">',1)
page=page.replace('76 unique syllabus questions from 158 source pages.',f'{count} unique syllabus questions from the four PDFs and accessible downloads.')
(root/'questions/leetquiz/leetquiz.html').write_text(page)
# Home integration includes progress, review lists, and the new group.
home=(root/'Databricks_Home.html').read_text()
pages=json.loads(re.search(r'const PAGES = (.*?);\n',home)[1])
pages=[p for p in pages if p['id']!='leetquiz']
pages.append({'id':'leetquiz','file':'questions/leetquiz/leetquiz.html','title':'LeetQuiz','subtitle':bn_count+'টি unique প্রশ্ন · May 2026 syllabus · updated নাম হলুদ','oos':False,'group':'leetquiz','qs':[[q['uid'],''.join(q['answer']),None,q['n']-1] for q in qs]})
home=re.sub(r'const PAGES = .*?;\n',lambda m:'const PAGES = '+json.dumps(pages,ensure_ascii=False)+';\n',home,count=1)
review=json.loads(re.search(r'const REVIEW_QUESTIONS = (.*?);\n',home)[1]);review=[q for q in review if not q['uid'].startswith('lq-')]
review.extend({**q,'setTitle':'LeetQuiz','file':'questions/leetquiz/leetquiz.html','index':i} for i,q in enumerate(qs))
home=re.sub(r'const REVIEW_QUESTIONS = .*?;\n',lambda m:'const REVIEW_QUESTIONS = '+json.dumps(review,ensure_ascii=False)+';\n',home,count=1)
if 'id="leetquizGrid"' not in home:
 home=home.replace('  <h2 class="sec">Syllabus-এর প্রশ্ন · Udemy</h2>','  <h2 class="sec">Syllabus-এর প্রশ্ন · LeetQuiz</h2>\n  <p class="note">চারটি PDF থেকে duplicate ও syllabus-এর বাইরের প্রশ্ন বাদ দেওয়া। Updated নাম হলুদ রঙে; সংশোধনের তথ্য explanation-এ। <a href="leetquiz/refinement-audit.md">Audit</a> · <a href="leetquiz/leetquiz-1.pdf">PDF 1</a> · <a href="leetquiz/leetquiz-2.pdf">PDF 2</a> · <a href="leetquiz/leetquiz-3.pdf">PDF 3</a> · <a href="leetquiz/leetquiz-4.pdf">PDF 4</a></p>\n  <div class="grid" id="leetquizGrid"></div>\n\n  <h2 class="sec">Syllabus-এর প্রশ্ন · Udemy</h2>')
 home=home.replace('grids = { et:', 'grids = { leetquiz: $("leetquizGrid"), et:')
(root/'Databricks_Home.html').write_text(home)
(root/'leetquiz/refined-questions.json').write_text(json.dumps(qs,ensure_ascii=False,indent=2))
# Question-only text PDFs, unique across the set, with renamed terms highlighted.
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='StemQ',fontName='Helvetica',fontSize=10.5,leading=15,spaceAfter=9))
styles.add(ParagraphStyle(name='ChoiceQ',fontName='Helvetica',fontSize=9.5,leading=13,spaceAfter=6,leftIndent=14))
styles.add(ParagraphStyle(name='NoteQ',fontName='Helvetica',fontSize=8,leading=11,textColor=colors.HexColor('#526173'),spaceAfter=8))
def pdfhtml(s):
 s=re.sub(r'<span class="rn-new"[^>]*>(.*?)</span>',r'<font backColor="#ffe866" color="#3b2f00">\1</font>',s,flags=re.S)
 s=re.sub(r'<pre><code>(.*?)</code></pre>',lambda m:'<font face="Courier" size="8">'+m[1].replace('\n','<br/>')+'</font>',s,flags=re.S)
 s=re.sub(r'</?p[^>]*>','',s)
 return s.replace('’',"'").replace('‘',"'").replace('–','-').replace('—','-')
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#667085'))
 c.drawString(42,24,'LeetQuiz - May 2026 syllabus | Yellow: updated item name')
 c.drawRightString(A4[0]-42,24,str(d.page))
counts={}
for n in range(1,5):
 out=root/f'leetquiz/leetquiz-{n}.pdf';backup=root/f'leetquiz/originals/leetquiz-{n}.pdf'
 if not backup.exists():shutil.copy2(out,backup)
 selected=[q for q in qs if q['origin_pdf']==n];counts[n]=len(selected)
 story=[Paragraph(f'LeetQuiz {n} - Refined Questions',styles['Title']),Paragraph(f'{len(selected)} unique questions. Duplicates removed across all four PDFs. Based on the May 2026 exam guide.',styles['NoteQ']),Paragraph('Updated product and SQL object names have a yellow background. Substantive corrections are disclosed below each affected question. Original page references refer to archived screenshot PDFs.',styles['NoteQ']),Spacer(1,12)]
 for q in selected:
  block=[Paragraph(f'Question {q["n"]} - {q["label"].split(" · ")[1]}',styles['Heading2']),Paragraph(f'Original: leetquiz-{n}.pdf, page {q["sourcePage"]}',styles['NoteQ']),Paragraph(pdfhtml(q['stem']),styles['StemQ'])]
  if len(q['answer'])>1:block.append(Paragraph(f'Choose {len(q["answer"])} answers.',styles['NoteQ']))
  block.extend(Paragraph(o['k']+'. '+pdfhtml(o['html']),styles['ChoiceQ']) for o in q['options'])
  if q['correction']:block.append(Paragraph('Source correction: '+html.escape(q['correction']),styles['NoteQ']))
  block.append(Spacer(1,16));story.append(KeepTogether(block))
 SimpleDocTemplate(str(out),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=42,title=f'LeetQuiz {n} - Refined Questions').build(story,onFirstPage=footer,onLaterPages=footer)
# Human-readable audit with every source page accounted for.
lines=['# LeetQuiz refinement audit','',f'Compared against the [May 2026 exam guide]({audit["guide"]}).','',f'158 source pages → 98 unique question variants → 76 retained, 22 excluded unique questions. 60 duplicate copies removed.','',audit['note'],'','Original screenshot PDFs are preserved in `originals/`. Refined PDF allocation: '+', '.join(f'PDF {n}: {counts[n]}' for n in counts)+'.','','## Name updates','','| Old name | Current name (yellow in quizzes and PDFs) |','| --- | --- |','| Delta Live Tables / DLT | Lakeflow Spark Declarative Pipelines |','| Databricks Repos | Databricks Git Folders |','| Databricks Asset Bundles | Declarative Automation Bundles |','| Databricks Lakehouse Platform | Databricks Data Intelligence Platform |','| SQL endpoint | SQL warehouse |','| Data Explorer | Catalog Explorer |','| CREATE STREAMING LIVE TABLE / CREATE INCREMENTAL LIVE TABLE | CREATE OR REFRESH STREAMING TABLE |','| CREATE LIVE TABLE | CREATE OR REFRESH MATERIALIZED VIEW |','','SQL/object migrations sometimes require behavior or code changes, not just renaming. Those are separately identified as Source correction.','','## Excluded unique questions','','| First source | Concept | Reason |','| --- | --- | --- |']
for a in audit['pages']:
 if a['status']=='excluded':lines.append(f'| PDF {a["pdf"]}, page {a["page"]} | {a["key"]} | {a["reason"]} |')
lines+=['','## Retained questions and corrections','','| Question | Source pages | Section | Correction |','| --- | --- | --- | --- |']
for q in qs:lines.append(f'| {q["n"]}: {q["key"]} | '+', '.join(f'{s["pdf"]}:{s["page"]}' for s in q['sources'])+f' | {q["sec"]} | {q["correction"] or "Wording consolidated; concept retained."} |')
lines+=['','## Every original page','','| PDF | Page | Concept | Disposition |','| --- | --- | --- | --- |']
for a in audit['pages']:lines.append(f'| {a["pdf"]} | {a["page"]} | {a["key"]} | {a["status"]} |')
(root/'leetquiz/refinement-audit.md').write_text('\n'.join(lines)+'\n')
readme=root/'README.md';s=readme.read_text().split('\n## LeetQuiz\n')[0];s+='\n## LeetQuiz\n\n[LeetQuiz](questions/leetquiz/leetquiz.html) contains 76 refined questions from four screenshot PDFs, with Bangla explanations, saved progress, review marks, and the same timer and grading behavior as ExamTopics. Names updated for the May 2026 guide have a yellow background.\n\nAcross 158 source pages, 60 duplicate copies and 22 unique questions outside the explicit guide objectives were removed. Substantive corrections to ambiguous/outdated questions are disclosed in their explanations and the [audit](leetquiz/refinement-audit.md). This bank is not complete coverage of every guide objective.\n\nThe four PDFs in `leetquiz/` now contain 21, 18, 24, and 13 unique questions respectively. Original screenshot PDFs remain in `leetquiz/originals/`.\n'
readme.write_text(s)
print('Published page, home integration, audit and four PDFs:',counts)
