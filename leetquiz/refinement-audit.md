# LeetQuiz refinement audit

Compared against the [May 2026 exam guide](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf).

158 source pages → 98 unique question variants → 76 retained, 22 excluded unique questions. 60 duplicate copies removed.

Syllabus exclusions are study-priority judgments against explicit May 2026 objectives, not an official excluded-question list. Cosmetic renames are yellow; substantive corrections are disclosed separately.

Original screenshot PDFs are preserved in `originals/`. Refined PDF allocation: PDF 1: 21, PDF 2: 18, PDF 3: 24, PDF 4: 13.

## Name updates

| Old name | Current name (yellow in quizzes and PDFs) |
| --- | --- |
| Delta Live Tables / DLT | Lakeflow Spark Declarative Pipelines |
| Databricks Repos | Databricks Git Folders |
| Databricks Asset Bundles | Declarative Automation Bundles |
| Databricks Lakehouse Platform | Databricks Data Intelligence Platform |
| SQL endpoint | SQL warehouse |
| Data Explorer | Catalog Explorer |
| CREATE STREAMING LIVE TABLE / CREATE INCREMENTAL LIVE TABLE | CREATE OR REFRESH STREAMING TABLE |
| CREATE LIVE TABLE | CREATE OR REFRESH MATERIALIZED VIEW |

SQL/object migrations sometimes require behavior or code changes, not just renaming. Those are separately identified as Source correction.

## Excluded unique questions

| First source | Concept | Reason |
| --- | --- | --- |
| PDF 1, page 4 | pivot | Outside the explicitly listed objectives: dynamic SQL PIVOT/category discovery. Original options also fail the stated dynamic-category requirement. |
| PDF 1, page 7 | temperature | Higher-order FILTER/SIZE array processing is not explicitly listed; the guide names exploding arrays. |
| PDF 1, page 9 | tempScope | Temporary/global temporary view lifetime trivia is not a listed objective; retained the separate view-creation use case. |
| PDF 1, page 11 | pipelineOptional | Legacy pipeline configuration-field optionality is not a listed objective and differs in modern Unity Catalog pipelines. |
| PDF 1, page 17 | pyIf | Standalone Python condition syntax is not a listed objective; the guide covers Lakeflow Jobs conditional tasks. |
| PDF 1, page 24 | dashFilters | Browser visualization/query filter tuning is not a listed optimization objective. |
| PDF 1, page 30 | legacyLocation | Legacy Hive/DBFS default database directory is outside the Unity Catalog-focused outline. |
| PDF 2, page 3 | scheduleEnd | SQL query-editor refresh schedule expiry is not the Lakeflow Jobs scheduling objective. |
| PDF 2, page 12 | eventlog | Direct pipeline event-log querying is not a listed monitoring objective; the guide specifies Jobs UI/history and Spark UI. |
| PDF 2, page 13 | classification | Generic sensitivity-classification taxonomy alone is not a listed control objective; the guide specifies privileges, masks, row filters, and ABAC. |
| PDF 2, page 30 | mode | Detailed continuous/triggered plus development/production pipeline compute lifecycle is not a listed objective. |
| PDF 3, page 1 | coauthor | Notebook real-time coauthoring feature trivia is not a listed objective. |
| PDF 3, page 5 | sundayPython | Wrapping SQL in standalone Python weekday control flow is outside the listed Jobs conditional-task objective. |
| PDF 3, page 12 | hof | Listing higher-order Spark SQL functions is not a listed objective. |
| PDF 3, page 17 | shareNotebook | Sharing notebooks with a person lacking workspace access is not a listed Unity Catalog data-access objective. |
| PDF 3, page 18 | pyOutput | Standalone Python function tracing is not a listed objective. |
| PDF 3, page 21 | metastoreColocate | Metastore colocation/performance configuration is not a listed objective. |
| PDF 3, page 29 | notebookRevision | Notebook automatic revision history trivia is not a listed CI/CD objective; Git branches and bundles are. |
| PDF 3, page 40 | dashboardDelay | Legacy dashboard manual-refresh architecture trivia is not a listed objective. |
| PDF 3, page 47 | pythonFunction | Standalone Python function-definition syntax is not a listed objective. |
| PDF 3, page 48 | shallowClone | Shallow/deep clone selection is not an explicitly listed objective. |
| PDF 4, page 36 | alert | Databricks SQL alert creation and refresh scheduling is not a listed Lakeflow Jobs objective. |

## Retained questions and corrections

| Question | Source pages | Section | Correction |
| --- | --- | --- | --- |
| 1: quality | 1:1 | P | Wording consolidated; concept retained. |
| 2: gold | 1:2, 1:3, 1:23 | T | Wording consolidated; concept retained. |
| 3: delta | 1:5 | P | Wording consolidated; concept retained. |
| 4: notebooklibs | 1:6 | T | Reworded notebook libraries as pipeline source files; modern pipelines are not restricted to notebook libraries. |
| 5: concurrency | 1:8 | P | Wording consolidated; concept retained. |
| 6: usage | 1:10 | G | Migrated the legacy database metadata-inspection question to catalog-level BROWSE. This is a privilege-model correction, not a simple rename. |
| 7: dashboardTask | 1:12 | J | Wording consolidated; concept retained. |
| 8: delete | 1:13, 3:13 | T | Wording consolidated; concept retained. |
| 9: expectFail | 1:14 | T | Corrected FAIL syntax and narrowed failure to the affected flow rather than claiming all independent flows stop. |
| 10: autostop | 1:15, 4:17, 4:21 | P | Consolidated equivalent daily-refresh variants; clarified the idle-compute question without relying on legacy dashboard endpoint matching. |
| 11: overwriteSchema | 1:16 | T | Wording consolidated; concept retained. |
| 12: truth | 1:18 | P | Wording consolidated; concept retained. |
| 13: schemaStorage | 1:19 | G | Specified a parent catalog with managed storage; schema creation itself does not create a directory containing data. |
| 14: externalDrop | 1:20 | G | Wording consolidated; concept retained. |
| 15: discount | 1:21 | T | Changed choose two to choose one: only B satisfies the row-level requirements; E duplicates non-discounted rows. |
| 16: vacuum | 1:22 | O | Wording consolidated; concept retained. |
| 17: ucIntegration | 1:25 | P | Narrowed the broad original integration claim to compatible existing data and storage. |
| 18: gitBranches | 1:26, 3:46 | C | Wording consolidated; concept retained. |
| 19: bundle | 1:27 | C | Wording consolidated; concept retained. |
| 20: overwriteHistory | 1:28 | P | Qualified the original claim that all historical versions are preserved indefinitely. |
| 21: grantUI | 1:29, 2:14 | G | Merged Catalog Explorer and Data Explorer wording variants. |
| 22: explodeSQL | 2:1 | T | Wording consolidated; concept retained. |
| 23: overwriteWhy | 2:2 | P | Clarified ambiguous clean-history wording to mean discarding history, making the incorrect claim explicit. |
| 24: tempCreate | 2:4, 2:8, 2:16, 2:22 | T | Wording consolidated; concept retained. |
| 25: merge | 2:5, 2:9 | T | Removed the original guarantee that MERGE automatically handles all duplicates; source rows must have unambiguous matches. |
| 26: explodeDF | 2:6, 2:10 | T | Wording consolidated; concept retained. |
| 27: qualitySchema | 2:7, 2:11 | P | Wording consolidated; concept retained. |
| 28: businessCatalog | 2:15 | G | Wording consolidated; concept retained. |
| 29: managed | 2:17, 2:20 | G | Reworked two conflicting incorrect choices and corrected immediate-delete wording for Unity Catalog managed tables. |
| 30: pull | 2:18, 2:23 | C | Wording consolidated; concept retained. |
| 31: uniqueCategory | 2:19, 2:24 | T | Specified product-name summary output; the original detail-row subquery was also a valid way to find violations and would otherwise make two options correct. |
| 32: queryDelta | 2:21, 2:25 | T | Wording consolidated; concept retained. |
| 33: qualityTool | 2:26, 2:31 | T | Wording consolidated; concept retained. |
| 34: mergeAvoid | 2:27, 2:32 | T | Made key-based duplicate avoidance explicit; MERGE is not a blanket deduplication guarantee. |
| 35: namespace | 2:28, 2:34 | G | Wording consolidated; concept retained. |
| 36: web | 2:29, 2:33, 4:34 | P | Wording consolidated; concept retained. |
| 37: owner | 2:36 | G | Added the metadata-discovery prerequisite; lack of SELECT alone does not guarantee or prevent owner visibility. |
| 38: update | 2:37 | T | Wording consolidated; concept retained. |
| 39: jobstartup | 2:38 | P | Clarified classic job compute and avoided claiming universally higher operational cost. |
| 40: migration | 3:2, 3:8, 4:38 | T | Clarified that no listed architecture change is required, not that the code needs no migration work. |
| 41: joinLeft | 3:3, 3:9, 4:39 | T | Wording consolidated; concept retained. |
| 42: tableCreate | 3:4, 3:6, 4:37 | T | Wording consolidated; concept retained. |
| 43: nestedCity | 3:11 | T | Specified retaining existing columns: the original select-and-alias choice also extracts a top-level field and was otherwise valid. |
| 44: autoWorkloads | 3:14 | I | Avoided the original misleading batch-versus-streaming dichotomy: Auto Loader can support batch-style scheduled processing using AvailableNow. |
| 45: once | 3:15 | I | Corrected source readStream, non-aggregated append output mode, and toTable sink. once=True is legacy/deprecated; retained its ingestion concept with an explicit explanation. |
| 46: storage | 3:16, 3:20, 3:43, 4:26, 4:31 | P | Wording consolidated; concept retained. |
| 47: taskValue | 3:19, 3:23 | J | Wording consolidated; concept retained. |
| 48: salesPy | 3:26 | T | Wording consolidated; concept retained. |
| 49: dateParts | 3:28 | T | Wording consolidated; concept retained. |
| 50: securables | 3:30 | G | Replaced the original Database/Data Location vocabulary with the actual Unity Catalog objects, not a cosmetic product rename. |
| 51: grantSelect | 3:31, 3:32 | G | Corrected principal quoting and stated parent-usage prerequisites. |
| 52: except | 3:33 | T | Wording consolidated; concept retained. |
| 53: autoFeatures | 3:34 | I | Wording consolidated; concept retained. |
| 54: pipelineCreate | 3:35 | J | Updated creation UI and clarified declarative dataset dependencies instead of notebook execution ordering. |
| 55: createEmpty | 3:36, 4:12, 4:16 | T | Merged equivalent empty-table variants and clarified that existing contents may be replaced. |
| 56: streamRead | 3:37, 3:38 | T | Replaced legacy LIVE syntax and corrected the original claim that STREAM proves the source itself is a streaming live table. |
| 57: optimize | 3:39 | O | Wording consolidated; concept retained. |
| 58: vacuumRetention | 3:41 | O | Clarified unreferenced-file retention rather than claiming all files older than one week are deleted. |
| 59: pool | 3:42 | P | Wording consolidated; concept retained. |
| 60: viewLegacyPermission | 3:44 | G | Corrected the old consumer-needs-base-table-SELECT premise for Unity Catalog SQL warehouses and stated the actual failing permission. |
| 61: vacuumPartial | 3:45 | O | Wording consolidated; concept retained. |
| 62: viewCreate | 3:49, 4:22, 4:27 | T | Wording consolidated; concept retained. |
| 63: optimizeWhere | 3:50 | O | Added partition prerequisite and an upper date bound so the query really targets 2022 only. |
| 64: bronze | 4:1, 4:9 | T | Wording consolidated; concept retained. |
| 65: incremental | 4:2, 4:7 | I | Wording consolidated; concept retained. |
| 66: hop | 4:3, 4:6, 4:11 | T | Specified Bronze input and cleaned output; the original raw-table wording could otherwise be ambiguous. |
| 67: jsonStruct | 4:4, 4:8 | T | Wording consolidated; concept retained. |
| 68: transferOwner | 4:5, 4:10 | G | Corrected TO syntax/principal quoting and specified an authorized owner. |
| 69: streamingVsMV | 4:13, 4:18 | T | Updated legacy live-table SQL names to modern streaming table/materialized view syntax. |
| 70: autoStrings | 4:14, 4:19 | I | Clarified the default configuration; being text-based does not universally force JSON readers to produce strings. |
| 71: urlDomain | 4:23, 4:29 | T | Original A and C both extracted the domain and B/D were valid projections. Retaining columns and regex requirement now distinguish one answer; adjusted distractor C. |
| 72: goldSource | 4:24, 4:28 | T | Wording consolidated; concept retained. |
| 73: csv | 4:25, 4:30 | I | Corrected the displayed path to match the stated CSV location; keep required external-location permissions in mind for Unity Catalog. |
| 74: checkpoint | 4:32 | I | Wording consolidated; concept retained. |
| 75: copyIdempotent | 4:33 | I | Made COPY INTO explicit in the question; the original omitted the executed command. |
| 76: autoExactlyOnce | 4:35 | I | Clarified Delta sink and file-ingestion scope; checkpoint state alone does not guarantee every possible external sink. |

## Every original page

| PDF | Page | Concept | Disposition |
| --- | --- | --- | --- |
| 1 | 1 | quality | kept |
| 1 | 2 | gold | kept |
| 1 | 3 | gold | duplicate |
| 1 | 4 | pivot | excluded |
| 1 | 5 | delta | kept |
| 1 | 6 | notebooklibs | kept |
| 1 | 7 | temperature | excluded |
| 1 | 8 | concurrency | kept |
| 1 | 9 | tempScope | excluded |
| 1 | 10 | usage | kept |
| 1 | 11 | pipelineOptional | excluded |
| 1 | 12 | dashboardTask | kept |
| 1 | 13 | delete | kept |
| 1 | 14 | expectFail | kept |
| 1 | 15 | autostop | kept |
| 1 | 16 | overwriteSchema | kept |
| 1 | 17 | pyIf | excluded |
| 1 | 18 | truth | kept |
| 1 | 19 | schemaStorage | kept |
| 1 | 20 | externalDrop | kept |
| 1 | 21 | discount | kept |
| 1 | 22 | vacuum | kept |
| 1 | 23 | gold | duplicate |
| 1 | 24 | dashFilters | excluded |
| 1 | 25 | ucIntegration | kept |
| 1 | 26 | gitBranches | kept |
| 1 | 27 | bundle | kept |
| 1 | 28 | overwriteHistory | kept |
| 1 | 29 | grantUI | kept |
| 1 | 30 | legacyLocation | excluded |
| 2 | 1 | explodeSQL | kept |
| 2 | 2 | overwriteWhy | kept |
| 2 | 3 | scheduleEnd | excluded |
| 2 | 4 | tempCreate | kept |
| 2 | 5 | merge | kept |
| 2 | 6 | explodeDF | kept |
| 2 | 7 | qualitySchema | kept |
| 2 | 8 | tempCreate | duplicate |
| 2 | 9 | merge | duplicate |
| 2 | 10 | explodeDF | duplicate |
| 2 | 11 | qualitySchema | duplicate |
| 2 | 12 | eventlog | excluded |
| 2 | 13 | classification | excluded |
| 2 | 14 | grantUI | duplicate |
| 2 | 15 | businessCatalog | kept |
| 2 | 16 | tempCreate | duplicate |
| 2 | 17 | managed | kept |
| 2 | 18 | pull | kept |
| 2 | 19 | uniqueCategory | kept |
| 2 | 20 | managed | duplicate |
| 2 | 21 | queryDelta | kept |
| 2 | 22 | tempCreate | duplicate |
| 2 | 23 | pull | duplicate |
| 2 | 24 | uniqueCategory | duplicate |
| 2 | 25 | queryDelta | duplicate |
| 2 | 26 | qualityTool | kept |
| 2 | 27 | mergeAvoid | kept |
| 2 | 28 | namespace | kept |
| 2 | 29 | web | kept |
| 2 | 30 | mode | excluded |
| 2 | 31 | qualityTool | duplicate |
| 2 | 32 | mergeAvoid | duplicate |
| 2 | 33 | web | duplicate |
| 2 | 34 | namespace | duplicate |
| 2 | 35 | mode | duplicate |
| 2 | 36 | owner | kept |
| 2 | 37 | update | kept |
| 2 | 38 | jobstartup | kept |
| 3 | 1 | coauthor | excluded |
| 3 | 2 | migration | kept |
| 3 | 3 | joinLeft | kept |
| 3 | 4 | tableCreate | kept |
| 3 | 5 | sundayPython | excluded |
| 3 | 6 | tableCreate | duplicate |
| 3 | 7 | coauthor | duplicate |
| 3 | 8 | migration | duplicate |
| 3 | 9 | joinLeft | duplicate |
| 3 | 10 | sundayPython | duplicate |
| 3 | 11 | nestedCity | kept |
| 3 | 12 | hof | excluded |
| 3 | 13 | delete | duplicate |
| 3 | 14 | autoWorkloads | kept |
| 3 | 15 | once | kept |
| 3 | 16 | storage | kept |
| 3 | 17 | shareNotebook | excluded |
| 3 | 18 | pyOutput | excluded |
| 3 | 19 | taskValue | kept |
| 3 | 20 | storage | duplicate |
| 3 | 21 | metastoreColocate | excluded |
| 3 | 22 | shareNotebook | duplicate |
| 3 | 23 | taskValue | duplicate |
| 3 | 24 | pyOutput | duplicate |
| 3 | 25 | metastoreColocate | duplicate |
| 3 | 26 | salesPy | kept |
| 3 | 27 | legacyLocation | duplicate |
| 3 | 28 | dateParts | kept |
| 3 | 29 | notebookRevision | excluded |
| 3 | 30 | securables | kept |
| 3 | 31 | grantSelect | kept |
| 3 | 32 | grantSelect | duplicate |
| 3 | 33 | except | kept |
| 3 | 34 | autoFeatures | kept |
| 3 | 35 | pipelineCreate | kept |
| 3 | 36 | createEmpty | kept |
| 3 | 37 | streamRead | kept |
| 3 | 38 | streamRead | duplicate |
| 3 | 39 | optimize | kept |
| 3 | 40 | dashboardDelay | excluded |
| 3 | 41 | vacuumRetention | kept |
| 3 | 42 | pool | kept |
| 3 | 43 | storage | duplicate |
| 3 | 44 | viewLegacyPermission | kept |
| 3 | 45 | vacuumPartial | kept |
| 3 | 46 | gitBranches | duplicate |
| 3 | 47 | pythonFunction | excluded |
| 3 | 48 | shallowClone | excluded |
| 3 | 49 | viewCreate | kept |
| 3 | 50 | optimizeWhere | kept |
| 4 | 1 | bronze | kept |
| 4 | 2 | incremental | kept |
| 4 | 3 | hop | kept |
| 4 | 4 | jsonStruct | kept |
| 4 | 5 | transferOwner | kept |
| 4 | 6 | hop | duplicate |
| 4 | 7 | incremental | duplicate |
| 4 | 8 | jsonStruct | duplicate |
| 4 | 9 | bronze | duplicate |
| 4 | 10 | transferOwner | duplicate |
| 4 | 11 | hop | duplicate |
| 4 | 12 | createEmpty | duplicate |
| 4 | 13 | streamingVsMV | kept |
| 4 | 14 | autoStrings | kept |
| 4 | 15 | dashboardDelay | duplicate |
| 4 | 16 | createEmpty | duplicate |
| 4 | 17 | autostop | duplicate |
| 4 | 18 | streamingVsMV | duplicate |
| 4 | 19 | autoStrings | duplicate |
| 4 | 20 | dashboardDelay | duplicate |
| 4 | 21 | autostop | duplicate |
| 4 | 22 | viewCreate | duplicate |
| 4 | 23 | urlDomain | kept |
| 4 | 24 | goldSource | kept |
| 4 | 25 | csv | kept |
| 4 | 26 | storage | duplicate |
| 4 | 27 | viewCreate | duplicate |
| 4 | 28 | goldSource | duplicate |
| 4 | 29 | urlDomain | duplicate |
| 4 | 30 | csv | duplicate |
| 4 | 31 | storage | duplicate |
| 4 | 32 | checkpoint | kept |
| 4 | 33 | copyIdempotent | kept |
| 4 | 34 | web | duplicate |
| 4 | 35 | autoExactlyOnce | kept |
| 4 | 36 | alert | excluded |
| 4 | 37 | tableCreate | duplicate |
| 4 | 38 | migration | duplicate |
| 4 | 39 | joinLeft | duplicate |
| 4 | 40 | sundayPython | duplicate |
