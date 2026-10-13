"""Apply a manually reviewed May 2026 syllabus decision to every download."""
import collections
import copy
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDE = 'https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf'
SECTIONS = {'P': 'Platform', 'I': 'Ingestion', 'T': 'Transformation', 'J': 'Lakeflow Jobs',
            'C': 'CI/CD', 'O': 'Optimization', 'G': 'Governance'}
OBJECTIVES = {
    'P': 'Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection.',
    'I': 'Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input.',
    'T': 'Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation.',
    'J': 'Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow.',
    'C': 'Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets.',
    'O': 'Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization.',
    'G': 'Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters.',
}

# Each exclusion was reviewed against the objectives on guide pages 2-4.
EXCLUSION_GROUPS = {
    'Notebook coauthoring feature trivia is not a listed Git-development objective.': [9],
    'Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective.': [20, 26, 52, 62, 76, 195],
    'Legacy Hive/DBFS database location or external-Parquet cache behavior is outside the Unity Catalog-focused operations in the guide.': [13, 16, 44, 196],
    'Legacy Z-Ordering-specific layout selection is not a cosmetic rename to Liquid Clustering; the current guide names Liquid Clustering and predictive optimization.': [12],
    'Development/production and continuous/triggered declarative-pipeline compute lifecycle trivia is not listed.': [37, 92, 101],
    'SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring.': [38, 43, 48, 89, 125, 194],
    'PII COMMENT syntax alone does not implement the listed masking, row filters, or ABAC policies.': [58],
    'Higher-order array FILTER/custom SQL UDF creation and PIVOT are not the explicitly listed explode, column manipulation, and DataFrame aggregation objectives.': [64, 106, 115],
    'Job email-notification setup is outside the listed task/control-flow, scheduling, and UI-status objectives.': [122],
    'Predicate push-down plans, EXPLAIN syntax, and Dynamic File Pruning feature trivia are not the listed stage-metric bottlenecks or tuning parameters.': [126, 147, 158],
    'Shallow/deep clone behavior and clone-specific recovery are not listed basic managed/external table operations.': [131, 159, 181],
    'Streaming watermark horizon/state-retention semantics are beyond the listed basic DataFrame deduplication objective.': [134],
    'Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives.': [137, 153, 160, 171, 186],
    'Legacy dbutils secret-scope ACL configuration is outside the listed Unity Catalog UI/SQL privileges and masking objectives.': [138],
    'Generic end-to-end testing terminology is not one of the listed CI/CD deployment objectives.': [139],
    'MLflow model inference and Dialogflow voice integration are outside this data-engineering exam outline.': [141, 145],
    'Legacy extreme-throughput cluster-topology guarantees cannot be retained through a product-name-only update.': [143],
    'Identity-column generation/ALTER restrictions are outside the listed basic column manipulation and table-lifecycle objectives.': [148, 173],
    'System-table lineage/access-frequency and query-audit lookups are not the listed governance controls.': [162, 175],
    'Delta Sharing recipients/connectors are not listed in the guide.': [169, 189],
    'A fixed default catalog name is workspace/session dependent; default-catalog trivia is not an explicit objective.': [192],
}

# Explicit section assignment for every retained question (stable source IDs).
SECTION_ITEMS = {
    'P': '1 2 3 7 8 22 42 46 50 51 53 63 65 67 68 70 71 84 85 110 111 113 114 135 149 150 154 161 168 177 190',
    'I': '19 27 28 29 30 57 69 79 82 87 99 103 104 105 120 121 128 142 156 157 167 178 183',
    'T': '10 11 15 17 18 21 23 24 25 31 32 33 35 36 54 56 66 73 74 75 77 78 80 81 83 86 90 91 94 97 98 100 102 116 118 119 124 127 129 132 146 151 152 172 179 182 185 187 197',
    'J': '34 39 40 41 72 96 176 184',
    'C': '6 61 108 109 130 140 164 180',
    'O': '60 93 95 112 133 144 163 170',
    'G': '4 5 14 45 47 49 55 59 88 107 117 123 136 155 165 166 174 188 191 193',
}

RENAMES = {
    'CREATE STREAMING LIVE TABLE': 'CREATE OR REFRESH STREAMING TABLE',
    'CREATE INCREMENTAL LIVE TABLE': 'CREATE OR REFRESH STREAMING TABLE',
    'CREATE OR REFRESH LIVE TABLE': 'CREATE OR REFRESH MATERIALIZED VIEW',
    'CREATE LIVE TABLE': 'CREATE OR REFRESH MATERIALIZED VIEW',
    'STREAMING LIVE TABLE': 'STREAMING TABLE',
    'LIVE TABLE': 'MATERIALIZED VIEW',
    'Databricks Lakehouse Platform': 'Databricks Data Intelligence Platform',
    'Databricks Lakehouse Architecture': 'Databricks Data Intelligence Platform architecture',
    'Delta Live Tables': 'Lakeflow Spark Declarative Pipelines',
    'Delta Live Table': 'Lakeflow Spark Declarative Pipeline',
    'DLT': 'Lakeflow Spark Declarative Pipelines',
    'Databricks Asset Bundles': 'Declarative Automation Bundles',
    'Databricks Asset Bundle': 'Declarative Automation Bundle',
    'Databricks Repos': 'Databricks Git Folders',
    'Databricks Repo': 'Databricks Git Folder',
    'Repos': 'Git Folders',
    'SQL endpoint': 'SQL warehouse',
    'SQL endpoints': 'SQL warehouses',
    'Data Explorer': 'Catalog Explorer',
    'Databricks Jobs': 'Lakeflow Jobs',
    'Databricks Job': 'Lakeflow Job',
    'Jobs UI': 'Lakeflow Jobs UI',
    'Jobs page': 'Jobs & Pipelines page',
    'is_member': 'is_account_group_member',
}
REFERENCES = {
    'privileges': 'https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference',
    'ownership': 'https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/',
    'managed': 'https://docs.databricks.com/aws/en/tables/managed',
    'git': 'https://docs.databricks.com/aws/en/repos/git-operations-with-repos',
    'pipelines': 'https://docs.databricks.com/aws/en/ldp/developer/sql-dev',
    'sql_compute': 'https://docs.databricks.com/aws/en/compute/sql-warehouse/warehouse-behavior',
    'alter': 'https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-alter-table',
}


def highlight(new, old):
    return '<span class="rn-new" title="Previously: ' + html.escape(old, quote=True) + '">' + html.escape(new) + '</span>'


def update_text(text, number, updates):
    renames = dict(RENAMES)
    if number in (5, 49, 59):
        renames.update({'DATABASE': 'SCHEMA', 'database': 'schema', 'databases': 'schemas'})
    pattern = re.compile(r'\b(' + '|'.join(re.escape(s) for s in sorted(renames, key=len, reverse=True)) + r')\b(?!\.[A-Za-z_])', re.I)
    by_lower = {k.lower(): v for k, v in renames.items()}
    plain, marked, start = [], [], 0
    for match in pattern.finditer(text):
        old = match.group()
        new = by_lower[old.lower()]
        plain.extend([text[start:match.start()], new])
        marked.extend([html.escape(text[start:match.start()]), highlight(new, old)])
        updates.add((old, new))
        start = match.end()
    plain.append(text[start:]); marked.append(html.escape(text[start:]))
    return ''.join(plain), '<div style="white-space: pre-wrap">' + ''.join(marked) + '</div>'


def override(q, stem=None, options=None, correct=None, explanation=None, note='', reference=None):
    if stem is not None:
        q['stem'] = stem
    if options is not None:
        q['options'] = [{'key': key, 'text': text, 'html': '', 'correct': key in (correct or [])} for key, text in options.items()]
    elif correct is not None:
        for option in q['options']:
            option['correct'] = option['key'] in correct
    if explanation is not None:
        q['explanation'] = explanation
    if note:
        q['corrections'].append(note)
    if reference:
        q['documentation'].append(reference)


def correct_source(q, number):
    # These corrections retain the tested objective and are disclosed separately
    # from cosmetic product renames. Original downloads remain untouched.
    if number in (10, 103):
        complete = max(q['variants'], key=lambda v: len(v['stem']))
        override(q, stem=complete['stem'], options={o['key']: o['text'] for o in complete['options']},
                 correct=[o['key'] for o in complete['options'] if o.get('correct')], explanation=complete.get('explanation', ''),
                 note='Restored the full schema/command and question prompt from a complete downloaded source version.')
    if number == 5:
        override(q, stem='A new data engineer already has USE CATALOG on main and USE SCHEMA on main.retail. Which command grants read access to the Unity Catalog table main.retail.sales?',
                 options={'A': 'GRANT USE SCHEMA ON TABLE main.retail.sales TO `new.engineer@company.com`;',
                          'B': 'GRANT CREATE TABLE ON TABLE main.retail.sales TO `new.engineer@company.com`;',
                          'C': 'GRANT SELECT ON TABLE main.retail.sales TO `new.engineer@company.com`;',
                          'D': 'GRANT MODIFY ON TABLE main.retail.sales TO `new.engineer@company.com`;',
                          'E': 'GRANT USE CATALOG ON CATALOG main TO `new.engineer@company.com`;'}, correct=['C'],
                 explanation='SELECT grants read access. USE CATALOG and USE SCHEMA are required parent privileges but do not themselves grant SELECT.',
                 note='Updated legacy database USAGE assumptions to Unity Catalog parent privileges, qualified the table, and quoted the principal.', reference=REFERENCES['privileges'])
    if number == 14:
        override(q, stem='A junior data engineer needs to create a managed Delta table main.retail.my_table. Unity Catalog should manage its metadata and data-file lifecycle, using the configured managed storage. Which command should they run?',
                 options={'A': "CREATE TABLE main.retail.my_table (id STRING, value STRING) USING DELTA LOCATION 's3://external-data/my_table';",
                          'B': 'CREATE MANAGED TABLE main.retail.my_table (id STRING, value STRING) USING DELTA;',
                          'C': 'CREATE VIEW main.retail.my_table AS SELECT 1 AS id;',
                          'D': 'CREATE TABLE main.retail.my_table (id STRING, value STRING) USING DBFS;',
                          'E': 'CREATE TABLE main.retail.my_table (id STRING, value STRING) USING DELTA;'}, correct=['E'],
                 explanation='CREATE TABLE without LOCATION creates a managed table. Unity Catalog selects its managed storage and manages its lifecycle. A table created with an external LOCATION is external.',
                 note='Kept the managed-versus-external creation concept; replaced legacy DBFS storage assumptions with Unity Catalog managed storage.', reference=REFERENCES['managed'])
    if number == 35:
        q['stem'] = q['stem'].replace('```', '')
        q['explanation'] += '\nThe current SQL declaration for this materialized result is CREATE OR REFRESH MATERIALIZED VIEW; keep the SELECT query as its definition.'
    if number == 49:
        q['explanation'] += '\nIn Unity Catalog, a schema managed location can be configured explicitly or inherited from its catalog. Do not assume the legacy Hive/DBFS warehouse path.'
    if number == 50:
        override(q, correct=['D'], explanation='Serverless SQL warehouses provide fast startup with infrastructure managed by Databricks. Increasing warehouse size mainly addresses query execution capacity after startup; Auto Stop controls idle shutdown rather than making a stopped warehouse start faster.',
                 note='Corrected the source answer from increasing warehouse size to using serverless SQL for a cold-start delay.', reference=REFERENCES['sql_compute'])
    if number == 47:
        q['stem'] = 'A group team needs all the capabilities included in ALL PRIVILEGES on the Unity Catalog table main.retail.sales. Assume required USE CATALOG and USE SCHEMA privileges already exist. Which grant is correct?'
        for option in q['options']:
            option['text'] = option['text'].replace('new.engineer@company.com', '`team`').replace('ON TABLE sales', 'ON TABLE main.retail.sales')
        q['explanation'] = 'GRANT ALL PRIVILEGES ON TABLE main.retail.sales TO `team` grants applicable table capabilities. MANAGE is not included in ALL PRIVILEGES; granting all applicable privileges is not a transfer of ownership.'
        q['corrections'].append('Qualified the Unity Catalog table, quoted the principal, and clarified the scope of ALL PRIVILEGES.')
        q['documentation'].append(REFERENCES['privileges'])
    if number == 55:
        override(q, stem='A group named team needs to discover tables and inspect metadata in the Unity Catalog catalog customers without reading table data. Which catalog-wide grant should an authorized administrator use?',
                 options={'A': 'GRANT SELECT ON CATALOG customers TO `team`;',
                          'B': 'GRANT CREATE SCHEMA ON CATALOG customers TO `team`;',
                          'C': 'GRANT MODIFY ON CATALOG customers TO `team`;',
                          'D': 'GRANT USE SCHEMA ON SCHEMA customers.default TO `team`;',
                          'E': 'GRANT BROWSE ON CATALOG customers TO `team`;'}, correct=['E'],
                 explanation='BROWSE allows catalog-wide object discovery and metadata inspection without granting access to table data.',
                 note='Updated the legacy USAGE-for-discovery question to the Unity Catalog BROWSE privilege; this is a behavior correction, not a product rename.', reference=REFERENCES['privileges'])
    if number == 59:
        override(q, stem='A group team needs the capabilities included in ALL PRIVILEGES on the Unity Catalog database main.customers. Which grant is correct? Privileges excluded from ALL PRIVILEGES, such as MANAGE, would need separate grants.',
                 options={'A': 'GRANT USE SCHEMA ON SCHEMA main.customers TO `team`;',
                          'B': 'GRANT ALL PRIVILEGES ON SCHEMA team TO `customers`;',
                          'C': 'GRANT SELECT ON SCHEMA main.customers TO `team`;',
                          'D': 'GRANT CREATE TABLE ON SCHEMA main.customers TO `team`;',
                          'E': 'GRANT ALL PRIVILEGES ON DATABASE main.customers TO `team`;'}, correct=['E'],
                 explanation='Grant ALL PRIVILEGES on the schema to the group. ALL PRIVILEGES includes applicable privileges but does not include MANAGE or external-use privileges.',
                 note='Qualified the Unity Catalog schema and clarified that ALL PRIVILEGES is not ownership and does not include every privilege.', reference=REFERENCES['privileges'])
    if number in (28, 32, 80, 98):
        q['stem'] = re.sub(r'spark\.table\(', 'spark.readStream.table(', q['stem'])
        q['stem'] = q['stem'].replace('.withcolumn(', '.withColumn(')
        for option in q['options']:
            option['text'] = re.sub(r'spark\.table\(', 'spark.readStream.table(', option['text'])
        q['explanation'] = re.sub(r'spark\.table\(', 'spark.readStream.table(', q.get('explanation', ''))
        q['corrections'].append('Corrected the source example to use spark.readStream.table before writeStream; spark.table produces a batch DataFrame.')
    if number == 90:
        override(q, stem='A data engineer wants to execute a SQL query containing a Python variable table_name and work with the result as a PySpark DataFrame. Fill the blank:\n____(f"SELECT customer_id, spend FROM {table_name}")',
                 note='Restored the missing command placeholder in the downloaded prompt.')
    if number == 94:
        override(q, stem="Why is STREAM used in this Delta Live Tables query?\nCREATE STREAMING LIVE TABLE loyal_customers AS\nSELECT customer_id FROM STREAM(customers) WHERE loyalty_level = 'high';",
                 options={'A': 'STREAM is unnecessary and always causes an error.',
                          'B': 'The target is only a batch materialized view.',
                          'C': 'The source is read with streaming semantics so new rows can be processed incrementally.',
                          'D': 'The source must be a Python DataFrame variable.',
                          'E': 'It guarantees that the source changed since the last update.'}, correct=['C'],
                 explanation='STREAM reads the source incrementally with streaming semantics. It does not require the source itself to be defined as a streaming table. Current SQL uses CREATE OR REFRESH STREAMING TABLE; the legacy LIVE namespace is unnecessary in modern pipelines.',
                 note='Removed a stray minus sign and legacy LIVE qualifier, and corrected the claim that STREAM requires a streaming-table source.', reference=REFERENCES['pipelines'])
    if number == 107:
        override(q, stem='A table owner has left the organization. An authorized administrator must transfer ownership of the Unity Catalog table to a new principal using Data Explorer. Which listed role can perform this transfer across the metastore?',
                 options={'A': 'Databricks account representative', 'B': 'Any workspace user',
                          'C': 'Unity Catalog metastore administrator', 'D': 'Any newly appointed project lead'}, correct=['C'],
                 explanation='A metastore administrator can transfer ownership. Owners of the parent catalog/schema and users with the appropriate MANAGE privilege can also transfer ownership within their authority. Workspace-admin status alone is not a universal grant on all metastore tables.',
                 note='Replaced the legacy workspace-admin-only ownership claim with Unity Catalog authorization.', reference=REFERENCES['ownership'])
    if number == 109:
        override(q, stem='When working in Databricks Repos, which operation combines changes from another branch into the current branch?',
                 explanation='Merge combines another branch into the current branch. Databricks Git Folders supports merging and conflict resolution in the workspace UI.',
                 note='Removed the obsolete claim that merge must be performed outside the workspace; the Git branch-integration concept is retained.', reference=REFERENCES['git'])
    if number == 117:
        override(q, stem='A Unity Catalog table is dropped with DROP TABLE IF EXISTS main.retail.my_table. Unity Catalog manages its underlying data lifecycle and schedules data deletion after the recovery period. Which type of table was dropped?',
                 explanation='A managed table has its metadata and underlying data lifecycle managed by Unity Catalog. Dropping it does not guarantee immediate physical deletion: an asynchronous purge follows the recovery period. Dropping an external table leaves its external data files.',
                 note='Updated immediate-deletion wording to the Unity Catalog recovery and asynchronous-purge behavior.', reference=REFERENCES['managed'])
    if number == 118:
        override(q, options={'A': 'When the storage location needs to change.',
                             'B': 'Whenever the target table is external, regardless of row matching.',
                             'C': 'When matching keys must be checked so updates or inserts do not blindly append duplicate rows.'}, correct=['C'],
                 explanation='MERGE INTO uses a join condition and matched/not-matched actions to perform conditional updates or inserts. INSERT INTO appends rows without that target-key matching. The source itself should also be prepared to avoid duplicate matching rows.',
                 note='Restored the target-key matching scenario missing from the downloaded choices; deleting the source table is not a reason to choose MERGE.')
    if number == 121:
        override(q, stem='Which workload model does Auto Loader use to incrementally process files? A bounded ingestion run can use an availableNow trigger.',
                 options={'A': 'Structured Streaming', 'B': 'Machine learning model training',
                          'C': 'Every serverless workload regardless of API', 'D': 'Only spark.read batch DataFrames',
                          'E': 'Dashboard rendering'}, correct=['A'],
                 explanation='Auto Loader uses Structured Streaming. A trigger such as availableNow can process a bounded set of currently available files and stop; this does not change the underlying API to spark.read.',
                 note='Clarified the ambiguous workload question and removed the incorrect second marked answer for conventional batch workloads.')
    if number == 127:
        override(q, stem='A data analyst has a SQL query against a Delta table. The data engineering team needs to execute that query and obtain a PySpark DataFrame for data-quality checks. Which operation executes the SQL query?', correct=['C'],
                 explanation='spark.sql executes a SQL query and returns a DataFrame. spark.table reads a registered table by name; it does not execute an arbitrary SQL query string.',
                 note='Clarified SQL-query execution and corrected the extra marked spark.table option for this requirement.')
    if number == 142:
        q['stem'] = 'An Auto Loader stream is configured for directory listing, without file-notification or managed-file-event discovery. Which statement describes how it ingests new files?'
        q['corrections'].append('Made the discovery-mode assumption explicit rather than claiming that all Auto Loader configurations have a fixed default.')
    if number == 136:
        q['stem'] = q['stem'].replace('Users in the workspace are configured into groups', 'Users are configured into Unity Catalog account groups')
        q['explanation'] += '\nFor Unity Catalog account-group membership, use is_account_group_member. The row-filter logic is unchanged: users outside auditing receive only rows with age >= 18.'
        q['corrections'].append('Updated the membership check to account groups for Unity Catalog while retaining the same row-security condition.')
    if number == 146:
        q['stem'] = 'How do you reference another table defined in the same modern Delta Live Tables pipeline using SQL?'
        for option in q['options']:
            if option.get('correct'):
                option['text'] = 'FROM table_name'
        q['explanation'] = 'Refer to the pipeline dataset by name. The LIVE virtual schema is a legacy compatibility mechanism; modern pipelines use the configured catalog/schema and do not require LIVE.table_name.'
        q['corrections'].append('Updated the legacy LIVE namespace requirement while retaining the pipeline dataset-reference concept.')
        q['documentation'].append(REFERENCES['pipelines'])
    if number == 152:
        q['stem'] = 'For an append-only streaming source, what is the primary difference between a materialized view and a streaming table in a Lakeflow pipeline?'
        q['corrections'].append('Scoped the append-only claim to an append-only source; it is not a universal statement about every streaming-table flow.')
    if number == 154:
        for option in q['options']:
            if option.get('correct'):
                option['text'] = 'Intelligent Workload Management manages compute capacity and query queues dynamically without user-managed infrastructure.'
        q['explanation'] = 'Serverless SQL warehouses use Intelligent Workload Management to manage capacity and query workloads. Idle shutdown follows configured Auto Stop behavior; zero-latency startup and immediate shutdown are not guarantees.'
        q['corrections'].append('Removed unsupported instant-scale-to-zero and instant-startup guarantees.')
        q['documentation'].append(REFERENCES['sql_compute'])
    if number == 170:
        override(q, stem='A join spills to disk because too few shuffle partitions create very large tasks. Which action directly addresses this cause?',
                 options={'A': 'Increase spark.sql.shuffle.partitions, then re-measure task size and spill metrics.',
                          'B': 'Reduce the number of shuffle partitions.', 'C': 'Always coalesce all shuffle partitions into one.',
                          'D': 'Convert the Delta tables to plain Parquet solely to remove the shuffle.'}, correct=['A'],
                 explanation='Increasing the number of shuffle partitions can reduce per-task data volume. Re-measure in the Spark UI; do not assume a universal numeric setting. AQE coalescing primarily combines small partitions and is not the direct remedy for too few large partitions.',
                 note='Corrected the source recommendation to coalesce partitions when the stated problem is too few large partitions.')
    if number == 174:
        q['stem'] = 'Assuming a user has required parent usage privileges and no other table grants, which SQL privilege grants read access without granting modification or deletion?'
        q['explanation'] = 'SELECT grants read access. It does not grant MODIFY. It also does not revoke modification permissions the user may already have through another grant or group.'
        q['corrections'].append('Clarified that granting SELECT does not explicitly deny or revoke pre-existing modification privileges.')
        q['documentation'].append(REFERENCES['privileges'])
    if number == 190:
        for option in q['options']:
            if option.get('correct'):
                option['text'] = 'They provide fast startup and Databricks-managed infrastructure.'
        q['explanation'] = 'Serverless SQL warehouses provide fast startup and infrastructure managed by Databricks. Fast startup is a benefit, not a guarantee of zero elapsed startup time.'
        q['corrections'].append('Replaced the absolute instant-startup guarantee with fast startup.')
        q['documentation'].append(REFERENCES['sql_compute'])
    if number == 193:
        override(q, stem='An engineer needs to use ALTER COLUMN and SET TBLPROPERTIES on a Unity Catalog table. Assuming required parent usage privileges, which is the least-privilege table grant among these options?', correct=['C'],
                 explanation='MODIFY permits ALTER COLUMN, ADD/DROP COLUMN, and SET/UNSET TBLPROPERTIES. Other ALTER TABLE operations can require ownership or MANAGE; do not assume every alteration uses the same permission.',
                 note='Specified the ALTER operations and corrected the least-privilege answer to MODIFY.', reference=REFERENCES['alter'])


def build():
    source = json.loads((ROOT / 'downloads/unique-questions.json').read_text(encoding='utf-8'))
    exclusions = {i: reason for reason, ids in EXCLUSION_GROUPS.items() for i in ids}
    sections = {int(i): sec for sec, items in SECTION_ITEMS.items() for i in items.split()}
    assert not (sections.keys() & exclusions.keys())
    assert sections.keys() | exclusions.keys() == set(range(1, 198)), 'Every source question needs an explicit decision'
    retained, audit_rows = [], []
    for original in source:
        number = int(original['id'].split('-')[1])
        row = {'uid': original['id'], 'sourceStem': original['stem'], 'status': 'excluded' if number in exclusions else 'kept',
               'reason': exclusions.get(number, OBJECTIVES.get(sections.get(number, ''), '')), 'sources': original['sources']}
        if number in exclusions:
            audit_rows.append(row)
            continue
        q = copy.deepcopy(original)
        q['sec'] = sections[number]
        q['guideObjective'] = OBJECTIVES[q['sec']]
        q['corrections'], q['documentation'] = [], []
        correct_source(q, number)
        if number == 124:
            q['stem'] = q['stem'].replace('(formerly CREATE INCREMENTAL LIVE TABLE)', '')
        # Strip embedded source numbering while keeping the stable lqd ID.
        q['stem'] = re.sub(r'^\s*(?:Question\s+\d+\s*[:.]?\s*|\d+\.\s*)', '', q['stem'], flags=re.I)
        updates = set()
        q['stem'], q['displayStem'] = update_text(q['stem'], number, updates)
        for option in q['options']:
            option['text'], option['displayHtml'] = update_text(option['text'], number, updates)
        q['explanation'], q['displayExplanation'] = update_text(q.get('explanation', ''), number, updates)
        # Add visibly marked updates for semantic changes whose original text was
        # replaced in an override; these are also disclosed as corrections.
        for n, current, previous in [(5, 'USE CATALOG', 'legacy database USAGE'),
                                      (14, 'Unity Catalog', 'legacy DBFS managed storage'),
                                      (55, 'BROWSE', 'USAGE for discovery'),
                                      (107, 'Unity Catalog metastore administrator', 'Workspace administrator'),
                                      (146, 'FROM table_name', 'FROM live.table_name')]:
            if number == n:
                if current in q['displayStem']:
                    q['displayStem'] = q['displayStem'].replace(current, highlight(current, previous), 1)
                else:
                    for option in q['options']:
                        if option.get('correct') and current in option['displayHtml']:
                            option['displayHtml'] = option['displayHtml'].replace(current, highlight(current, previous), 1)
                updates.add((previous, current))
        q['updates'] = [{'old': old, 'new': new} for old, new in sorted(updates)]
        q['oos'] = False
        assert any(o.get('correct') for o in q['options'])
        retained.append(q)
        row.update({'section': q['sec'], 'updates': q['updates'], 'corrections': q['corrections']})
        audit_rows.append(row)
    dump = lambda name, data: (ROOT / 'downloads' / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    dump('syllabus-questions.json', retained)
    original = json.loads((ROOT / 'refined-questions.json').read_text(encoding='utf-8'))
    audit = {'guide': GUIDE, 'reviewDate': '2026-10-13', 'downloadedSourceQuestions': len(source),
             'downloadedKept': len(retained), 'downloadedExcluded': len(exclusions),
             'originalBankReviewed': len(original), 'originalBankKept': len(original),
             'policy': 'Human study-priority judgments against the listed objectives. Similar foundational concepts are kept even when product names changed; cosmetic updates are yellow. Behavior and answer corrections are disclosed separately. This is not an official Databricks excluded-question list.',
             'sectionCounts': dict(collections.Counter(q['sec'] for q in retained)), 'references': REFERENCES,
             'questions': audit_rows,
             'originalBankReview': [{'uid': q['uid'], 'status': 'kept', 'section': q['sec'], 'reason': OBJECTIVES[q['sec']]} for q in original]}
    dump('syllabus-refinement-audit.json', audit)
    md = ['# LeetQuiz May 2026 syllabus review', '', f'[Exam guide]({GUIDE})', '', audit['policy'], '',
          f"Downloaded bank: {len(source)} reviewed → {len(retained)} kept, {len(exclusions)} excluded. Original refined bank: {len(original)} reviewed and retained.", '',
          'This audit records the syllabus-filtering stage. The subsequent ExamTopics overlap audit in ../examtopics-deduplication-audit.md records additional removals from the active sets. The raw downloaded collection and all source versions remain in downloads.', '',
          '## Excluded downloaded questions', '', '| Source ID | Question | Reason |', '| --- | --- | --- |']
    for row in audit_rows:
        if row['status'] == 'excluded':
            md.append('| ' + row['uid'] + ' | ' + row['sourceStem'].replace('\n', ' ').replace('|', '\\|') + ' | ' + row['reason'] + ' |')
    md.extend(['', '## Retained questions and objective mapping', '', '| Source ID | Section | Objective |', '| --- | --- | --- |'])
    for row in audit_rows:
        if row['status'] == 'kept':
            md.append('| ' + row['uid'] + ' | ' + SECTIONS[row['section']] + ' | ' + row['reason'] + ' |')
    md.extend(['', '## Corrections beyond product renames', ''])
    for q in retained:
        if q['corrections']:
            md.append('### ' + q['id'])
            md.extend(['', *['- ' + note for note in q['corrections']], ''])
    md.extend(['## Yellow name updates', '', '| Old term | Updated term |', '| --- | --- |'])
    for old, new in RENAMES.items():
        md.append('| ' + old + ' | ' + new + ' |')
    (ROOT / 'downloads/syllabus-refinement-audit.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print(json.dumps({k: audit[k] for k in ['downloadedSourceQuestions', 'downloadedKept', 'downloadedExcluded', 'originalBankReviewed', 'sectionCounts']}, indent=2))


if __name__ == '__main__':
    build()
