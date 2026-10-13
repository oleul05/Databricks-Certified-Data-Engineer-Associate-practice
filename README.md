# Databricks Data Engineer Associate Practice

Interactive practice questions with Bangla explanations, answer grading, saved browser progress, and light/dark themes.

The practice pass mark is 80%; completed-set results and home readiness messages use this threshold.

Open `Databricks_Home.html` in a browser to choose a question set.

Udemy mock exams have a fixed 90-minute timer for 55 questions. Other sets have a countdown of 70 seconds per question (45 questions = 52 minutes 30 seconds). It counts only while the question page is visible. Going home, closing the page, or switching tabs pauses it; returning or refreshing resumes the saved remaining time. Completing the set stops the timer; resetting the set or retrying wrong answers after completion starts a fresh timer. Use Pause/Resume to manually control the countdown; a manual pause stays paused when you return or refresh. Reset Timer starts the full duration again without clearing answers. When time runs out, you can continue practicing.

## Udemy practice exams

Udemy questions are deduplicated and tagged with their May 2026 exam-guide section. All 11 mock exams contain 55 questions and allow 90 minutes. Each retains its original 45 questions and adds 10 from the extra practice pool, with different sections mixed together. The remaining 11 questions are in three extra practice sets.

| Set | Questions |
| --- | ---: |
| [Mock Exam 1](questions/udemy/Databricks_Udemy_Mock_Exam_1.html) | 55 |
| [Mock Exam 2](questions/udemy/Databricks_Udemy_Mock_Exam_2.html) | 55 |
| [Mock Exam 3](questions/udemy/Databricks_Udemy_Mock_Exam_3.html) | 55 |
| [Mock Exam 4](questions/udemy/Databricks_Udemy_Mock_Exam_4.html) | 55 |
| [Mock Exam 5](questions/udemy/Databricks_Udemy_Mock_Exam_5.html) | 55 |
| [Mock Exam 6](questions/udemy/Databricks_Udemy_Mock_Exam_6.html) | 55 |
| [Mock Exam 7](questions/udemy/Databricks_Udemy_Mock_Exam_7.html) | 55 |
| [Mock Exam 8](questions/udemy/Databricks_Udemy_Mock_Exam_8.html) | 55 |
| [Mock Exam 9](questions/udemy/Databricks_Udemy_Mock_Exam_9.html) | 55 |
| [Mock Exam 10](questions/udemy/Databricks_Udemy_Mock_Exam_10.html) | 55 |
| [Mock Exam 11](questions/udemy/Databricks_Udemy_Mock_Exam_11.html) | 55 |
| [Extra Practice 1](questions/udemy/Databricks_Udemy_Extra_Practice_1.html) | 4 |
| [Extra Practice 2](questions/udemy/Databricks_Udemy_Extra_Practice_2.html) | 4 |
| [Extra Practice 3](questions/udemy/Databricks_Udemy_Extra_Practice_3.html) | 3 |

The sets contain 616 unique syllabus questions with Bangla explanations, code, reference links, and original illustrations. Each question label keeps its original exam and question number, so it can be found in the PDFs. Saved answers are kept because they are stored per question.

The 38 Udemy questions flagged as outside the syllabus are in [Syllabus-এর বাইরে](questions/optional/Databricks_Out_of_Syllabus.html), which contains 97 optional questions. Optional questions do not count toward overall syllabus progress.

The twelve original PDFs keep all 640 Udemy questions in their original order with the English explanations:

| Exam | PDF |
| --- | --- |
| 1 | [PDF](output/pdf/udemy%20practice%20exam%201.pdf) |
| 2 | [PDF](output/pdf/udemy%20practice%20exam%202.pdf) |
| 3 | [PDF](output/pdf/udemy%20practice%20exam%203.pdf) |
| 4 | [PDF](output/pdf/udemy%20practice%20exam%204.pdf) |
| 5 | [PDF](output/pdf/udemy%20practice%20exam%205.pdf) |
| 6 | [PDF](output/pdf/udemy%20practice%20exam%206.pdf) |
| 7 | [PDF](output/pdf/udemy%20practice%20exam%207.pdf) |
| 8 | [PDF](output/pdf/udemy%20practice%20exam%208.pdf) |
| 9 | [PDF](output/pdf/udemy%20practice%20exam%209.pdf) |
| 10 | [PDF](output/pdf/udemy%20practice%20exam%2010.pdf) |
| 11 | [PDF](output/pdf/udemy%20practice%20exam%2011.pdf) |
| 12 | [PDF](output/pdf/udemy%20practice%20exam%2012.pdf) |

The flags compare questions with the explicitly listed objectives in the [May 2026 exam guide](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf). These are study-priority judgments, not an official excluded-question list.

## ExamTopics

ExamTopics questions are deduplicated and grouped into three mock exams that follow the section weights in the May 2026 exam guide, plus an extra practice set:

| Set | Questions |
| --- | ---: |
| [Mock Exam 1](questions/examtopics/Databricks_ExamTopics_Mock_Exam_1.html) | 45 |
| [Mock Exam 2](questions/examtopics/Databricks_ExamTopics_Mock_Exam_2.html) | 45 |
| [Mock Exam 3](questions/examtopics/Databricks_ExamTopics_Mock_Exam_3.html) | 45 |
| [Extra Practice](questions/examtopics/Databricks_ExamTopics_Extra_Practice.html) | 74 |

## Databricks Academy

The three Academy quiz sets mix the course topics by exam-guide section, so no two consecutive questions come from the same section. The course quizzes have no Platform questions, so exact exam-guide proportions are not possible for these sets.

The home page also includes other practice sets. Answers are saved in browser local storage.

## Review questions later

Use ☆ Mark for Review on difficult or guessed questions, including correct answers. Stars appear in the question palette. Review Marked Questions opens the saved list during or after the quiz; select a question to revisit its answer and explanation. Click ★ Marked for Review to remove a mark. Review marks stay saved in the same browser, independently of scores and quiz resets.

## Folder layout

`Databricks_Home.html` is the entry point at the repository root. Question pages are grouped under `questions/academy/`, `questions/examtopics/`, `questions/udemy/`, `questions/github/`, and `questions/optional/`. PDFs remain in their existing locations.

After completing a set, the summary shows correct answers, mistakes, and accuracy for each section, ordered by mistake rate. Click a wrong question in the summary to read its answer and explanation. Questions without section tags appear under Other / Unclassified.

## Final exam simulation

Open [Final Mock Exam](questions/mock/Databricks_Final_Mock_Exam.html), also linked from Home. Each attempt selects 55 unique questions only from the syllabus ExamTopics and GitHub pools, with 3 Platform, 12 Ingestion, 12 Transformation, 9 Lakeflow Jobs, 5 CI/CD, 6 Optimization, and 8 Governance questions. These rounded counts follow the May 2026 guide's 6/21/22/16/10/10/15 percent section weights. GitHub questions are manually assigned section tags in this standalone pool.

The 90-minute wall-clock timer continues across tab changes, closure, and refresh, and submits on expiry (on reopening if the page was closed). Answers can be changed and flagged during the exam; grading, correct answers, and Bangla explanations appear only after submission. Results show section scores and the existing 80% practice target. Attempts use separate browser storage and do not change practice-set progress. New attempt returns to the start screen and generates a fresh selection when started.

## LeetQuiz

[LeetQuiz](questions/leetquiz/leetquiz.html) contains 42 questions with Bangla explanations, saved progress, review marks, and the same timer and grading behavior as ExamTopics. Its preserved source bank has 77 refined questions from four screenshot PDFs and accessible downloads; 35 questions overlapping with the syllabus ExamTopics bank were removed from the active page. Names updated for the May 2026 guide have a yellow background.

Across 158 source pages, 60 duplicate copies and 22 unique questions outside the explicit guide objectives were removed. Substantive corrections to ambiguous/outdated questions are disclosed in their explanations and the [audit](leetquiz/refinement-audit.md). This bank is not complete coverage of every guide objective.

The four source-archive PDFs in `leetquiz/` contain 21, 18, 24, and 13 questions respectively. Their historical allocation is preserved and includes questions since removed from the interactive page due to ExamTopics overlap. Original screenshot PDFs remain in `leetquiz/originals/`.

The 12 accessible Next-button downloads add one new time-travel question; 11 overlap with existing LeetQuiz entries and are preserved as source references. See `leetquiz/downloads/import-audit.json`. The four refined PDFs retain their original 76-question allocation.

The larger download collection has 611 Real Exam entries. Together with the 12 Next-button downloads, these contain **197 distinct questions**, after grouping 426 repeated or reworded copies. Browse the [searchable source archive](leetquiz/downloads/unique-questions.html), [Markdown](leetquiz/downloads/unique-questions.md), or [JSON with all source versions](leetquiz/downloads/unique-questions.json). The [source deduplication audit](leetquiz/downloads/unique-questions-audit.json) maps every source entry to its retained source question. This archive preserves source answers and explanations and has not been syllabus-filtered; the active exams below use the reviewed and filtered questions.

The downloaded questions were reviewed against the May 2026 guide: **147 syllabus questions retained and 50 outside the listed objectives excluded**. The original 77-question refined bank also passed this syllabus review. Product-name changes are highlighted yellow in question text, choices, and explanations; behavior/answer corrections are disclosed separately. See the [syllabus audit](leetquiz/downloads/syllabus-refinement-audit.md) for every syllabus decision and correction. These are study-priority judgments against the guide, not an official excluded-question list.

A subsequent comparison with all **209 syllabus ExamTopics questions removed 120 overlapping LeetQuiz entries: 35 from the original bank and 85 from the downloaded bank**. Exact copies, paraphrases, and corrected modernizations of the same source question are grouped; same-topic questions testing different requirements remain. The [cross-bank audit](leetquiz/examtopics-deduplication-audit.md) identifies the retained ExamTopics counterpart for every removal. ExamTopics pages remain unchanged.

The **62 remaining downloads** are mixed across three interactive exam sets linked from Home, and each appears exactly once. Together with the original page's 42 questions, the LeetQuiz section now contains 104 active question entries. Each set has saved progress, review marks, answer grading, section results, and Bangla explanations. Correction notes, syllabus explanations, and reference labels are also in Bangla; code and technical/product names retain their original spelling. Home review lists use the same Bangla explanations. The translations are maintained in `leetquiz/bangla_explanations.py` and are applied during regeneration. Stable question IDs preserve saved answers and review marks for retained questions. Timers restart for changed question/answer set contents, while explanation-only updates keep the timer key.

| Set | Questions | Timer |
| --- | ---: | --- |
| [LeetQuiz Download Exam 1](questions/leetquiz/LeetQuiz_Download_Exam_1.html) | 21 | 24 minutes 30 seconds |
| [LeetQuiz Download Exam 2](questions/leetquiz/LeetQuiz_Download_Exam_2.html) | 21 | 24 minutes 30 seconds |
| [LeetQuiz Download Exam 3](questions/leetquiz/LeetQuiz_Download_Exam_3.html) | 20 | 23 minutes 20 seconds |
