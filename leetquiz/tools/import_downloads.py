"""Merge the saved Next-button download into the LeetQuiz page without duplicate questions."""
from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parents[2]
qs=json.loads((root/'leetquiz/refined-questions.json').read_text())
raw=json.loads((root/'leetquiz/downloads/questions.json').read_text())
keys=['migration','mergeAvoid','tableCreate','truth','pool','web','delta','storage','delete','vacuumTimeTravel','quality','gitBranches']
assert len(raw)==len(keys)
lookup={q['key']:q for q in qs}
report=[]
for i,(source,key) in enumerate(zip(raw,keys),1):
 if key in lookup:
  q=lookup[key];status='merged with existing question'
 else:
  q={'key':key,'uid':'lq-'+key,'sec':'P','n':len(qs)+1,'label':f'LeetQuiz #{len(qs)+1} · Platform · Download #10','stem':source['stemHtml'],'options':[{'k':o['key'],'html':o['html']} for o in source['options']],'answer':['A'],'oos':False,'reference':'https://docs.databricks.com/aws/en/delta/vacuum','correction':'Time travel requires both transaction history and the referenced data files. VACUUM only removes unreferenced files past its retention threshold; the default is seven days. This scenario assumes the needed files were eligible under the configured retention policy.','sources':[],'origin_pdf':None,'sourcePage':None}
  q['explain']='<p class="ans">✅ সঠিক উত্তর: A</p><h3>ব্যাখ্যা</h3><p>Delta time travel-এর জন্য transaction log-এর সঙ্গে সেই version-এর data file-ও থাকতে হয়। VACUUM configured retention পার হওয়া unreferenced file মুছে দিলে পুরোনো version restore/read করা যায় না।</p><p>Default retention ৭ দিন। শুধু তিন দিন আগের version বলেই VACUUM তার file মুছে দেয় না; প্রশ্নে প্রয়োজনীয় file retention policy অনুযায়ী deletion-এর জন্য eligible ছিল ধরে নেওয়া হয়েছে। OPTIMIZE compaction করে, কিন্তু পুরোনো file তাৎক্ষণিকভাবে delete করে না। TIME TRAVEL ও DELETE HISTORY নামে এই কাজের standard command নেই।</p><p><a href="'+q['reference']+'" target="_blank" rel="noopener noreferrer">Databricks VACUUM documentation</a></p>'
  qs.append(q);lookup[key]=q;status='added'
 urls=q.setdefault('download_sources',[])
 if source['url'] not in urls:urls.append(source['url'])
 if 'Downloaded source' not in q['explain']:
  q['explain']+='<p><a href="'+html.escape(source['url'],quote=True)+'" target="_blank" rel="noopener noreferrer">Downloaded source</a></p>'
 report.append({'download':i,'source':source['url'],'uid':q['uid'],'status':status})
count=len(qs);bn=str(count).translate(str.maketrans('0123456789','০১২৩৪৫৬৭৮৯'))
(root/'leetquiz/refined-questions.json').write_text(json.dumps(qs,ensure_ascii=False,indent=2))
pagepath=root/'questions/leetquiz/leetquiz.html';page=pagepath.read_text()
page=re.sub(r'const QUESTIONS = .*?;\n',lambda m:'const QUESTIONS = '+json.dumps(qs,ensure_ascii=False)+';\n',page,count=1)
page=re.sub(r'[০-৯]+টি unique প্রশ্ন',bn+'টি unique প্রশ্ন',page)
page=re.sub(r'\d+ unique syllabus questions from 158 source pages\.',f'{count} unique syllabus questions from the four PDFs and accessible downloads.',page)
pagepath.write_text(page)
homepath=root/'Databricks_Home.html';home=homepath.read_text();pages=json.loads(re.search(r'const PAGES = (.*?);\n',home)[1])
for p in pages:
 if p['id']=='leetquiz':
  p['subtitle']=bn+'টি unique প্রশ্ন · May 2026 syllabus · updated নাম হলুদ'
  p['qs']=[[q['uid'],''.join(q['answer']),None,i] for i,q in enumerate(qs)]
home=re.sub(r'const PAGES = .*?;\n',lambda m:'const PAGES = '+json.dumps(pages,ensure_ascii=False)+';\n',home,count=1)
review=json.loads(re.search(r'const REVIEW_QUESTIONS = (.*?);\n',home)[1]);review=[q for q in review if not q['uid'].startswith('lq-')]
review.extend({**q,'setTitle':'LeetQuiz','file':'questions/leetquiz/leetquiz.html','index':i} for i,q in enumerate(qs))
home=re.sub(r'const REVIEW_QUESTIONS = .*?;\n',lambda m:'const REVIEW_QUESTIONS = '+json.dumps(review,ensure_ascii=False)+';\n',home,count=1);homepath.write_text(home)
(root/'leetquiz/downloads/import-audit.json').write_text(json.dumps(report,indent=2))
readme=root/'README.md';s=readme.read_text();s=re.sub(r'contains \d+ refined questions from four screenshot PDFs',f'contains {count} refined questions from four screenshot PDFs and accessible downloads',s)
line='The 12 accessible Next-button downloads add one new time-travel question; 11 overlap with existing LeetQuiz entries and are preserved as source references. See `leetquiz/downloads/import-audit.json`. The four refined PDFs retain their original 76-question allocation.\n'
if line not in s:s+='\n'+line
readme.write_text(s)
print(f'{count} unique questions; 11 merged source references; 1 added')
