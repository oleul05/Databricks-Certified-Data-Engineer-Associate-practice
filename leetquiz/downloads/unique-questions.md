# LeetQuiz — unique downloaded questions

197 unique questions from 623 downloaded entries (426 duplicate copies grouped). Reworded copies are grouped; all source versions remain in the JSON collection and original downloads. Source answers and explanations are preserved without fact-checking or syllabus filtering.

## 1. lqd-001

Which of the following describes a benefit of a data lakehouse that is unavailable in a traditional data warehouse?

A. A data lakehouse provides a relational system of data management.

B. A data lakehouse captures snapshots of data for version control purposes.

C. A data lakehouse couples storage and compute for complete control.

D. A data lakehouse utilizes proprietary storage formats for data.

E. A data lakehouse enables both batch and streaming analytics.

**Source answer: E**

The primary benefit highlighted is that a data lakehouse supports both batch and streaming analytics from the same storage system. Traditional data warehouses are typically designed for batch-oriented workloads and analytical queries on structured data, whereas a lakehouse (for example, Databricks Lakehouse with Delta Lake) unifies data warehousing and data lakes to support streaming ingest/processing and batch analytics together. While snapshot/versioning (time travel) is also a capability offered by some lakehouse implementations (Delta Lake provides time travel), the best single answer for a benefit broadly unavailable in traditional data warehouses is the unified support for both batch and streaming analytics. Other options are incorrect: A is false because traditional warehouses are relational; C is incorrect because lakehouses typically decouple compute and storage rather than coupling them; D is incorrect because lakehouses favor open storage formats (e.g., Parquet, Delta) rather than proprietary formats.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmgwah9s70001z8yllffk55r9/see?quizType=REAL_EXAM&page=75

## 2. lqd-002

A data architect is designing a data model that works for both video-based machine learning workloads and highly audited batch ETL/ELT workloads.

Which of the following describes how using a data lakehouse can help the data architect meet the needs of both workloads?

A. A data lakehouse requires very little data modeling.

B. A data lakehouse combines compute and storage for simple governance.

C. A data lakehouse provides autoscaling for compute clusters.

D. A data lakehouse stores unstructured data and is ACID-compliant.

E. A data lakehouse fully exists in the cloud.

**Source answer: D**

A lakehouse combines the best aspects of data lakes (supporting unstructured data like video, flexible storage formats) and data warehouses (ACID transactions, schema enforcement, and reliable governance), making it well-suited for both video-based machine learning and highly audited batch ETL/ELT workloads. Specifically, it can store large unstructured data such as video and still provide ACID transactions and schema enforcement for audited batch operations. Option A is incorrect because modeling is still important; option B is incorrect because lakehouses decouple compute and storage (not combine) for scalability and governance; option C is true of some platforms but not a defining characteristic addressing the requirement; option E is not universally true and is not relevant to the workload needs.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmgwamutc0001qc0fkmfsb826/see?quizType=REAL_EXAM&page=75

## 3. lqd-003

Which of the following describes a scenario in which a data engineer will want to use a Job cluster instead of an all-purpose cluster?

A. An ad-hoc analytics report needs to be developed while minimizing compute costs.

B. A data team needs to collaborate on the development of a machine learning model.

C. An automated workflow needs to be run every 30 minutes.

D. A Databricks SQL query needs to be scheduled for upward reporting.

E. A data engineer needs to manually investigate a production error.

**Source answer: C**

Job clusters are ephemeral clusters that are created and terminated for individual jobs or scheduled workflows. They are ideal for automated, recurring, production tasks because they provide isolation, reproducibility, and cost control (clusters run only for the duration of the job). An automated workflow that runs every 30 minutes is a classic use case for job clusters. In contrast, all-purpose clusters are intended for interactive, collaborative development and ad-hoc investigation (options A, B, and E). Databricks SQL scheduled queries typically use SQL warehouses/SQL endpoints rather than job clusters (option D). Therefore option C is the correct choice.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmgwapxtj0003qc0fhm864nud/see?quizType=REAL_EXAM&page=75

## 4. lqd-004

A data engineer has created a Delta table as part of a data pipeline. Downstream data analysts now need SELECT permission on the Delta table.

Assuming the data engineer is the Delta table owner, which part of the Databricks Lakehouse Platform can the data engineer use to grant the data analysts the appropriate access?

A. Repos

B. Jobs

C. Data Explorer

D. Databricks Filesystem

E. Dashboards

**Source answer: C**

Data Explorer provides the ability to manage and grant permissions on tables and other data objects in the Databricks workspace. As the owner of a Delta table, the data engineer can use Data Explorer to grant SELECT (and other) permissions to downstream analysts. Repos manages code, Jobs manages scheduled jobs, DBFS is a storage layer, and Dashboards provide visualizations but do not manage table permissions.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmgwavc1i0001wlaudnkprw8g/see?quizType=REAL_EXAM&page=75

## 5. lqd-005

A new data engineer has started at a company. The data engineer has recently been added to the company’s Databricks workspace as new.engineer@company.com. The data engineer needs to be able to query the table sales in the database retail. The new data engineer already has been granted USAGE on the database retail.

Which of the following commands can be used to grant the appropriate permissions to the new data engineer?

Context / important info:

Database: retail
Table: sales
User: new.engineer@company.com
The user already has: USAGE on DATABASE retail

You may assume standard Databricks SQL privileges syntax is used (GRANT ... ON TABLE ... TO ...).

Note: Do not include the answer options in this field.

A. GRANT USAGE ON TABLE sales TO new.engineer@company.com;

B. GRANT CREATE ON TABLE sales TO new.engineer@company.com;

C. GRANT SELECT ON TABLE sales TO new.engineer@company.com;

D. GRANT USAGE ON TABLE new.engineer@company.com TO sales;

E. GRANT SELECT ON TABLE new.engineer@company.com TO sales;

**Source answer: C**

To allow the data engineer to query (read) the table sales, you must grant the SELECT privilege on that table to the user. USAGE on the database allows the user to see and reference objects in the database but does not allow reading table data. CREATE on the table is not appropriate because it grants ability to create new objects, not read data. Options D and E are syntactically incorrect because the object and principal are reversed (GRANT ... ON TABLE <object> TO <principal>). The correct SQL command is: GRANT SELECT ON TABLE retail.sales TO new.engineer@company.com; If the username contains special characters (such as @), quoting or using the identity as a principal in Databricks may require backticks or using the user or group identifier as configured. This answer falls under "Data Governance" because it concerns privileges and access control.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmgwg2o1w00014uftxae6891h/see?quizType=REAL_EXAM&page=75

## 6. lqd-006

Question 7

Which of the following describes how Databricks Repos can help facilitate CI/CD workflows on the Databricks Lakehouse Platform?

A. Databricks Repos can facilitate the pull request, review, and approval process before merging branches

B. Databricks Repos can merge changes from a secondary Git branch into a main Git branch

C. Databricks Repos can be used to design, develop, and trigger Git automation pipelines

D. Databricks Repos can store the single-source-of-truth Git repository

E. Databricks Repos can commit or push code changes to trigger a CI/CD process

**Source answer: E**

✅ Correct Answer: E only

Databricks Repos helps facilitate CI/CD workflows by enabling developers to commit and push code changes from the Databricks workspace to a connected Git repository. These actions can trigger external CI/CD pipelines (such as GitHub Actions, Azure DevOps, or GitLab CI) that run tests, validations, or deployment processes. This makes E the only correct option.

❌ Why the other options are incorrect

A. Facilitate pull requests, reviews, and approvals
Pull requests and approvals are handled entirely by the Git provider, not Databricks Repos. Repos has no PR or review interface.

B. Merge branches
Branch merging is a Git operation performed in GitHub/GitLab/Azure DevOps, not in Databricks.

C. Design or develop CI/CD pipelines
Databricks Repos integrates with pipelines but does not define or manage them.

D. Store the source‑of‑truth repository
The authoritative repository always lives in the Git provider, not Databricks.

✅ Key takeaway for the exam

Databricks Repos synchronizes code with Git and can trigger CI/CD, but all governance and automation logic lives outside Databricks.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya33000601k0tu0s4n76/see?quizType=REAL_EXAM&page=76

## 7. lqd-007

Question 8

Which of the following statements describes Delta Lake?

A. Delta Lake is an open source analytics engine used for big data workloads.

B. Delta Lake is an open format storage layer that delivers reliability, security, and performance.

C. Delta Lake is an open source platform to help manage the complete machine learning lifecycle.

D. Delta Lake is an open source data storage format for distributed data.

E. Delta Lake is an open format storage layer that processes data.

**Source answer: B**

Explanation

Delta Lake is correctly described as "an open format storage layer that delivers reliability, security, and performance" (Option B). Here's why:

Delta Lake is an open-source storage layer that sits on top of data lakes and provides ACID transactions, scalable metadata handling, and unified streaming and batch data processing.

Option A is incorrect because this describes Apache Spark, not Delta Lake. Spark is the analytics engine, while Delta Lake is the storage layer.

Option C is incorrect because this describes MLflow, which is a separate platform for managing the machine learning lifecycle.

Option D is partially correct but incomplete. While Delta Lake is indeed an open-source data storage format for distributed data, the most accurate and comprehensive description is Option B, which emphasizes its role as a storage layer delivering reliability, security, and performance.

Option E is incorrect because Delta Lake doesn't process data - it stores data. Data processing is handled by engines like Apache Spark.

Delta Lake's key features include:

ACID transactions
Schema enforcement and evolution
Time travel (data versioning)
Unified batch and streaming
Data reliability and quality
Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya33000701k0p4hger6n/see?quizType=REAL_EXAM&page=76

## 8. lqd-008

Question 2

Which of the following locations hosts the driver and worker nodes of a Databricks-managed cluster?

A. Data plane

B. Control plane

C. Databricks Filesystem

D. JDBC data source

E. Databricks web application

**Source answer: A**

Explanation

In Databricks architecture, the Data plane (also known as the compute plane) is where the driver and worker nodes of a Databricks-managed cluster are hosted. Here's why:

Data Plane: This is the environment where your actual data processing occurs. It contains the compute resources (clusters) that run your Spark jobs, notebooks, and workflows. The driver node coordinates the execution, while worker nodes perform the actual data processing tasks.

Control Plane: This manages the workspace, user authentication, job scheduling, and cluster management, but does not host the actual compute nodes.

Databricks Filesystem (DBFS): This is a distributed file system for storing data, not for hosting cluster nodes.

JDBC data source: This is a connectivity method for accessing external databases, not a location for cluster nodes.

Databricks web application: This is the user interface for interacting with Databricks, not where cluster compute resources run.

The data plane is typically hosted in your cloud account (AWS, Azure, or GCP) and contains the actual virtual machines that form the Databricks clusters.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya32000101k006q5hlvt/see?quizType=REAL_EXAM&page=76

## 9. lqd-009

Question 6

Two junior data engineers are authoring separate parts of a single data pipeline notebook. They are working on separate Git branches so they can pair program on the same notebook simultaneously. A senior data engineer experienced in Databricks suggests there is a better alternative for this type of collaboration.

Which of the following supports the senior data engineer’s claim?

A. Databricks Notebooks support automatic change-tracking and versioning

B. Databricks Notebooks support real-time coauthoring on a single notebook

C. Databricks Notebooks support commenting and notification comments

D. Databricks Notebooks support the use of multiple languages in the same notebook

E. Databricks Notebooks support the creation of interactive data visualizations

**Source answer: B**

Explanation

The senior data engineer's claim likely relates to collaborative features that enable multiple team members to work together effectively on data engineering tasks.

Option B (Correct Answer): Databricks Notebooks support real-time coauthoring on a single notebook, which directly supports collaborative work by allowing multiple data engineers to work simultaneously on the same notebook, seeing each other's changes in real-time.

Why other options are less relevant:

Option A: Automatic change-tracking and versioning is more about individual development and audit trails rather than real-time collaboration
Option C: Commenting and notification comments support asynchronous communication but not real-time collaborative editing
Option D: Multi-language support is about technical capabilities, not collaboration features
Option E: Interactive visualizations are about data presentation and exploration, not collaborative development

Real-time coauthoring is specifically designed for collaborative scenarios where multiple team members need to work together on the same notebook simultaneously, making it the best support for the senior data engineer's claim about collaborative work.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya33000501k0zsmz6bu0/see?quizType=REAL_EXAM&page=76

## 10. lqd-010

Question 9

A data architect has determined that a table of the following format is necessary:

id	birthDate	avgRating
a1	1990-01-06	5.5
a2	1974-11-21	7.1
-	-	-

A. CREATE OR REPLACE TABLE table_name AS
SELECT
    id STRING,
    birthDate DATE,
    avgRating FLOAT
USING DELTA


B. CREATE OR REPLACE TABLE table_name (
    id STRING,
    birthDate DATE,
    avgRating FLOAT
)


C. CREATE TABLE IF NOT EXISTS table_name (
    id STRING,
    birthDate DATE,
    avgRating FLOAT
)


D. CREATE TABLE table_name AS
SELECT
    id STRING,
    birthDate DATE,
    avgRating FLOAT


E. CREATE OR REPLACE TABLE table_name WITH COLUMNS (
    id STRING,
    birthDate DATE,
    avgRating FLOAT
) USING DELTA


**Source answer: B**

Explanation

Let's analyze each option:

Option A: Uses CREATE OR REPLACE TABLE ... AS SELECT - This creates a table from a SELECT statement, but it's not creating an empty table. The SELECT statement would need to return data.

Option B: ✅ CORRECT - Uses CREATE OR REPLACE TABLE with explicit column definitions in parentheses. This creates an empty Delta table with the specified schema and will replace any existing table with the same name.

Option C: Uses CREATE TABLE IF NOT EXISTS - This only creates the table if it doesn't exist, so it doesn't meet the requirement of creating the table "regardless of whether a table already exists with this name."

Option D: Uses CREATE TABLE ... AS SELECT - Similar to option A, this creates a table from a SELECT statement, not an empty table.

Option E: Uses invalid syntax - WITH COLUMNS is not valid SQL syntax for table creation in Databricks.

The key requirements are:

Create an empty Delta table
Use SQL DDL commands
Work regardless of whether a table already exists

Option B satisfies all these requirements by using CREATE OR REPLACE TABLE with explicit column definitions, which creates an empty table with the specified schema and replaces any existing table.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya33000801k0q8pbwhcl/see?quizType=REAL_EXAM&page=77

## 11. lqd-011

Question 10

Which of the following SQL keywords can be used to append new rows to an existing Delta table?

A. UPDATE

B. COPY

C. INSERT INTO

D. DELETE

E. UNION

**Source answer: C**

Explanation

INSERT INTO is the correct SQL keyword for appending new rows to an existing Delta table. Here's why:

INSERT INTO - This command adds new rows to an existing table without affecting existing data. It's specifically designed for appending data.

Why the other options are incorrect:

UPDATE - Modifies existing rows in a table, doesn't add new rows
COPY - Not a standard SQL keyword for table operations; typically used for file operations
DELETE - Removes rows from a table, doesn't add new data
UNION - Combines results from multiple SELECT statements, but doesn't directly append to tables

In Databricks with Delta tables, INSERT INTO is the standard way to add new records while maintaining table integrity and supporting ACID transactions.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source: https://www.leetquiz.com/quiz/cmhaiya33000901k0k4px4zww/see?quizType=REAL_EXAM&page=77

## 12. lqd-012

Question 11

A data engineering team needs to query a Delta table to extract rows that all meet the same condition. However, the team has noticed that the query is running slowly. The team has already tuned the size of the data files. Upon investigating, the team has concluded that the rows meeting the condition are sparsely located throughout each of the data files.

Based on the scenario, which of the following optimization techniques could speed up the query?

A. Data skipping

B. Z-Ordering

C. Bin-packing

D. Write as a Parquet file

E. Tuning the file size

**Source answer: B**

Explanation

Z-Ordering is the correct optimization technique for this scenario because:

Problem Context: The query is slow even after tuning file sizes, and the qualifying rows are "sparsely located throughout each of the data files"
How Z-Ordering Helps: Z-Ordering (also known as multidimensional clustering) physically co-locates related data based on multiple columns, which improves data locality for filtering operations
Why Other Options Don't Work:
A. Data skipping: Already occurs automatically in Delta Lake but doesn't help when qualifying rows are scattered throughout files
C. Bin-packing: Helps with file size optimization (already done) but doesn't address data locality
D. Write as a Parquet file: Delta tables already use Parquet format internally, so this wouldn't help
E. Tuning the file size: The team has already done this optimization

Key Benefit: By applying Z-ORDER BY on the columns used in the filter condition, rows that meet the condition will be physically clustered together, reducing the number of files that need to be scanned and improving query performance significantly when filtering on those columns.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source: https://www.leetquiz.com/quiz/cmhaiya33000a01k0i6deef7a/see?quizType=REAL_EXAM&page=77

## 13. lqd-013

Question 12

A data engineer needs to create a database called customer360 at the location /customer/customer360. The data engineer is unsure if one of their colleagues has already created the database.

Which of the following commands should the data engineer run to complete this task?

A. CREATE DATABASE customer360 LOCATION '/customer/customer360';

B. CREATE DATABASE IF NOT EXISTS customer360;

C. CREATE DATABASE IF NOT EXISTS customer360 LOCATION '/customer/customer360';

D. CREATE DATABASE IF NOT EXISTS customer360 DELTA LOCATION '/customer/customer360';

E. CREATE DATABASE customer360 DELTA LOCATION '/customer/customer360';

**Source answer: C**

Explanation

The correct answer is C because:

The IF NOT EXISTS clause ensures that the database is only created if it doesn't already exist, which addresses the engineer's uncertainty about whether a colleague has already created it
The LOCATION '/customer/customer360' clause specifies the exact location where the database should be created
Option A would fail if the database already exists
Option B doesn't specify the location, so it would use the default location
Options D and E are incorrect because DELTA is not a valid keyword in the CREATE DATABASE syntax - Delta is a table format, not a database type

This command follows the proper Spark SQL syntax for creating a database with conditional existence checking and custom location specification.

Source copies: 2; distinct source versions: 2.

Source: https://www.leetquiz.com/quiz/cmhaiya33000b01k0pzz1mx4h/see?quizType=REAL_EXAM&page=77

## 14. lqd-014

Question 13 A junior data engineer needs to create a Spark SQL table my_table for which Spark manages both the data and the metadata. The metadata and data should also be stored in the Databricks Files system (DBFS).

Which of the following commands should a senior data engineer share with the junior data engineer to complete this task?

A. CREATE TABLE my_table (id STRING, value STRING) USING org.apache.spark.sql.parquet OPTIONS (PATH "storage-path");

B. CREATE MANAGED TABLE my_table (id STRING, value STRING) USING org.apache.spark.sql.parquet OPTIONS (PATH "storage-path");

C. CREATE MANAGED TABLE my_table (id STRING, value STRING);

D. CREATE TABLE my_table (id STRING, value STRING) USING DBFS;

E. CREATE TABLE my_table (id STRING, value STRING);

**Source answer: E**

Explanation

Option E (CREATE TABLE my_table (id STRING, value STRING);) is the correct choice because:

Managed Table: When you create a table using just CREATE TABLE without specifying a location in Databricks, it automatically creates a managed table where Spark manages both the data and metadata.

DBFS Storage: By default in Databricks, managed tables are stored in DBFS (Databricks File System) under the managed table location.

No External Path Needed: Unlike external tables that require explicit path specification, managed tables don't need a PATH option since Spark handles the storage location automatically.

Why other options are incorrect:

Option A: Uses USING org.apache.spark.sql.parquet with a custom path, which creates an external table where Spark only manages metadata, not the data.
Option B: CREATE MANAGED TABLE is not valid Spark SQL syntax - the correct syntax is simply CREATE TABLE for managed tables.
Option C: Same syntax error as Option B - CREATE MANAGED TABLE is not valid.
Option D: USING DBFS is not valid syntax - DBFS is the underlying storage system, not a table format.

In Databricks, the default behavior for CREATE TABLE without location specification creates a managed table stored in DBFS, meeting all the requirements: Spark manages both data and metadata, and storage is in DBFS.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000c01k0es4yhpdg/see?quizType=REAL_EXAM&page=77

## 15. lqd-015

Question 14 A data engineer wants to create a relational object by pulling data from two tables. The relational object must be used by other data engineers in other sessions. In order to save on storage costs, the data engineer wants to avoid copying and storing physical data.

Which of the following relational objects should the data engineer create?

A. View

B. Temporary view

C. Delta Table

D. Database

E. Spark SQL Table

**Source answer: A**

Explanation

The correct answer is A. View.

Here's why:

View: A view is a virtual table that represents the result of a SQL query. It doesn't store physical data but rather provides a logical representation of data from underlying tables. Views can be accessed by multiple users across different sessions, making them ideal for sharing relational objects without duplicating data.

Temporary view (B): Temporary views are session-scoped and cannot be accessed by other data engineers in different sessions, which violates the requirement.

Delta Table (C): Delta Tables store physical data on storage, which would incur storage costs and duplicate data, contrary to the requirement to avoid copying and storing physical data.

Database (D): A database is a container for tables and other objects, not a relational object that pulls data from tables.

Spark SQL Table (E): Like Delta Tables, Spark SQL Tables store physical data and would require storage space, defeating the cost-saving objective.

Views provide the perfect solution as they:

Create relational objects from multiple tables
Don't store physical data (no storage costs)
Are accessible across different sessions
Can be shared with other data engineers

Source copies: 3; distinct source versions: 3.

Source: https://www.leetquiz.com/quiz/cmhaiya34000d01k06t0ss4c5/see?quizType=REAL_EXAM&page=77

## 16. lqd-016

Question 15 A data engineering team has created a series of tables using Parquet data stored in an external system. The team is noticing that after appending new rows to the data in the external system, their queries within Databricks are not returning the new rows. They identify the caching of the previous data as the cause of this issue.

Which of the following approaches will ensure that the data returned by queries is always up-to-date?

A. Use the REFRESH TABLE command before querying the table

B. Use the CACHE TABLE command to cache the table

C. Use the UNCACHE TABLE command to remove the table from cache

D. Use the DESCRIBE TABLE command to view the table schema

E. Use the ANALYZE TABLE command to update table statistics

F. Use the MSCK REPAIR TABLE command to repair the table

**Source answer: A**

Explanation

When working with external tables in Databricks that reference Parquet data stored in external systems, caching can cause stale data to be returned even after the underlying data has been updated.

Correct Approach: REFRESH TABLE (Option A)

The REFRESH TABLE command explicitly invalidates the cached metadata and forces Databricks to reload the table metadata from the external storage
This ensures that subsequent queries will see the latest data including any newly appended rows
This is the most direct solution for this specific problem

Alternative Approach: UNCACHE TABLE (Option C)

The UNCACHE TABLE command removes the table from cache entirely
This would also solve the problem but is less efficient as it requires the table to be re-cached on subsequent queries
While it works, REFRESH TABLE is more appropriate for this scenario

Why other options don't work:

Option B (CACHE TABLE): This would make the problem worse by caching the stale data
Option D (DESCRIBE TABLE): Only shows schema information, doesn't refresh cached data
Option E (ANALYZE TABLE): Updates statistics for query optimization but doesn't refresh cached data
Option F (MSCK REPAIR TABLE): Used for Hive metastore partition discovery, not for refreshing cached data

Best Practice: For external tables that are frequently updated, consider using REFRESH TABLE before queries or configuring appropriate caching strategies to balance performance with data freshness requirements.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhaiya34000e01k0u6tthgu5/see?quizType=REAL_EXAM&page=77

## 17. lqd-017

Question 19

A data engineer wants to horizontally combine two tables as a part of a query. They want to use a shared column as a key column, and they only want the query result to contain rows whose value in the key column is present in both tables.

Which of the following SQL commands can they use to accomplish this task?

A. INNER JOIN

B. OUTER JOIN

C. LEFT JOIN

D. MERGE

E. UNION

**Source answer: A**

Explanation

An INNER JOIN is the correct SQL command for this scenario because:

INNER JOIN returns only the rows that have matching values in both tables based on the specified key column
It horizontally combines tables (side-by-side) using a shared column as the join key
It filters out rows where the key column value exists in only one table
Only rows with matching key values in both tables are included in the result

Why other options are incorrect:

OUTER JOIN (B): Returns all rows from both tables, including non-matching rows (fills with NULLs)
LEFT JOIN (C): Returns all rows from the left table and matching rows from the right table
MERGE (D): Used for upsert operations (update/insert), not for horizontal table combination in queries
UNION (E): Vertically combines tables (stacking rows), not horizontally combining columns

The key requirements in the question are:

Horizontal combination of tables
Using a shared column as key
Only rows with matching key values in both tables
INNER JOIN perfectly satisfies all these requirements.

Source copies: 2; distinct source versions: 2.

Source: https://www.leetquiz.com/quiz/cmhaiya34000i01k0uv55o60f/see?quizType=REAL_EXAM&page=78

## 18. lqd-018

Question 20

A junior data engineer has ingested a JSON file into a table raw_table with the following schema:

cart_id STRING,
items ARRAY<item_id:STRING>


The junior data engineer would like to unnest the items column in raw_table to result in a new table with the following schema:

cart_id STRING,
item_id STRING


Which of the following commands should the junior data engineer run to complete this task?

A. SELECT cart_id, filter(items) AS item_id FROM raw_table;

B. SELECT cart_id, flatten(items) AS item_id FROM raw_table;

C. SELECT cart_id, reduce(items) AS item_id FROM raw_table;

D. SELECT cart_id, explode(items) AS item_id FROM raw_table;

E. SELECT cart_id, slice(items) AS item_id FROM raw_table;

**Source answer: D**

Explanation

The correct answer is D because the EXPLODE function is specifically designed to unnest array columns in Spark SQL.

Why EXPLODE is the correct choice:
EXPLODE takes an array column and creates a new row for each element in the array
For a row with cart_id = "cart1" and items = ["itemA", "itemB", "itemC"], EXPLODE(items) would generate:
("cart1", "itemA")
("cart1", "itemB")
("cart1", "itemC")
This perfectly transforms the nested array structure into the desired flat table format
Why other options are incorrect:
A. FILTER: Used to filter elements from an array based on a condition, not to unnest arrays
B. FLATTEN: Used to flatten nested arrays (arrays of arrays), not to explode single arrays into rows
C. REDUCE: Used for aggregating array elements using a function, not for unnesting
E. SLICE: Used to extract a subset of elements from an array, not to create new rows
Key Concept:

EXPLODE is the standard Spark SQL function for converting array elements into individual rows, which is exactly what's needed for this data transformation task.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000j01k0jkdazzxe/see?quizType=REAL_EXAM&page=78

## 19. lqd-019

Question 21

A data engineer has ingested a JSON file into a table raw_table with the following schema:

transaction_id STRING,
payload ARRAY<customer_id:STRING, date:TIMESTAMP, store_id:STRING>


The data engineer wants to efficiently extract the date of each transaction into a table with the following schema:

transaction_id STRING,
date TIMESTAMP


Which of the following commands should the data engineer run to complete this task?

A. SELECT transaction_id, explode(payload) FROM raw_table;

B. SELECT transaction_id, payload.date FROM raw_table;

C. SELECT transaction_id, date FROM raw_table;

D. SELECT transaction_id, payload[date] FROM raw_table;

E. SELECT transaction_id, date from payload FROM raw_table;

**Source answer: B**

Explanation

The correct answer is B because:

The payload field is an array of structs with fields including date
In Spark SQL, when you have an array of structs, you can directly access struct fields using dot notation (payload.date)
This will return an array of dates for each transaction_id

Why the other options are incorrect:

Option A: explode(payload) would create multiple rows for each element in the array, which is not what's needed here. The requirement is to extract just the date field from the payload array.

Option C: date alone would not work because the date field is nested inside the payload array struct, not at the top level of the table schema.

Key Concept: When working with arrays of structs in Spark SQL, you can use dot notation to access struct fields directly, which returns an array of the specified field values. This is more efficient than using explode() when you only need to extract specific fields from the struct elements.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000k01k09oyh1v1l/see?quizType=REAL_EXAM&page=78

## 20. lqd-020

Question 22

A data analyst has provided a data engineering team with the following Spark SQL query:

SELECT district,
       avg(sales)
FROM store_sales_20220101
GROUP BY district;


The data analyst would like the data engineering team to run this query every day. The date at the end of the table name (20220101) should automatically be replaced with the current date each time the query is run.

Which of the following approaches could be used by the data engineering team to efficiently automate this process?

A. They could wrap the query using PySpark and use Python's string variable system to automatically update the table name.

B. They could manually replace the date within the table name with the current day's date.

C. They could request that the data analyst rewrites the query to be run less frequently.

D. They could replace the string-formatted date in the table with a timestamp-formatted date.

E. They could pass the table into PySpark and develop a robustly tested module on the existing query.

**Source answer: A**

Explanation

Option A is the correct answer because:

Automation: Using PySpark with Python's string formatting allows dynamic generation of table names based on the current date, enabling fully automated daily execution
Efficiency: This approach eliminates manual intervention and can be scheduled to run automatically
Scalability: The solution can be easily integrated into production pipelines and scheduled workflows

Other options are incorrect:

B: Manual replacement is inefficient and not scalable for daily automation
C: Changing the frequency doesn't solve the automation problem
D: Changing the date format doesn't address the dynamic table name requirement
E: While developing a tested module is good practice, it doesn't specifically address the dynamic table name automation

This approach aligns with Databricks best practices for production pipelines where dynamic table references are common in daily data processing workflows.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya35000l01k0dxlfvqfs/see?quizType=REAL_EXAM&page=78

## 21. lqd-021

Question 16

A table customerLocations exists with the following schema:

id STRING,
date STRING,
city STRING,
country STRING


A senior data engineer wants to create a new table from this table using the following command:

CREATE TABLE customersPerCountry AS
SELECT country,
       COUNT(*) AS customers
FROM customerLocations
GROUP BY country;


A junior data engineer asks why the schema is not being declared for the new table.

Which of the following responses explains why declaring the schema is not necessary?

A. CREATE TABLE AS SELECT statements adopt schema details from the source table and query.

B. CREATE TABLE AS SELECT statements infer the schema by scanning the data.

C. CREATE TABLE AS SELECTstatements result in tables where schemas are optional.

D. CREATE TABLE AS SELECTstatements assign all columns the type STRING.

E. CREATE TABLE AS SELECTstatements result in tables that do not support schemas.

**Source answer: A**

Explanation

In Databricks and Spark SQL, the CREATE TABLE AS SELECT (CTAS) statement automatically adopts the schema from the source table and the query results. Here's why:

Option A is correct: CTAS statements inherit the schema definition from the SELECT query's result set. The new table customersPerCountry will have:

country column with STRING type (inherited from the source table)
customers column with BIGINT type (result of COUNT(*))

Option B is incorrect: Schema inference by scanning data is not how CTAS works. The schema is determined at query compilation time, not by scanning actual data.

Option C is incorrect: Schemas are not optional in Databricks tables - all tables have defined schemas.

Option D is incorrect: CTAS does not default all columns to STRING type. It preserves the actual data types from the query result.

Option E is incorrect: All tables in Databricks support schemas and have defined schemas.

The CTAS statement automatically determines the schema based on:

Column names and types from the source table (country from customerLocations)
Aggregation functions and their result types (COUNT(*) returns BIGINT)
Expression results and their inferred types

This eliminates the need for manual schema declaration when creating tables from existing data.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000f01k06h3fo22d/see?quizType=REAL_EXAM&page=78

## 22. lqd-022

Question 17

A data engineer is overwriting data in a table by deleting the table and recreating the table. Another data engineer suggests that this is inefficient and the table should simply be overwritten instead. Which of the following reasons to overwrite the table instead of deleting and recreating the table is incorrect?

A. Overwriting a table is efficient because no files need to be deleted.

B. Overwriting a table results in a clean table history for logging and audit purposes.

C. Overwriting a table maintains the old version of the table for Time Travel.

D. Overwriting a table is an atomic operation and will not leave the table in an unfinished state.

E. Overwriting a table allows for concurrent queries to be completed while in progress.

**Source answer: B**

Explanation

Let's analyze each option:

A. Overwriting a table is efficient because no files need to be deleted. - INCORRECT When you overwrite a table in Databricks, the underlying files are indeed deleted and replaced with new files. This is not more efficient than deleting and recreating in terms of file operations. Both operations involve file deletion and creation.

B. Overwriting a table results in a clean table history for logging and audit purposes. - CORRECT Overwriting maintains a cleaner table history as it's a single operation in the transaction log, making audit trails more straightforward.

C. Overwriting a table maintains the old version of the table for Time Travel. - CORRECT Databricks Time Travel allows you to access previous versions of tables when using operations like OVERWRITE, preserving historical data.

D. Overwriting a table is an atomic operation and will not leave the table in an unfinished state. - CORRECT Overwrite operations are atomic, meaning they either complete fully or not at all, preventing partial table states.

E. Overwriting a table allows for concurrent queries to be completed while in progress. - CORRECT Overwrite operations in Databricks are designed to allow concurrent reads to continue using the previous version while the new version is being written.

Key Point: Option A is incorrect because overwriting a table does require deleting the existing files and replacing them with new files, making it no more efficient than delete-and-recreate in terms of file operations.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000g01k0rohlqb2c/see?quizType=REAL_EXAM&page=78

## 23. lqd-023

Question 18

Which of the following commands will return records from an existing Delta table my_table where duplicates have been removed?

A. DROP DUPLICATES FROM my_table;

B. SELECT * FROM my_table WHERE duplicate = False;

C. SELECT DISTINCT * FROM my_table;

D. MERGE INTO my_table a USING new_records b ON a.id = b.id WHEN NOT MATCHED THEN INSERT *;

E. MERGE INTO my_table a USING new_records b;

**Source answer: C**

Explanation

Let's analyze each option:

A. DROP DUPLICATES FROM my_table; - This is not a valid SQL command. There is no DROP DUPLICATES statement in standard SQL or Databricks SQL.

B. SELECT * FROM my_table WHERE duplicate = False; - This assumes there's a column named duplicate in the table, which is unlikely. Even if such a column existed, it wouldn't necessarily remove all duplicates from the result set.

C. SELECT DISTINCT * FROM my_table; - ✅ CORRECT - This command will return all records from my_table but will remove duplicate rows (rows where all column values are identical). The DISTINCT keyword ensures that only unique rows are returned.

D. MERGE INTO my_table a USING new_records b ON a.id = b.id WHEN NOT MATCHED THEN INSERT *; - This is a MERGE operation that inserts new records from new_records into my_table where they don't already exist. It doesn't remove duplicates from the existing table.

E. MERGE INTO my_table a USING new_records b; - This is an incomplete MERGE statement that will result in a syntax error because it's missing the required ON clause and WHEN conditions.

Therefore, only option C (SELECT DISTINCT * FROM my_table;) will return records from the existing Delta table with duplicates removed.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya34000h01k0mxnqax04/see?quizType=REAL_EXAM&page=78

## 24. lqd-024

Question 29 Which of the following data workloads will utilize a Bronze table as its source?

A. A job that aggregates cleaned data to create standard summary statistics

B. A job that queries aggregated data to publish key insights into a dashboard

C. A job that ingests raw data from a streaming source into the Lakehouse

D. A job that develops a feature set for a machine learning application

E. A job that enriches data by parsing its timestamps into a human-readable format

**Source answer: E**

Explanation

In the Databricks Lakehouse architecture, the Bronze table is the first layer where raw data is ingested and stored in its original format. The Bronze layer typically contains:

Raw, unprocessed data
Data in its original format (JSON, CSV, etc.)
Data that may need cleaning, transformation, or enrichment

Looking at the options:

Option A: Aggregates cleaned data - This would use Silver or Gold tables as source, not Bronze
Option B: Queries aggregated data - This would use Gold tables for reporting/dashboards
Option C: Ingests raw data - This is the process that CREATES Bronze tables, not uses them as source
Option D: Develops feature sets - This typically uses Silver tables with cleaned, structured data
Option E: Enriches data by parsing timestamps - This is exactly the type of transformation that would use Bronze tables as source, taking raw data and performing initial data quality/enrichment operations

Therefore, Option E is correct because parsing timestamps from raw data into human-readable format is a typical data enrichment operation that would use Bronze tables as the source.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya35000s01k01lst45v8/see?quizType=REAL_EXAM&page=79

## 25. lqd-025

Question 23

A data engineer has ingested data from an external source into a PySpark DataFrame raw_df. They need to briefly make this data available in SQL for a data analyst to perform a quality assurance check on the data.

Which of the following commands should the data engineer run to make this data available in SQL for only the remainder of the Spark session?

A. raw_df.createOrReplaceTempView("raw_df")

B. raw_df.createTable("raw_df")

C. raw_df.write.save("raw_df")

D. raw_df.saveAsTable("raw_df")

**Source answer: A**

Explanation

The correct answer is A because:

createOrReplaceTempView("raw_df") creates a temporary view that is only available for the duration of the current Spark session, which perfectly matches the requirement to "briefly make this data available in SQL for only the remainder of the Spark session"
Temporary views are automatically dropped when the Spark session ends
This allows data analysts to query the data using SQL syntax like SELECT * FROM raw_df

Why the other options are incorrect:

B createTable("raw_df"): This method doesn't exist in PySpark DataFrame API
C write.save("raw_df"): This saves the DataFrame to a file system location but doesn't make it available as a SQL table/view
D saveAsTable("raw_df"): This creates a permanent table in the Hive metastore that persists beyond the current Spark session, which contradicts the requirement for temporary availability

The key distinction is that temporary views (createOrReplaceTempView) are session-scoped while tables created with saveAsTable are persistent and survive session restarts.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya35000m01k0kcxzw5mm/see?quizType=REAL_EXAM&page=79

## 26. lqd-026

Question 24

A data engineer needs to dynamically create a table name string using three Python variables: region, store, and year. An example of a table name is below when region = "nyc", store = "100", and year = "2021":

nyc100_sales_2021

Which of the following commands should the data engineer use to construct the table name in Python?

A. " {region}+{store}+_sales_{year}"

B. f"{region}+{store}+_sales_{year}"

C. " {region}{store}_sales_{year}"

D. f"{region}{store}_sales_{year}"

E. {region}+{store}+_sales_"+{year}

**Source answer: D**

Explanation

To construct the table name nyc100_sales_2021 using Python variables region, store, and year, we need to use Python's f-string formatting correctly.

Let's analyze each option:

Option A: " {region}+{store}+_sales_{year}" - This is a regular string, not an f-string, so the variables won't be interpolated. It would literally output " {region}+{store}+_sales_{year}".

Option B: f"{region}+{store}+_sales_{year}" - This uses f-string formatting but includes + characters between variables, which would result in nyc+100+_sales_2021 instead of the desired nyc100_sales_2021.

Option C: " {region}{store}_sales_{year}" - This is a regular string without f-string prefix, so variables won't be interpolated.

Option D: f"{region}{store}_sales_{year}" - CORRECT: This uses f-string formatting correctly without any extra characters between variables. When region = "nyc", store = "100", and year = "2021", it will produce exactly nyc100_sales_2021.

Option E: {region}+{store}+_sales_"+{year} - This is invalid Python syntax that would cause a syntax error.

Key points:

F-strings (formatted string literals) are prefixed with f or F
Variables are placed directly inside curly braces {}
No concatenation operators like + are needed between variables in f-strings
The desired output format is {region}{store}_sales_{year} without any separators between region and store

Therefore, option D is the correct choice for dynamically creating the table name string in Python.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhaiya35000n01k0a498tm7f/see?quizType=REAL_EXAM&page=79

## 27. lqd-027

Question 25

A data engineer has developed a code block to perform a streaming read on a data source. The code block is below:

(spark
 .read
 .schema(schema)
 .format("cloudFiles")
 .option("cloudFiles.format", "json")
 .load(dataSource)
)


The code block is returning an error.

Which of the following changes should be made to the code block to configure the block to successfully perform a streaming read?

A. The .read line should be replaced with .readStream.

B. A new .stream line should be added after the .read line.

C. The .format("cloudFiles") line should be replaced with .format("stream").

D. A new .stream line should be added after the spark line.

E. A new .stream line should be added after the .load(dataSource) line.

**Source answer: A**

Explanation

In Apache Spark Structured Streaming, to perform a streaming read (as opposed to a batch read), you need to use .readStream instead of .read.

Key Points:

.read is used for batch processing
.readStream is used for streaming processing
The .format("cloudFiles") is correct for reading from cloud storage with Auto Loader
The .option("cloudFiles.format", "json") is correct for specifying JSON format
The .schema(schema) and .load(dataSource) are properly configured

Why other options are incorrect:

Option B: There is no .stream method in Spark's DataFrameReader API
Option C: .format("stream") is not a valid format - "cloudFiles" is the correct format for Auto Loader
Option D: There is no .stream method that can be added after spark
Option E: Adding .stream after .load(dataSource) would be syntactically incorrect

The corrected code should be:

(spark
 .readStream
 .schema(schema)
 .format("cloudFiles")
 .option("cloudFiles.format", "json")
 .load(dataSource)
)

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya35000o01k0f72ca8mg/see?quizType=REAL_EXAM&page=79

## 28. lqd-028

Question 26 A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.

The code block used by the data engineer is below:

(spark.table("sales")
  .withColumn("avg_price", col("sales") / col("units"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("complete")
  .______
  .table("new_sales"))


If the data engineer only wants the query to execute a single micro-batch to process all of the available data, which of the following lines of code should the data engineer use to fill in the blank?

A. trigger(once=True)

B. trigger(continuous="once")

C. processingTime("once")

D. trigger(processingTime="once")

E. processingTime(1)

**Source answer: A**

Explanation

In Apache Spark Structured Streaming, when you want to execute a streaming query that processes all available data in a single micro-batch and then stops, you should use the trigger(once=True) option.

Why Option A is correct:
trigger(once=True) is specifically designed for this use case
It processes all available data in one batch and then terminates the streaming query
This is commonly used for batch-like processing using the streaming framework
Why other options are incorrect:
B. trigger(continuous="once"): This syntax is incorrect. Continuous processing mode doesn't use "once" as a parameter
C. processingTime("once"): This is invalid syntax. processingTime expects a time interval string like "1 second" or "5 minutes"
D. trigger(processingTime="once"): Invalid syntax - processingTime trigger expects a time interval, not the string "once"
E. processingTime(1): This would trigger the query every 1 millisecond, creating continuous micro-batches, not a single batch
Key Points:
trigger(once=True) is the proper way to execute a one-time batch processing using Structured Streaming
This is useful for scenarios where you want to process all available data at once and then stop
The query will process all data that has accumulated since the last trigger and then terminate

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhaiya35000p01k0sfyf3c1z/see?quizType=REAL_EXAM&page=79

## 29. lqd-029

Question 27 A data engineer is designing a data pipeline. The source system generates files in a shared directory that is also used by other processes. As a result, the files should be kept as is and will accumulate in the directory. The data engineer needs to identify which files are new since the previous run in the pipeline, and set up the pipeline to only ingest those new files with each run.

Which of the following tools can the data engineer use to solve this problem?

A. Databricks SQL

B. Delta Lake

C. Unity Catalog

D. Data Explorer

E. Auto Loader

**Source answer: E**

Explanation

Auto Loader is specifically designed to solve this exact problem. Here's why:

Auto Loader Features:
Incremental File Processing: Auto Loader automatically tracks which files have been processed and only loads new files in subsequent runs
File Tracking: It maintains state about processed files using checkpointing
Efficient Discovery: Uses efficient file listing and directory scanning to identify new files
Exactly-Once Processing: Ensures files are processed only once even if the pipeline restarts
Why Other Options Don't Fit:
A. Databricks SQL: This is a query service, not a file ingestion tool
B. Delta Lake: While Delta Lake handles incremental data processing, it doesn't inherently solve the file discovery problem
C. Unity Catalog: This is for data governance and cataloging, not file ingestion
D. Data Explorer: This is for exploring and visualizing data, not for incremental file processing
Auto Loader Implementation:
# Example Auto Loader code for incremental file processing
df = spark.readStream.format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.includeExistingFiles", "false") \
    .load("path/to/shared/directory")


Auto Loader's ability to track processed files and only ingest new ones makes it the perfect solution for this scenario where files accumulate in a shared directory and need to be processed incrementally.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmhaiya35000q01k0bvwkjs6d/see?quizType=REAL_EXAM&page=79

## 30. lqd-030

Question 28 A data engineering team is in the process of converting their existing data pipeline to utilize Auto Loader for incremental processing in the ingestion of JSON files. One data engineer comes across the following code block in the Auto Loader documentation:

(streaming_df = spark.readStream.format("cloudFiles")
 .option("cloudFiles.format", "json")
 .option("cloudFiles.schemaLocation", schemaLocation)
 .load(sourcePath))


Assuming that schemaLocation and sourcePath have been set correctly, which of the following changes does the data engineer need to make to convert this code block to use Auto Loader to ingest the data?

A. The data engineer needs to change the format("cloudFiles") line to format("autoLoader").

B. There is no change required. Databricks automatically uses Auto Loader for streaming reads.

C. There is no change required. The inclusion of format("cloudFiles") enables the use of Auto Loader.

D. The data engineer needs to add the .autoLoader line before the .load(sourcePath) line.

E. There is no change required. The data engineer needs to ask their administrator to turn on Auto Loader.

**Source answer: C**

Explanation

The correct answer is C because the code block shown is already using the proper Auto Loader syntax.

Key Points:

format("cloudFiles") is the correct format specification for Auto Loader in Databricks
cloudFiles.format option specifies the file format (JSON in this case)
cloudFiles.schemaLocation option is used for schema evolution in Auto Loader
The code already follows the standard Auto Loader pattern for streaming ingestion

Why other options are incorrect:

A: Auto Loader uses "cloudFiles" format, not "autoLoader"
B: Auto Loader is not automatically used for all streaming reads - it requires specific configuration
D: There is no .autoLoader method in the Auto Loader API
E: Auto Loader doesn't require administrator intervention to enable - it's available by default

Auto Loader Syntax:

spark.readStream.format("cloudFiles")
  .option("cloudFiles.format", "<file-format>")
  .option("cloudFiles.schemaLocation", "<schema-location>")
  .load("<source-path>")


The provided code is already correctly configured for Auto Loader incremental processing.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya35000r01k057reo4gf/see?quizType=REAL_EXAM&page=79

## 31. lqd-031

Question 30 Which of the following data workloads will utilize a Silver table as its source?

A. A workload that curates data for use in a dashboard

B. A workload that ingests raw data from a streaming source

C. A workload that enriches data by joining multiple data sources

D. A workload that applies business logic to create aggregated metrics

E. A workload that cleanses data by removing malformed records

**Source answer: D**

Explanation

In the Databricks Lakehouse medallion architecture:

Bronze tables contain raw, unprocessed data from source systems
Silver tables contain cleaned, validated, and enriched data ready for business use
Gold tables contain aggregated, summarized data for reporting and analytics

A Silver table serves as the source for workloads that:

Curate data for dashboards and BI tools
Prepare data for downstream analytics
Provide clean, reliable data for business applications

Option A is incorrect because this is a data cleaning and preparation task. It typically happens when creating a Silver table. The source for this job would be a Bronze table.

Option B is incorrect because ingesting raw data from streaming sources would use Bronze tables as the source.

Option C is incorrect because joining multiple data sources typically happens during the Silver layer processing, not using Silver as a source.

Option D is correct because D. This is the definitive process for creating a Gold table. The source for this aggregation job is the cleaned, reliable data in the Silver table.

Option E is incorrect because cleansing data by removing malformed records is typically done during the Bronze to Silver transformation process.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhaiya36000t01k0ije79yo7/see?quizType=REAL_EXAM&page=80

## 32. lqd-032

Question 31

Which of the following Structured Streaming queries is performing a hop from a Bronze table to a Silver table?

A. (spark.table("sales")
  .groupBy("store")
  .agg(sum("sales"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("complete")
  .table("aggregatedSales"))


B. (spark.table("sales")
  .agg(sum("sales"), sum("units"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("complete")
  .table("aggregatedSales"))


C. (spark.table("sales")
  .withColumn("avgPrice", col("sales") / col("units"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("cleanedSales"))


D. (spark.readStream.load(rawSalesLocation)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("uncleanedSales"))


E. (spark.read.load(rawSalesLocation)
  .writeStream


**Source answer: C**

Explanation

In the Databricks medallion architecture:

Bronze tables contain raw, unprocessed data
Silver tables contain cleaned, validated, and enriched data
Gold tables contain aggregated data for business intelligence

Analysis of each option:

Option A & B: These perform aggregations (groupBy and agg) which are typically associated with creating Gold tables from Silver tables, not Bronze to Silver transformations.

Option C: This query performs data cleaning/enrichment by calculating avgPrice using withColumn(col("sales") / col("units")) and writes to a table named cleanedSales. This represents the typical Bronze to Silver transformation where raw data is cleaned and enriched.

Option D: This writes to a table named uncleanedSales, indicating it's still in the Bronze stage (raw data).

Option E: This is an incomplete query and doesn't represent a valid transformation.

The key indicators that Option C represents a Bronze to Silver hop are:

Data transformation/cleaning (withColumn operation)
Output table named cleanedSales (suggesting cleaned data)
append output mode (appropriate for incremental data processing)

Therefore, Option C correctly represents moving from Bronze (raw data) to Silver (cleaned, processed data).

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36000u01k0mz1dvpvu/see?quizType=REAL_EXAM&page=80

## 33. lqd-033

Question 32

Which of the following benefits does Delta Live Tables provide for ELT pipelines over standard data pipelines that utilize Spark and Delta Lake on Databricks?

A. The ability to declare and maintain data table dependencies

B. The ability to write pipelines in Python and/or SQL

C. The ability to access previous versions of data tables

D. The ability to automatically scale compute resources

E. The ability to perform batch and streaming queries

**Source answer: A**

Explanation

Delta Live Tables (DLT) provides several advantages over standard Spark and Delta Lake pipelines, but the key distinguishing benefit is the ability to declare and maintain data table dependencies (Option A).

Let's analyze each option:

A. The ability to declare and maintain data table dependencies ✅ - This is a core DLT feature. DLT automatically manages dependencies between tables in your pipeline, ensuring proper execution order and handling failures gracefully.

B. The ability to write pipelines in Python and/or SQL ❌ - Standard Spark pipelines on Databricks can also be written in Python and SQL, so this is not a unique DLT benefit.

C. The ability to access previous versions of data tables ❌ - This is a Delta Lake feature (time travel) that's available in standard Delta Lake pipelines, not specific to DLT.

D. The ability to automatically scale compute resources ❌ - Databricks provides autoscaling for standard Spark clusters as well, so this is not unique to DLT.

E. The ability to perform batch and streaming queries ❌ - Standard Spark Structured Streaming supports both batch and streaming processing, so this capability exists outside DLT.

Key DLT advantages over standard pipelines:

Declarative pipeline definition - You declare what you want, not how to compute it
Automatic dependency management - DLT figures out execution order
Data quality monitoring - Built-in expectations and data quality constraints
Simplified operations - Automatic retries, error handling, and pipeline recovery
Unified batch and streaming - Single code path for both processing modes

The dependency management capability (Option A) is particularly valuable as it eliminates the need for manual orchestration and ensures data consistency across the pipeline.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36000v01k0ktegs670/see?quizType=REAL_EXAM&page=80

## 34. lqd-034

Question 33

A data engineer has three notebooks in an ELT pipeline. The notebooks need to be executed in a specific order for the pipeline to complete successfully. The data engineer would like to use Delta Live Tables to manage this process.

Which of the following steps must the data engineer take as part of implementing this pipeline using Delta Live Tables?

A. They need to create a Delta Live Tables pipeline from the Data page.

B. They need to create a Delta Live Tables pipeline from the Jobs page.

C. They need to create a Delta Live tables pipeline from the Compute page.

D. They need to refactor their notebook to use Python and the dlt library.

E. They need to refactor their notebook to use SQL and CREATE LIVE TABLE keyword.

**Source answer: B**

Explanation

Delta Live Tables (DLT) pipelines are created and managed from the Jobs page in Databricks, not from the Data or Compute pages. Here's why:

Option B is correct: The Jobs page is where you create and manage all types of jobs in Databricks, including Delta Live Tables pipelines. This is the primary interface for scheduling and orchestrating data processing workflows.

Option A is incorrect: The Data page is primarily for exploring and managing datasets, tables, and databases, not for creating pipelines.

Option C is incorrect: The Compute page is for managing compute clusters and SQL warehouses, not for creating pipelines.

Option D and E are incorrect: While DLT supports both Python (using the dlt library) and SQL (using CREATE LIVE TABLE statements), refactoring notebooks is not mandatory for using DLT. You can reference existing notebooks in a DLT pipeline without refactoring them, as long as they contain valid DLT code. The key requirement is creating the pipeline from the Jobs page.

Key Point: The essential step for implementing a DLT pipeline is creating it from the Jobs page, where you can specify the notebooks to run, their execution order, and other pipeline configurations.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36000w01k075svjphw/see?quizType=REAL_EXAM&page=80

## 35. lqd-035

Question 34

Which of the following describes the change the colleague needs to make to the query?

A data engineer has written the following query:

SELECT *
FROM json.`/path/to/json/file.json`;
```

The data engineer asks a colleague for help to convert this query for use in a Delta Live
Tables (DLT) pipeline. The query should create the first table in the DLT pipeline.
Which of the following describes the change the colleague needs to make to the query?


A. They need to add a COMMENT line at the beginning of the query.

B. They need to add a CREATE LIVE TABLE table_name AS line at the beginning of the query.

C. They need to add a live. prefix prior to json. in the FROM line.

D. They need to add a CREATE DELTA LIVE TABLE table_name AS line at the beginning of the query.

E. They need to add the cloud_files(...) wrapper to the JSON file path.

**Source answer: B**

The correct answer is B. They need to add a CREATE LIVE TABLE table_name AS line at the beginning of the query.

Here's the detailed explanation:

In Delta Live Tables (DLT), you define tables using SQL by prefixing standard SQL queries with DLT-specific declarations. The basic syntax for creating a table is:

CREATE LIVE TABLE table_name
AS
SELECT * FROM json.`/path/to/json/file.json`;


Let's examine why the other options are incorrect:

A. They need to add a COMMENT line at the beginning of the query. - While comments are good practice, they are not required for the query to function in DLT.
C. They need to add a live. prefix prior to json. in the FROM line. - The live. prefix is used to reference other tables within the same DLT pipeline, not to read external data sources.
D. They need to add a CREATE DELTA LIVE TABLE table_name AS line at the beginning of the query. - The correct keyword is CREATE LIVE TABLE, not CREATE DELTA LIVE TABLE.
E. They need to add the cloud_files(...) wrapper to the JSON file path. - While cloud_files is an excellent function for autoloader-style ingestion and is commonly used in DLT pipelines for incremental processing, it's not strictly required to convert this specific query. The original query using the json. data source will work in DLT when wrapped with the proper CREATE LIVE TABLE syntax. The cloud_files wrapper would be an enhancement for better pipeline performance and incremental processing, but the fundamental change needed is the DLT table creation syntax.

The core requirement to convert any standard Databricks SQL query for use in a DLT pipeline is to add the appropriate DLT declaration (CREATE LIVE TABLE..., CREATE LIVE VIEW..., etc.) at the beginning.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36000x01k09ol7e4t9/see?quizType=REAL_EXAM&page=80

## 36. lqd-036

Question 35 \

A dataset has been defined using Delta Live Tables and includes an expectations clause:
CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') \

What is the expected behavior when a batch of data containing data that violates these constraints is processed?

A. Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.

B. Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.

C. Records that violate the expectation cause the job to fail.

D. Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.

E. Records that violate the expectation are dropped from the target dataset and loaded into a quarantine table.

**Source answer: A**

The correct answer is A. Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.

Here's the accurate explanation:

In Delta Live Tables, when you use a basic CONSTRAINT ... EXPECT clause without any additional violation handling, the default behavior is:

Retention: Records that violate the expectation are still added to the target dataset
Logging: The violations are recorded as metrics in the event log for monitoring
Pipeline Continuation: The pipeline continues processing without failing or dropping records

This represents DLT's default "track only" behavior for data quality constraints.

The other options represent different behaviors that require explicit configuration:

B (dropping records): Would require EXPECT ... ON VIOLATION DROP ROW
C (failing the job): Would require EXPECT ... ON VIOLATION FAIL UPDATE
E (quarantine table): Would require custom logic with multiple output targets

Thank you for the correction. The basic EXPECT clause without additional violation handling simply monitors data quality without altering the data flow, making option A the correct answer.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhaiya36000y01k0f1jursh0/see?quizType=REAL_EXAM&page=80

## 37. lqd-037

Question 36 A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE.

The table is configured to run in Development mode using the Triggered Pipeline Mode.

Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline?

A. All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.

B. All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will be deployed for the update and terminated when the
pipeline is stopped.

C. All datasets will be updated at set intervals until the pipeline is shut down. The
compute resources will persist after the pipeline is stopped to allow for additional
testing.

D. All datasets will be updated once and the pipeline will shut down. The compute
resources will persist to allow for additional testing

E. All datasets will be updated continuously and the pipeline will not shut down. The
compute resources will persist with the pipeline

**Source answer: D**

Let’s break this down carefully.

Key facts from the question:

Pipeline mode: Development mode
Trigger type: Triggered Pipeline Mode
Table types:
Two datasets: STREAMING LIVE TABLE
Three datasets: LIVE TABLE (against Delta Lake sources)
Previously unprocessed data exists.
All definitions are valid.
1. Understanding Development mode in DLT

In Development mode:

The pipeline performs one update of the DAG and then shuts down.
Compute resources are kept alive for a period (default 30 minutes or so) to allow for iterative development — meaning you can start it again quickly without cluster startup time.
2. Understanding Triggered vs. Continuous in this context
Triggered = Run once (in Production mode, that means process available data then stop; in Dev mode, same but compute persists for developer convenience).
Continuous = Run forever (only available in Production mode).

Since this is Development mode + Triggered, the behavior is:

Process all available data through the DAG once.
Pipeline run stops (status: Completed).
Compute does not terminate immediately — it stays available for the developer to run again without waiting for cluster startup.
3. Impact of mixed streaming and batch tables
STREAMING LIVE TABLE: In Triggered mode, these will process only new data since last run (or all data if first run).
LIVE TABLE (batch): In Triggered mode, these will run once.

All datasets are updated once in a single DAG execution, then the pipeline stops.

4. Matching to options
A: Shuts down + compute terminated — ❌ Incorrect, because in Dev mode compute persists.
B: Updates at intervals until shut down — ❌ That’s Continuous mode, not Triggered.
C: Updates at intervals + compute persists after stop — ❌ Again, intervals imply Continuous.
D: Updates once, pipeline shuts down, compute persists — ✅ Matches Dev + Triggered.
E: Updates continuously, doesn’t shut down — ❌ That’s Continuous in Production mode.

Correct answer: D

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36000z01k0ulfpmnzf/see?quizType=REAL_EXAM&page=80

## 38. lqd-038

Question 42

A data engineering team has been using a Databricks SQL query to monitor the performance of an ELT job. The ELT job is triggered by a specific number of input records being ready to process. The Databricks SQL query returns the number of minutes since the job's most recent runtime.

Which of the following approaches can enable the data engineering team to be notified if the ELT job has not been run in an hour?

A. They can set up an Alert for the accompanying dashboard to notify them if the returned value is greater than 60.

B. They can set up an Alert for the query to notify when the ELT job fails.

C. They can set up an Alert for the accompanying dashboard to notify when it has not refreshed in 60 minutes.

D. They can set up an Alert for the query to notify them if the returned value is greater than 60.

E. This type of alerting is not possible in Databricks.

**Source answer: D**

Explanation

Option D is the correct answer because:

The Databricks SQL query returns the number of minutes since the job's most recent runtime
Setting up an alert on the query itself allows monitoring the query results directly
When the returned value (minutes since last run) is greater than 60, it means the job hasn't run in over an hour
Query alerts in Databricks can be configured to trigger when query results meet specific conditions

Why other options are incorrect:

Option A: Dashboard alerts monitor dashboard refresh status, not the actual query results
Option B: This would only notify on job failures, not on the job not running at all
Option C: Dashboard refresh alerts don't monitor the actual job runtime data
Option E: This type of alerting is absolutely possible in Databricks through query alerts

This approach provides proactive monitoring to ensure the ELT job is running as expected based on the input record trigger condition.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya37001501k0ql0g56yq/see?quizType=REAL_EXAM&page=81

## 39. lqd-039

Question 37

A data engineer has a Job with multiple tasks that runs nightly. One of the tasks unexpectedly fails during 10 percent of the runs.

Which of the following actions can the data engineer perform to ensure the Job completes each night while minimizing compute costs?

A. They can institute a retry policy for the entire Job

B. They can observe the task as it runs to try and determine why it is failing

C. They can set up the Job to run multiple times ensuring that at least one will complete

D. They can institute a retry policy for the task that periodically fails

E. They can utilize a Jobs cluster for each of the tasks in the Job

**Source answer: D**

Explanation

Option D is the correct answer because:

Targeted retry policy: Instituting a retry policy specifically for the failing task (which only fails 10% of the time) is the most cost-effective solution. This allows the task to automatically retry when it fails, without affecting other tasks that are running successfully.

Cost minimization: Since the task only fails 10% of the time, retrying it a few times when it fails is much more cost-effective than running the entire job multiple times or using more expensive compute resources.

Job completion guarantee: With appropriate retry settings, the task will eventually succeed, ensuring the entire job completes each night.

Why other options are less optimal:

Option A: Retrying the entire job is inefficient and costly, as it would rerun all tasks (including successful ones) when only one task fails.

Option B: While observing the task is good for troubleshooting, it doesn't solve the immediate problem of ensuring job completion each night.

Option C: Running the job multiple times is wasteful and expensive, as it would consume compute resources for duplicate runs.

Option E: Using separate Jobs clusters for each task increases complexity and costs without solving the underlying reliability issue.

The retry policy approach directly addresses the intermittent failure while maintaining cost efficiency.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36001001k0b2g20z5x/see?quizType=REAL_EXAM&page=81

## 40. lqd-040

Question 38

A data engineer has set up two Jobs that each run nightly. The first Job starts at 12:00 AM, and it usually completes in about 20 minutes. The second Job depends on the first Job, and it starts at 12:30 AM. Sometimes, the second Job fails when the first Job does not complete by 12:30 AM.

Which of the following approaches can the data engineer use to avoid this problem?

A. They can utilize multiple tasks in a single job with a linear dependency

B. They can use cluster pools to help the Jobs run more efficiently

C. They can set up a retry policy on the first Job to help it run more quickly

D. They can limit the size of the output in the second Job so that it will not fail as easily

E. They can set up the data to stream from the first Job to the second Job

**Source answer: A**

Explanation

The correct answer is A because:

Multiple tasks in a single job with linear dependency ensures that the second task only starts after the first task successfully completes. This eliminates the timing issue where the second job starts before the first job finishes.

Option B (cluster pools) might improve efficiency but doesn't solve the dependency timing problem.

Option C (retry policy) might help with transient failures but doesn't guarantee the first job completes before the second job starts.

Option D (limit output size) addresses potential performance issues but doesn't solve the fundamental dependency timing problem.

Option E (streaming data) is not appropriate for batch jobs and doesn't address the job dependency issue.

By using multiple tasks within a single job with linear dependencies, the data engineer can ensure proper execution order without relying on fixed start times that may cause race conditions.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36001101k0kpdlt24m/see?quizType=REAL_EXAM&page=81

## 41. lqd-041

Question 39

A data engineer has set up a notebook to automatically process using a Job. The data engineer's manager wants to version control the schedule due to its complexity.

Which of the following approaches can the data engineer use to obtain a version-controllable configuration of the Job's schedule?

A. They can link the Job to notebooks that are a part of a Databricks Repo.

B. They can submit the Job once on a Job cluster.

C. They can download the JSON description of the Job from the Job's page.

D. They can submit the Job once on an all-purpose cluster.

E. They can download the XML description of the Job from the Job's page.

**Source answer: C**

Explanation

The correct answer is C because:

Option C: Downloading the JSON description of the Job from the Job's page provides a complete, machine-readable configuration file that includes the schedule settings. This JSON file can be stored in a version control system (like Git) and tracked over time, allowing for proper version control of the Job's schedule configuration.
Why other options are incorrect:

Option A: Linking the Job to notebooks in a Databricks Repo only version controls the notebook code, not the Job's schedule configuration itself.

Option B: Submitting the Job once on a Job cluster doesn't provide a version-controllable configuration file for the schedule.

Option D: Submitting the Job once on an all-purpose cluster similarly doesn't provide a configuration file for version control.

Option E: Databricks Jobs use JSON format for configuration, not XML. Downloading XML description is not a valid option.

Best Practice:

The JSON description contains all Job settings including the schedule, which can be committed to version control, enabling tracking of changes, rollback capabilities, and collaborative development of Job configurations.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya36001201k04o45tw5t/see?quizType=REAL_EXAM&page=81

## 42. lqd-042

Question 40

A data analyst has noticed that their Databricks SQL queries are running too slowly. They claim that this issue is affecting all of their sequentially run queries. They ask the data engineering team for help. The data engineering team notices that each of the queries uses the same SQL endpoint, but the SQL endpoint is not used by any other user.

Which of the following approaches can the data engineering team use to improve the latency of the data analyst's queries?

A. They can turn on the Serverless feature for the SQL endpoint.

B. They can increase the maximum bound of the SQL endpoint's scaling range.

C. They can increase the cluster size of the SQL endpoint.

D. They can turn on the Auto Stop feature for the SQL endpoint.

E. They can turn on the Serverless feature for the SQL endpoint and change the Spot Instance Policy to "Reliability Optimized."

**Source answer: C**

Correct Answer: C — Increase the cluster size of the SQL endpoint

Why C is Correct:

Sequential queries use one worker at a time
Larger cluster size = more power per worker (CPU, memory)
Directly improves performance for each individual query

Why B is Incorrect:

Scaling range controls number of workers for handling concurrent queries
Since queries run sequentially (not concurrently), more workers won't help
Would only help if multiple users were querying simultaneously

Why Others Are Wrong:

A & E (Serverless): Improves startup time/manageability, not query speed
D (Auto Stop): Cost-saving feature, doesn't affect performance

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya37001301k0nzz60bba/see?quizType=REAL_EXAM&page=81

## 43. lqd-043

Question 41

An engineering manager uses a Databricks SQL query to monitor their team's progress on fixes related to customer-reported bugs. The manager checks the results of the query every day, but they are manually rerunning the query each day and waiting for the results.

Which of the following approaches can the manager use to ensure the results of the query are updated each day?

A. They can schedule the query to run every 1 day from the Jobs UI.

B. They can schedule the query to refresh every 1 day from the query’s page in Databricks SQL.

C. They can schedule the query to run every 12 hours from the Jobs UI.

D. They can schedule the query to refresh every 1 day from the SQL endpoint’s page in Databricks SQL.

E. They can schedule the query to refresh every 12 hours from the SQL endpoint’s page
in Databricks SQL.

**Source answer: B**

In Databricks SQL, queries can be scheduled to refresh automatically from the query’s page. This feature ensures that the results are updated at a chosen frequency (e.g., daily), without requiring the user to manually rerun the query.

Let’s break down the options:

A: Schedule from Jobs UI (every 1 day)
Jobs UI is typically used for workflows, notebooks, or pipelines—not for refreshing SQL queries directly. This is not the most appropriate solution.

B: Schedule the query to refresh every 1 day from the query’s page in Databricks SQL This is the correct approach. Databricks SQL allows you to set a refresh schedule directly on the query’s page, ensuring results are updated daily.

C: Schedule the query to run every 12 hours from the Jobs UI
Same issue as option A—Jobs UI is not the right place for SQL query refresh scheduling.

D: Schedule the query to refresh every 1 day from the SQL endpoint’s page
SQL endpoints manage compute resources, not query refresh schedules. Incorrect.

E: Schedule the query to refresh every 12 hours from the SQL endpoint’s page
Same as D—endpoints don’t handle query refresh scheduling.

Correct Answer:

B: They can schedule the query to refresh every 1 day from the query’s page in Databricks SQL.

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya37001401k02v1mud54/see?quizType=REAL_EXAM&page=81

## 44. lqd-044

A data engineer has created a new database using the following command: CREATE DATABASE IF NOT EXISTS customer360;

In which of the following locations will the customer360 database be located?

A. dbfs:/user/hive/database/customer360

B. dbfs:/user/hive/warehouse

C. dbfs:/user/hive/customer360

D. More information is needed to determine the correct response

E. dbfs:/user/hive/database

**Source answer: B**

Explanation

In Databricks, when you create a database using the CREATE DATABASE command without specifying a location, the database is created in the default Hive warehouse location. The default location for Hive databases in Databricks is:

dbfs:/user/hive/warehouse/

When you create a database without specifying a custom location, Databricks creates a subdirectory for that database within the warehouse directory. For the customer360 database, the actual directory would be:

dbfs:/user/hive/warehouse/customer360.db

Let's analyze why the other options are incorrect:

Option A (dbfs:/user/hive/database/customer360): This is not the standard Databricks Hive warehouse structure.
Option C (dbfs:/user/hive/customer360): This path doesn't follow the standard warehouse directory structure.
Option D (More information is needed): This is incorrect because we have enough information - databases created without a specified location go to the default warehouse.
Option E (dbfs:/user/hive/database): This is not the standard warehouse location.

Key Points:

The default Hive warehouse location in Databricks is dbfs:/user/hive/warehouse
Databases are created as subdirectories with .db extension within this location
You can specify a custom location using: CREATE DATABASE customer360 LOCATION 'dbfs:/custom/path'
Without a custom location, it defaults to the warehouse directory
Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o1001j01jwokx6jhoc/see?quizType=REAL_EXAM&page=99

## 45. lqd-045

A data engineer is attempting to drop a Spark SQL table my_table. The data engineer wants to delete all table metadata and data. They run the following command: DROP TABLE IF EXISTS my_table. While the object no longer appears when they run SHOW TABLES, the data files still exist. Which of the following describes why the data files still exist and the metadata files were deleted?

A. The table's data was larger than 10 GB

B. The table's data was smaller than 10 GB

C. The table was external

D. The table did not have a location

E. The table was managed

**Source answer: C**

The reason why the data files still exist while the metadata files were deleted is because the table was external. When a table is external in Spark SQL (or in other database systems), it means that the table metadata (such as schema information and table structure) is managed externally, and Spark SQL assumes that the data is managed and maintained outside of the system. Therefore, when you execute a DROP TABLE statement for an external table, it removes only the table metadata from the catalog, leaving the data files intact. On the other hand, for managed tables (option E), Spark SQL manages both the metadata and the data files. When you drop a managed table, it deletes both the metadata and the associated data files, resulting in a complete removal of the table.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39uy000301k1ssstyehr/see?quizType=REAL_EXAM&page=82

## 46. lqd-046

Which of the following data lakehouse features results in improved data quality over a traditional data lake?

A. A data lakehouse provides storage solutions for structured and unstructured data.

B. A data lakehouse supports ACID-compliant transactions.

C. A data lakehouse allows the use of SQL queries to examine data.

D. A data lakehouse stores data in open formats.

E. A data lakehouse enables machine learning and artificial intelligence workloads.

**Source answer: B**

One of the key features of a data lakehouse that results in improved data quality over a traditional data lake is its support for ACID (Atomicity, Consistency, Isolation, Durability) transactions. ACID transactions provide data integrity and consistency guarantees, ensuring that operations on the data are reliable and that data is not left in an inconsistent state due to failures or concurrent access. In a traditional data lake, such transactional guarantees are often lacking, making it vulnerable to data inconsistency issues.

Source copies: 10; distinct source versions: 10.

Source: https://www.leetquiz.com/quiz/cmkcd39uz000401k1aqa2d1wa/see?quizType=REAL_EXAM&page=82

## 47. lqd-047

Question 45

A new data engineer new.engineer@company.com has been assigned to an ELT project. The new data engineer will need full privileges on the table sales to fully manage the project.

Which of the following commands can be used to grant full permissions on the table to the new data engineer?

A. GRANT ALL PRIVILEGES ON TABLE sales TO new.engineer@company.com;

B. GRANT USAGE ON TABLE sales TO new.engineer@company.com;

C. GRANT ALL PRIVILEGES ON TABLE new.engineer@company.com TO sales;

D. GRANT SELECT ON TABLE sales TO new.engineer@company.com;

E. GRANT SELECT CREATE MODIFY ON TABLE sales TO new.engineer@company.com;

**Source answer: A**

Explanation

Let's analyze each option:

A. GRANT ALL PRIVILEGES ON TABLE sales TO new.engineer@company.com; ✅

This is the correct command to grant full permissions on the table.
ALL PRIVILEGES grants all available privileges on the table, including SELECT, INSERT, UPDATE, DELETE, CREATE, MODIFY, etc.
The syntax follows the standard pattern: GRANT ALL PRIVILEGES ON TABLE <table_name> TO <user>;

B. GRANT USAGE ON TABLE sales TO new.engineer@company.com; ❌

USAGE privilege is insufficient for full management of the table.
USAGE typically allows basic access but not full administrative privileges.

C. GRANT ALL PRIVILEGES ON TABLE new.engineer@company.com TO sales; ❌

This syntax is incorrect and reversed.
It attempts to grant privileges on the user email to the table, which doesn't make sense.

D. GRANT SELECT ON TABLE sales TO new.engineer@company.com; ❌

This only grants SELECT privilege, which allows reading data but not modifying or managing the table.
Insufficient for full project management.

E. GRANT SELECT CREATE MODIFY ON TABLE sales TO new.engineer@company.com; ❌

This syntax is invalid - you cannot list multiple specific privileges this way.
The correct way to grant multiple specific privileges would be separate GRANT statements or use ALL PRIVILEGES.

Key Points:

ALL PRIVILEGES is the standard SQL command for granting full permissions on database objects
The syntax must follow: GRANT ALL PRIVILEGES ON TABLE <table_name> TO <user_or_role>;
This grants all available table-level privileges including SELECT, INSERT, UPDATE, DELETE, and administrative privileges

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmhaiya37001701k0pk8b0rlw/see?quizType=REAL_EXAM&page=82

## 48. lqd-048

Question 43

A data engineering manager has noticed that each of the queries in a Databricks SQL dashboard takes a few minutes to update when they manually click the “Refresh” button. They are curious why this might be occurring, so a team member provides a variety of reasons on why the delay might be occurring. Which of the following reasons fails to explain why the dashboard might be taking a few minutes to update?

A. The SQL endpoint being used by each of the queries might need a few minutes to start up.

B. The queries attached to the dashboard might take a few minutes to run under normal circumstances.

C. The queries attached to the dashboard might first be checking to determine if new data is available.

D. The Job associated with updating the dashboard might be using a non-pooled endpoint.

E. The queries attached to the dashboard might all be connected to their own, unstarted Databricks clusters.

**Source answer: D**



Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmhalewo60000il0nxsu2myhr/see?quizType=REAL_EXAM&page=82

## 49. lqd-049

Which of the following commands will return the location of database customer360?

A. DESCRIBE LOCATION customer360;

B. DROP DATABASE customer360;

C. DESCRIBE DATABASE customer360;

D. ALTER DATABASE customer360 SET DBPROPERTIES ('location' = '/user');

E. USE DATABASE customer360;

**Source answer: C**

To retrieve the location of a database named "customer360" in a database management system like Hive or Databricks, you can use the DESCRIBE DATABASE command followed by the database name. This command will provide information about the database, including its location.

Detailed

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39uy000101k10w8p57xo/see?quizType=REAL_EXAM&page=82

## 50. lqd-050

A data engineering team has noticed that their Databricks SQL queries are running too slowly when they are submitted to a non-running SQL endpoint. The data engineering team wants this issue to be resolved. Which of the following approaches can the team use to reduce the time it takes to return results in this scenario?

A. They can turn on the Serverless feature for the SQL endpoint and change the Spot Instance Policy to "Reliability Optimized."

B. They can turn on the Auto Stop feature for the SQL endpoint.

C. They can increase the cluster size of the SQL endpoint.

D. They can turn on the Serverless feature for the SQL endpoint.

E. They can increase the maximum bound of the SQL endpoint's scaling range

**Source answer: C**

Explanation

When Databricks SQL queries are running too slowly when submitted to a non-running SQL endpoint, the main issue is that the endpoint needs to start up (cold start) before processing queries. This startup time contributes significantly to the overall query execution time.

Let's analyze each option:

A. Turn on Serverless feature and change Spot Instance Policy to "Reliability Optimized"

Serverless SQL endpoints can help with cold starts, but changing the Spot Instance Policy to "Reliability Optimized" is more about cost optimization and reliability than reducing startup time.

B. Turn on the Auto Stop feature for the SQL endpoint

Auto Stop automatically stops the endpoint after a period of inactivity to save costs. This would actually make the problem worse because it would cause more frequent cold starts.

C. Increase the cluster size of the SQL endpoint (CORRECT)

Increasing the cluster size provides more compute resources, which can significantly reduce query execution time. Larger clusters have more processing power and memory, allowing queries to run faster. This directly addresses the performance issue.

D. Turn on the Serverless feature for the SQL endpoint

While Serverless endpoints can help with cold starts by providing faster provisioning, it's not the most direct solution for improving query performance once the endpoint is running.

E. Increase the maximum bound of the SQL endpoint's scaling range

This allows the endpoint to scale to larger sizes when needed, but doesn't guarantee faster performance for individual queries, especially during cold starts.

Key Insight: The question specifically mentions queries are slow when submitted to a non-running SQL endpoint. While cold start is part of the problem, increasing cluster size provides more compute resources that can process queries faster once the endpoint is running, which is the most direct solution to improve query performance.

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39uz000501k1wqlkw3xy/see?quizType=REAL_EXAM&page=83

## 51. lqd-051

Which of the following can be used to simplify and unify siloed data architectures that are specialized for specific use cases?

A. None of these

B. Data lake

C. Data warehouse

D. All of these

E. Data lakehouse

**Source answer: E**

The data lakehouse architecture combines the best features of data lakes and data warehouses to simplify and unify siloed data architectures. Data lakehouses provide:

Data lake flexibility - Ability to store raw, semi-structured, and structured data
Data warehouse performance - ACID transactions, schema enforcement, and BI tool support
Unified platform - Eliminates the need for separate specialized systems for different use cases
Simplified architecture - Reduces data movement and duplication between siloed systems

Traditional data lakes and data warehouses alone are specialized for specific use cases and contribute to siloed architectures. The data lakehouse addresses this limitation by providing a unified platform that serves both analytics and data science workloads.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd39uz000601k1d6hvt72c/see?quizType=REAL_EXAM&page=83

## 52. lqd-052

A data engineer only wants to execute the final block of a Python program if the Python variable day_of_week is equal to 1 and the Python variable review_period is True.

Which of the following control flow statements should the data engineer use to begin this conditionally executed code block?

A. if day_of_week = 1 and review_period:

B. if day_of_week = 1 and review_period = "True":

C. if day_of_week == 1 and review_period == "True":

D. if day_of_week == 1 and review_period:

E. if day_of_week = 1 & review_period == "True":

**Source answer: D**

This statement will check if the variable day_of_week is equal to 1 and if the variable review_period evaluates to a truthy value. The use of the double equal sign (==) in the comparison of day_of_week is important, as a single equal sign (=) would be used to assign a value to the variable instead of checking its value. The use of a single ampersand (&) instead of the keyword and is not valid syntax in Python. The use of quotes around True in options B and C will result in a string comparison, which will not evaluate to True even if the value of review_period is True.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd39uz000701k1512n5b7j/see?quizType=REAL_EXAM&page=83

## 53. lqd-053

Which of the following is a benefit of the Databricks Lakehouse Platform embracing open source technologies?

A. Cloud-specific integrations

B. Simplified governance

C. Ability to scale storage

D. Ability to scale workloads

E. Avoiding vendor lock-in

**Source answer: E**

The Databricks Lakehouse Platform's embrace of open source technologies provides the benefit of avoiding vendor lock-in. This allows organizations to maintain flexibility and portability across different cloud providers and environments, rather than being tied to proprietary solutions that limit their options. Open source technologies enable greater interoperability and reduce dependency on specific vendors.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd3s9m000601jzp17a6r94/see?quizType=REAL_EXAM&page=88

## 54. lqd-054

A data analyst has created a Delta table sales that is used by the entire data analysis team. They want help from the data engineering team to implement a series of tests to ensure the data is clean. However, the data engineering team uses Python for its tests rather than SQL. Which of the following commands could the data engineering team use to access sales in PySpark?

A. SELECT * FROM sales

B. There is no way to share data between Pyspark and SQL.

C. spark.sql("sales")

D. spark.delta.table("sales")

E. spark.table("sales")

**Source answer: E**

Explanation

In PySpark, there are multiple ways to access Delta tables:

spark.table("sales") - This is the correct method to access a registered table in PySpark. When a Delta table is created, it's typically registered in the Spark catalog, and spark.table() can be used to access it.

spark.sql("SELECT * FROM sales") - While option A shows SELECT * FROM sales alone, in PySpark you would need to wrap it in spark.sql() to execute SQL queries.

spark.read.table("sales") - Another valid method for reading tables.

spark.read.format("delta").table("sales") - For explicitly specifying Delta format.

Why other options are incorrect:

A: SELECT * FROM sales alone is not valid PySpark syntax - it needs to be wrapped in spark.sql()
B: This is false - Delta tables can be accessed from both SQL and PySpark
C: spark.sql("sales") is incorrect syntax - spark.sql() expects a SQL query, not just a table name
D: spark.delta.table("sales") is not valid PySpark syntax - there's no spark.delta.table() method

The most straightforward and correct way to access a registered Delta table in PySpark is spark.table("sales").

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75ny000s01jwvfgypxvv/see?quizType=REAL_EXAM&page=95

## 55. lqd-055

A new data engineering team has been assigned to work on a project. The team will need access to database customers in order to see what tables already exist. The team has its own group team. Which of the following commands can be used to grant the necessary permission on the entire database to the new team?

A. GRANT VIEW ON CATALOG customers TO team;

B. GRANT CREATE ON DATABASE customers TO team;

C. GRANT USAGE ON CATALOG team TO customers;

D. GRANT CREATE ON DATABASE team TO customers;

E. GRANT USAGE ON DATABASE customers TO team;

**Source answer: E**

The correct answer is E because:

USAGE privilege is required to access and view objects within a database. The USAGE privilege on a database allows users to see what tables exist within that database.

Database context: The question specifies access to the "database customers" for the "team" group, so the syntax should be GRANT USAGE ON DATABASE customers TO team;

Why other options are incorrect:

A: GRANT VIEW ON CATALOG customers TO team; - This grants view permission on a catalog, not a database
B: GRANT CREATE ON DATABASE customers TO team; - This grants CREATE permission, which allows creating new tables, but not necessarily viewing existing ones
C: GRANT USAGE ON CATALOG team TO customers; - This reverses the direction (grants permission on catalog 'team' to 'customers')
D: GRANT CREATE ON DATABASE team TO customers; - This grants CREATE permission on database 'team' to 'customers', which is the opposite of what's needed

Note: The explanation in the original text mentions GRANT ALL PRIVILEGES ON DATABASE customers TO team; which would also work, but among the given options, only E provides the necessary USAGE privilege to view existing tables in the database.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000b01k11tfhyxys/see?quizType=REAL_EXAM&page=83

## 56. lqd-056

Which of the following describes the relationship between Bronze tables and raw data?

A. Bronze tables contain less data than raw data files.

B. Bronze tables contain more truthful data than raw data.

C. Bronze tables contain aggregates while raw data is unaggregated.

D. Bronze tables contain a less refined view of data than raw data.

E. Bronze tables contain raw data with a schema applied.

**Source answer: E**

The Bronze layer is where we land all the data from external source systems. The table structures in this layer correspond to the source system table structures "as-is," along with any additional metadata columns that capture the load date/time, process ID, etc. The focus in this layer is quick Change Data Capture and the ability to provide an historical archive of source (cold storage), data lineage, auditability, reprocessing if needed without rereading the data from the source system. https://www.databricks.com/glossary/medallion-architecture

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000c01k15yzodkk4/see?quizType=REAL_EXAM&page=84

## 57. lqd-057

In order for Structured Streaming to reliably track the exact progress of the processing so that it can handle any kind of failure by restarting and/or reprocessing, which of the following two approaches is used by Spark to record the offset range of the data being processed in each trigger?

A. Checkpointing and Write-ahead Logs

B. Structured Streaming cannot record the offset range of the data being processed in each trigger.

C. Replayable Sources and Idempotent Sinks

D. Write-ahead Logs and Idempotent Sinks

E. Checkpointing and Idempotent Sinks

**Source answer: A**

The engine uses checkpointing and write-ahead logs to record the offset range of the data being processed in each trigger. This approach ensures reliable progress tracking and enables Structured Streaming to handle failures by restarting and/or reprocessing data. Checkpointing saves the state of the streaming query, while write-ahead logs record the offset ranges that have been processed, allowing for exactly-once processing semantics.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000d01k1jc3jjbl3/see?quizType=REAL_EXAM&page=84

## 58. lqd-058

CREATE TABLE customersInFrance

CREATE TABLE customersInFrance
_______ AS
SELECT id,
       firstName,
       lastName,
FROM customerLocations
WHERE country = 'FRANCE';


A senior data engineer mentions that it is organization policy to include a table property indicating that the new table includes personally identifiable information (PII). Which of the following lines of code fills in the above blank to successfully complete the task?

A. There is no way to indicate whether a table contains PII.

B. "COMMENT PII"

C. TBLPROPERTIES P II

D. COMMENT "Contains PII"

E. PII

**Source answer: D**

Correct Answer: D

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000e01k12zsnw8sh/see?quizType=REAL_EXAM&page=84

## 59. lqd-059

A new data engineering team has been assigned to an ELT project. The new data engineering team will need full privileges on the database customers to fully manage the project. Which of the following commands can be used to grant full permissions on the database to the new data engineering team?

A. GRANT USAGE ON DATABASE customers TO team;

B. GRANT ALL PRIVILEGES ON DATABASE team TO customers;

C. GRANT SELECT PRIVILEGES ON DATABASE customers TO teams;

D. GRANT SELECT CREATE MODIFY USAGE PRIVILEGES ON DATABASE customersTO team;

E. GRANT ALL PRIVILEGES ON DATABASE customers TO team;

**Source answer: E**

To grant full privileges on the database "customers" to the new data engineering team, you can use the GRANT ALL PRIVILEGES command as shown in option E. This command provides the team with all possible privileges on the specified database, allowing them to fully manage it.

Detailed

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000f01k19r7nmmkx/see?quizType=REAL_EXAM&page=84

## 60. lqd-060

A data engineer has three tables in a Delta Live Tables (DLT) pipeline. They have configured the pipeline to drop invalid records at each table. They notice that some data is being dropped due to quality concerns at some point in the DLT pipeline. They would like to determine at which table in their pipeline the data is being dropped.

Which of the following approaches can the data engineer take to identify the table that is dropping the records?

A. They can set up separate expectations for each table when developing their DLT pipeline.

B. They cannot determine which table is dropping the records.

C. They can set up DLT to notify them via email when records are dropped.

D. They can navigate to the DLT pipeline page, click on each table, and view the data quality statistics.

E. They can navigate to the DLT pipeline page, click on the "Error" button, and review the present errors.

**Source answer: D**

To identify the table in a Delta Live Tables (DLT) pipeline where data is being dropped due to quality concerns, the data engineer can navigate to the DLT pipeline page, click on each table in the pipeline, and view the data quality statistics. These statistics often include information about records dropped, violations of expectations, and other data quality metrics. By examining the data quality statistics for each table in the pipeline, the data engineer can determine at which table the data is being dropped.

Why other options are incorrect:

A: Setting up separate expectations for each table helps define quality rules but doesn't directly help identify which table is currently dropping records.
B: This is incorrect because there is a way to determine which table is dropping records through the DLT UI.
C: Email notifications can alert about quality issues but don't specifically identify which table is dropping records.
E: The "Error" button typically shows pipeline execution errors, not detailed data quality statistics for individual tables.
Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000g01k17jm02cb4/see?quizType=REAL_EXAM&page=84

## 61. lqd-061

A data engineer is running code in a Databricks Repo that is cloned from a central Git repository. A colleague of the data engineer informs them that changes have been made and synced to the central Git repository. The data engineer now needs to sync their Databricks Repo to get the changes from the central Git repository. Which of the following Git operations does the data engineer need to run to accomplish this task?

A. Merge

B. Push

C. Pull

D. Commit

E. Clone

**Source answer: C**

To synchronize local changes with the remote repository, the data engineer should use the pull command. This retrieves the latest changes from the central Git repository and integrates them into the local Databricks Repo.

Detailed

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v0000h01k1sa1xgi76/see?quizType=REAL_EXAM&page=84

## 62. lqd-062

A data analyst has a series of queries in a SQL program. The data analyst wants this program to run every day. They only want the final query in the program to run on Sundays. They ask for help from the data engineering team to complete this task. Which of the following approaches could be used by the data engineering team to complete this task?

A. They could submit a feature request with Databricks to add this functionality.

B. They could wrap the queries using PySpark and use Python's control flow system to determine when to run the final query.

C. They could only run the entire program on Sundays.

D. They could automatically restrict access to the source table in the final query so that it is only accessible on Sundays.

E. They could redesign the data model to separate the data used in the final query into a new table.

**Source answer: B**

Explanation

The correct answer is B because:

Using PySpark with Python's control flow allows for conditional execution of queries based on the day of the week. The data engineering team can wrap the SQL queries in a PySpark script and use Python's datetime module to check if today is Sunday before executing the final query.

Why other options are incorrect:

A: Submitting a feature request is not a practical solution for immediate implementation.
C: Running the entire program only on Sundays contradicts the requirement to run the program daily (with only the final query conditionally executed on Sundays).
D: Restricting table access based on days is not a standard practice and would affect all users, not just this specific program.
E: Redesigning the data model is unnecessary and doesn't solve the conditional execution requirement.

Implementation approach:

from pyspark.sql import SparkSession
import datetime

spark = SparkSession.builder.appName("ConditionalQuery").getOrCreate()

# Run first queries daily
spark.sql("SELECT * FROM table1 WHERE ...")
spark.sql("SELECT * FROM table2 WHERE ...")

# Check if today is Sunday
if datetime.datetime.today().weekday() == 6:  # Sunday is 6 in Python
    spark.sql("SELECT * FROM final_table WHERE ...")  # Final query


This approach provides the flexibility to run the program daily while conditionally executing the final query only on Sundays.

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75nx000m01jw9evh0bex/see?quizType=REAL_EXAM&page=95

## 63. lqd-063

Which of the following benefits of using the Databricks Lakehouse Platform is provided by Delta Lake?

A. The ability to manipulate the same data using a variety of languages

B. The ability to collaborate in real time on a single notebook

C. The ability to set up alerts for query failures

D. The ability to support batch and streaming workloads

E. The ability to distribute complex data operations

**Source answer: D**

Delta Lake provides ACID transactions, schema enforcement, and unified batch and streaming data processing. This is one of the key benefits of Delta Lake within the Databricks Lakehouse Platform - the ability to support both batch and streaming workloads on the same data. Options A, B, C, and E describe features that are part of the broader Databricks platform but are not specifically provided by Delta Lake itself.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000j01k11jnur4vy/see?quizType=REAL_EXAM&page=85

## 64. lqd-064

A data engineer needs to apply custom logic to identify employees with more than 5 years of experience in array column employees in table stores. The custom logic should create a new column exp_employees that is an array of all of the employees with more than 5 years of experience for each row. In order to apply this custom logic at scale, the data engineer wants to use the FILTER higher-order function. Which of the following code blocks successfully completes this task?

A. SELECT
    store_id,
    employees,
    FILTER (employees, i -> i.years_exp > 5) AS exp_employees
FROM stores;


B. SELECT
    store_id,
    employees,
    FILTER (exp_employees, years_exp > 5) AS exp_employees
FROM stores;


C. SELECT
    store_id,
    employees,
    FILTER (employees, years_exp > 5) AS exp_employees
FROM stores;


D. SELECT
    store_id,
    employees,
    CASE WHEN employees.years_exp > 5 THEN employees
         ELSE NULL
    END AS exp_employees
FROM stores;


E. SELECT
    store_id,
    employees,
    FILTER (exp_employees, i -> i.years_exp > 5) AS exp_employees
FROM stores;


**Source answer: A**

Explanation

Option A is correct because it properly uses the FILTER higher-order function with the correct syntax:

FILTER function structure: FILTER(array, lambda_function)
Correct array reference: employees is the source array column
Proper lambda syntax: i -> i.years_exp > 5 where i represents each element in the array, and i.years_exp accesses the years_exp field of each employee object

Why other options are incorrect:

Option B: Incorrectly references exp_employees in the FILTER function before it's created. Also missing lambda syntax.
Option C: Missing lambda function syntax - needs i -> i.years_exp > 5 instead of just years_exp > 5
Option D: Uses CASE statement which doesn't filter arrays properly - it would return the entire array or NULL, not filter individual elements
Option E: Incorrectly references exp_employees in the FILTER function before it's created

Key Concepts:

FILTER is a higher-order function that takes an array and a lambda function
The lambda function should return true/false for each element
In Spark SQL/Databricks, array elements are accessed using dot notation within lambda functions

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000k01k19qvh5i6r/see?quizType=REAL_EXAM&page=85

## 65. lqd-065

A data engineer wants to schedule their Databricks SQL dashboard to refresh once per day, but they only want the associated SQL endpoint to be running when it is necessary. Which of the following approaches can the data engineer use to minimize the total running time of the SQL endpoint used in the refresh schedule of their dashboard?

A. They can ensure the dashboard’s SQL endpoint matches each of the queries’ SQL endpoints.

B. They can set up the dashboard’s SQL endpoint to be serverless.

C. They can turn on the Auto Stop feature for the SQL endpoint.

D. They can reduce the cluster size of the SQL endpoint.

E. They can ensure the dashboard’s SQL endpoint is not one of the included query’s SQL endpoint.

**Source answer: C**

Explanation

The correct answer is C - They can turn on the Auto Stop feature for the SQL endpoint.

Why this is correct:

Auto Stop Feature: This feature automatically stops the SQL endpoint after a period of inactivity, which is exactly what the data engineer needs. Since the dashboard only refreshes once per day, the SQL endpoint can be stopped when not in use, minimizing its running time.

How it works: When Auto Stop is enabled, the SQL endpoint will automatically shut down after a configurable period of inactivity (typically 10-30 minutes). When the scheduled refresh occurs, the endpoint will automatically start up, run the queries, and then stop again after the inactivity period.

Why other options are incorrect:

A. They can ensure the dashboard’s SQL endpoint matches each of the queries’ SQL endpoints.

This ensures consistency but doesn't minimize running time. Matching endpoints doesn't control when the endpoint runs.

B. They can set up the dashboard’s SQL endpoint to be serverless.

Serverless SQL endpoints are always running and billed by compute usage, not by minimizing running time. They don't automatically stop when not in use.

D. They can reduce the cluster size of the SQL endpoint.

This reduces compute cost but doesn't minimize the total running time. A smaller cluster still runs continuously unless stopped.

E. They can ensure the dashboard’s SQL endpoint is not one of the included query’s SQL endpoint.

This doesn't make sense in this context and wouldn't help minimize running time. It might actually cause inefficiencies if queries use different endpoints.
Best Practice:

For dashboards that refresh infrequently (like once per day), enabling Auto Stop is the most cost-effective approach as it ensures the SQL endpoint only runs when needed and automatically stops after completing the refresh, minimizing both running time and costs.

Source copies: 8; distinct source versions: 8.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000l01k127a28egh/see?quizType=REAL_EXAM&page=85

## 66. lqd-066

Which of the following commands can be used to write data into a Delta table while avoiding the writing of duplicate records?

A. DROP

B. IGNORE

C. MERGE

D. APPEND

E. INSERT

**Source answer: C**

To write data into a Delta table while avoiding the writing of duplicate records, you can use the MERGE command. The MERGE command in Delta Lake allows you to combine the ability to insert new records and update existing records in a single atomic operation. The MERGE command compares the data being written with the existing data in the Delta table based on specified matching criteria, typically using a primary key or unique identifier. It then performs conditional actions, such as inserting new records or updating existing records, depending on the comparison results. By using the MERGE command, you can handle the prevention of duplicate records in a more controlled and efficient manner. It allows you to synchronize and reconcile data from different sources while avoiding duplication and ensuring data integrity.

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000m01k17pmv0lqj/see?quizType=REAL_EXAM&page=85

## 67. lqd-067

A data engineer has a Python notebook in Databricks, but they need to use SQL to accomplish a specific task within a cell. They still want all of the other cells to use Python without making any changes to those cells. Which of the following describes how the data engineer can use SQL within a cell of their Python notebook?

A. It is not possible to use SQL in a Python notebook

B. They can attach the cell to a SQL endpoint rather than a Databricks cluster

C. They can simply write SQL syntax in the cell

D. They can add %sql to the first line of the cell

E. They can change the default language of the notebook to SQL

**Source answer: D**

In Databricks notebooks, you can use language magic commands to specify the language for individual cells. To use SQL in a Python notebook cell, you need to add %sql as the first line of that specific cell. This tells Databricks to interpret the cell content as SQL code while keeping other cells as Python. Option A is incorrect because it is possible to use SQL in Python notebooks. Option B is incorrect because attaching to a SQL endpoint doesn't enable SQL syntax in a Python notebook cell. Option C is incorrect because simply writing SQL syntax without the magic command will cause an error. Option E is incorrect because changing the default language would affect all cells, not just the specific one.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000n01k1i2nxyitl/see?quizType=REAL_EXAM&page=85

## 68. lqd-068

Which of the following describes a scenario in which a data engineer will want to use a single node cluster?

A. When they are working interactively with a small amount of data

B. When they are running automated reports to be refreshed as quickly as possible

C. When they are working with SQL within Databricks SQL

D. When they are concerned about the ability to automatically scale with larger data

E. When they are manually running reports with a large amount of data

**Source answer: A**

Explanation

A single node cluster is most appropriate when working interactively with a small amount of data because:

Cost Efficiency: Single node clusters are less expensive as they don't require multiple worker nodes
Interactive Development: For exploratory data analysis, development, and testing with small datasets, a single node is sufficient
Reduced Overhead: No network communication overhead between nodes
Simplified Debugging: Easier to debug issues when working on a single node

Why other options are incorrect:

B: Automated reports that need quick refresh would benefit from multi-node clusters for parallel processing
C: Working with SQL in Databricks SQL doesn't necessarily require a single node cluster; it depends on the data size and complexity
D: Concern about automatic scaling with larger data indicates a need for multi-node clusters with auto-scaling capabilities
E: Manual reports with large amounts of data would require multi-node clusters for distributed processing

Single node clusters are ideal for development, testing, and small-scale interactive work where the data fits comfortably in memory and doesn't require distributed processing.

Source copies: 5; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75o0001801jwi1o5nvzk/see?quizType=REAL_EXAM&page=98

## 69. lqd-069

A data engineer is required to create a table in Databricks using data from a CSV file at location /path/to/csv.

CREATE TABLE new_table
______

OPTIONS (
    header = "true",
    delimiter = "|"
)
LOCATION "path/to/csv"


Which of the following lines of code fills in the above blank to successfully complete the task?

A. None of these lines of code are needed to successfully complete the task

B. USING CSV

C. FROM CSV

D. USING DELTA

E. FROM "path/to/csv"

**Source answer: B**

The correct answer is B (USING CSV). In Databricks SQL, when reading CSV files, you use the USING CSV clause to specify the file format. This is the proper syntax for loading CSV data in Databricks. Option A is incorrect because format specification is needed. Option C (FROM CSV) uses incorrect syntax. Option D (USING DELTA) is for Delta format, not CSV. Option E (FROM "path/to/csv") only specifies the path but not the format.

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v1000p01k1ew1x8ywh/see?quizType=REAL_EXAM&page=85

## 70. lqd-070

A data engineer has realized that they made a mistake when making a daily update to a table. They need to use Delta time travel to restore the table to a version that is 3 days old. However, when the data engineer attempts to time travel to the older version, they are unable to restore the data because the data files have been deleted.

Which of the following explains why the data files are no longer present?

A. The VACUUM command was run on the table

B. The TIME TRAVEL command was run on the table

C. The DELETE HISTORY command was run on the table

D. The OPTIMIZE command was run on the table

E. The HISTORY command was run on the table

**Source answer: A**

The VACUUM command in Delta Lake is used to clean up and remove unnecessary data files that are no longer needed for time travel or query purposes. When you run VACUUM with certain retention settings, it can delete older data files, which might include versions of data that are older than the specified retention period. If the data engineer is unable to restore the table to a version that is 3 days old because the data files have been deleted, it's likely because the VACUUM command was run on the table, removing the older data files as part of data cleanup.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000q01k1uvnzfb8g/see?quizType=REAL_EXAM&page=86

## 71. lqd-071

Which of the following describes a scenario in which a data team will want to utilize cluster pools?

A. An automated report needs to be refreshed as quickly as possible.

B. An automated report needs to be made reproducible.

C. An automated report needs to be tested to identify errors.

D. An automated report needs to be version-controlled across multiple collaborators.

E. An automated report needs to be runnable by all stakeholders.

**Source answer: A**

Cluster pools are typically used in distributed computing environments, such as cloud-based data platforms like Databricks. They allow you to pre-allocate a set of compute resources (a cluster) for specific tasks or workloads. In this case, if an automated report needs to be refreshed as quickly as possible, you can allocate a cluster pool with sufficient resources to ensure fast data processing and report generation. This helps ensure that the report is generated with minimal latency and can be delivered to stakeholders in a timely manner. Cluster pools allow you to optimize resource allocation for high-demand, time-sensitive tasks like real-time report generation.

Source copies: 8; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000r01k1w9whg3en/see?quizType=REAL_EXAM&page=86

## 72. lqd-072

A data engineer has a Job that has a complex run schedule, and they want to transfer that schedule to other jobs. Rather than manually selecting each value in the scheduling form in Databricks, which of the following tools can the data engineer use to represent and submit the schedule programmatically?

A. pyspark.sql.types.DateType

B. datetime

C. pyspark.sql.types.TimestampType

D. Cron syntax

E. There is no way to represent and submit this information programmatically

**Source answer: D**

Explanation

Correct Answer: D - Cron syntax

In Databricks, job schedules can be defined programmatically using Cron syntax. This allows data engineers to:

Programmatically define schedules - Cron expressions provide a standardized way to represent complex scheduling patterns
Transfer schedules between jobs - Once defined as a Cron expression, the same schedule can be easily applied to multiple jobs
Use Databricks APIs - The Databricks Jobs API accepts Cron syntax for scheduling when creating or updating jobs programmatically

Why other options are incorrect:

A. pyspark.sql.types.DateType - This is a Spark SQL data type for dates, not a scheduling mechanism
B. datetime - While Python's datetime module handles date/time operations, it doesn't provide a way to define recurring schedules for Databricks jobs
C. pyspark.sql.types.TimestampType - Similar to DateType, this is a data type for timestamps in Spark SQL, not a scheduling tool
E. There is no way to represent and submit this information programmatically - This is incorrect because Databricks provides programmatic scheduling through Cron syntax and APIs

Practical Application:

When using Databricks Jobs API (e.g., via Databricks CLI, REST API, or SDKs), you can specify a schedule using a Cron expression like:

{
  "schedule": {
    "quartz_cron_expression": "0 0 9 * * ?",
    "timezone_id": "America/Los_Angeles"
  }
}


This allows for automation and consistency across multiple jobs with complex scheduling requirements.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000s01k1zil5979e/see?quizType=REAL_EXAM&page=86

## 73. lqd-073

A data engineer and data analyst are working together on a data pipeline. The data engineer is working on the raw, bronze, and silver layers of the pipeline using Python, and the data analyst is working on the gold layer of the pipeline using SQL. The raw source of the pipeline is a streaming input. They now want to migrate their pipeline to use Delta Live Tables. Which of the following changes will need to be made to the pipeline when migrating to Delta Live Tables?

A. None of these changes will need to be made

B. The pipeline will need to stop using the mediation-based multi-hop architecture

C. The pipeline will need to be written entirely in SQL

D. The pipeline will need to use a batch source in place of a streaming source

E. The pipeline will need to be written entirely in Python

**Source answer: A**

Explanation

Delta Live Tables (DLT) is designed to be flexible and support various pipeline architectures. Let's analyze each option:

A. None of these changes will need to be made - CORRECT

DLT supports both Python and SQL for different parts of the pipeline
DLT supports streaming sources natively
DLT supports the medallion (bronze/silver/gold) architecture
DLT allows mixing Python and SQL in the same pipeline

B. The pipeline will need to stop using the mediation-based multi-hop architecture - INCORRECT

DLT actually encourages and supports the medallion architecture (bronze/silver/gold)
This is a recommended pattern for DLT pipelines

C. The pipeline will need to be written entirely in SQL - INCORRECT

DLT supports both Python and SQL
You can mix Python and SQL in the same DLT pipeline
The data engineer can continue using Python for bronze/silver layers

D. The pipeline will need to use a batch source in place of a streaming source - INCORRECT

DLT supports both streaming and batch processing
Streaming sources are fully supported in DLT

E. The pipeline will need to be written entirely in Python - INCORRECT

DLT supports both Python and SQL
The data analyst can continue using SQL for the gold layer

Key DLT Features:

Language Flexibility: Supports both Python and SQL in the same pipeline
Streaming Support: Handles both streaming and batch data sources
Medallion Architecture: Designed to work with bronze/silver/gold layers
Incremental Processing: Automatically handles incremental updates
Declarative Approach: Focus on what data should be, not how to compute it

The existing pipeline architecture is already compatible with DLT, so no changes are needed.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000t01k1n7lhv37m/see?quizType=REAL_EXAM&page=86

## 74. lqd-074

Which of the following data workloads will utilize a Gold table as its source?

A. A job that enriches data by parsing its timestamps into a human-readable format

B. A job that aggregates uncleaned data to create standard summary statistics

C. A job that cleans data by removing malformed records

D. A job that queries aggregated data designed to feed into a dashboard

E. A job that ingests raw data from a streaming source into the Lakehouse

**Source answer: D**

Explanation

In the Databricks Lakehouse architecture, data typically flows through three layers:

Bronze Layer: Raw, unprocessed data ingested from source systems
Silver Layer: Cleaned, validated, and enriched data
Gold Layer: Aggregated, business-ready data optimized for consumption

Gold tables contain aggregated, business-ready data that is optimized for consumption by end-users, dashboards, and reporting tools. They represent the final, refined data layer where data is:

Aggregated to business-level metrics
Optimized for query performance
Structured for specific business use cases
Ready for consumption by BI tools and dashboards

Analysis of each option:

A: This describes data enrichment (parsing timestamps), which typically happens in the Silver layer, not using Gold tables as source.
B: This describes aggregating uncleaned data, which would happen before the Gold layer (likely in Silver or Bronze).
C: This describes data cleaning (removing malformed records), which is a Silver layer activity.
D: CORRECT - Querying aggregated data for dashboards is exactly what Gold tables are designed for. Gold tables contain aggregated, business-ready data optimized for consumption by dashboards and reporting tools.
E: This describes data ingestion from streaming sources, which is a Bronze layer activity.

Therefore, only option D correctly describes a workload that would utilize a Gold table as its source.

Source copies: 4; distinct source versions: 3.

Source: https://www.leetquiz.com/quiz/cmkcd75o3001s01jwkiac9jv9/see?quizType=REAL_EXAM&page=101

## 75. lqd-075

A dataset has been defined using Delta Live Tables and includes an expectations clause:

CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') ON VIOLATION FAIL UPDATE


What is the expected behavior when a batch of data containing data that violates these constraints is processed?

A. Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.

B. Records that violate the expectation cause the job to fail.

C. Records that violate the expectation are dropped from the target dataset and loaded into a quarantine table.

D. Records that violate the expectation are added to the target dataset and recorded as invalid in the event log.

E. Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.

**Source answer: B**

The ON VIOLATION FAIL UPDATE clause in Delta Live Tables expectations causes the entire job to fail when any records violate the constraint. This is different from the warn action (which allows invalid records to be written while reporting metrics) or the drop action (which drops invalid records and continues processing). The fail action requires manual intervention before re-processing can occur, making it suitable for critical data quality requirements where invalid data should not be processed at all.

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000v01k1fn2q20ka/see?quizType=REAL_EXAM&page=86

## 76. lqd-076

A data engineer that is new to using Python needs to create a Python function to add two integers together and return the sum. Which of the following code blocks can the data engineer use to complete this task?

A. function add_integers(x, y):
    return x + y


B. function add_integers(x,y):
    x + y


C. def add_integers(x, y):
    print(x + y)


D. def add_integers(x, y):
    return x + y


E. def add_integers(x, y):
    x + y


**Source answer: D**

Explanation

Let's analyze each option:

Option A: Incorrect. Python uses def keyword to define functions, not function. The syntax is wrong.

Option B: Incorrect. Same issue as Option A - uses function keyword instead of def. Also, the function doesn't return anything explicitly.

Option C: Incorrect. While it uses the correct def keyword, it prints the result instead of returning it. The requirement is to "return the sum", not print it.

Option D: CORRECT. This uses the proper Python syntax with def keyword, takes two parameters x and y, and returns their sum using the return statement.

Option E: Incorrect. Uses correct def keyword but doesn't return the result. In Python, if you don't explicitly return a value, the function returns None.

Key Python concepts:

Functions in Python are defined using the def keyword
The return statement is used to return a value from a function
Without a return statement, a function returns None by default
print() outputs to console but doesn't return a value for further use in code

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o2001l01jwnuj5u6r2/see?quizType=REAL_EXAM&page=100

## 77. lqd-077

Which of the following code blocks will remove the rows where the value in column age is greater than 25 from the existing Delta table my_table and save the updated table?

A. SELECT * FROM my_table WHERE age > 25;

B. UPDATE my_table WHERE age > 25;

C. DELETE FROM my_table WHERE age > 25;

D. UPDATE my_table WHERE age <= 25;

E. DELETE FROM my_table WHERE age <= 25;

**Source answer: C**

The correct answer is C because:

DELETE statement: The DELETE statement is used to remove rows from a table based on a condition.
Condition: The requirement is to remove rows where age > 25, so the WHERE clause should be WHERE age > 25.
Other options analysis:
A: SELECT statement only retrieves data, doesn't modify the table.
B: UPDATE statement modifies existing rows, doesn't delete them.
D: UPDATE statement with wrong condition (would update rows where age <= 25).
E: DELETE statement with wrong condition (would delete rows where age <= 25, opposite of what's needed).

In Delta Lake, DELETE operations are fully supported and provide ACID transactions, making option C the correct choice for removing rows where age > 25.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd39v2000x01k1ru4056lg/see?quizType=REAL_EXAM&page=87

## 78. lqd-078

A data engineer is maintaining a data pipeline. Upon data ingestion, the data engineer notices that the source data is starting to have a lower level of quality. The data engineer would like to automate the process of monitoring the quality level. Which of the following tools can the data engineer use to solve this problem?

A. Unity Catalog

B. Data Explorer

C. Delta Lake

D. Delta Live Tables

E. Auto Loader

**Source answer: D**

Delta Live Tables (DLT) is the correct tool for automating data quality monitoring in Databricks pipelines. DLT provides built-in data quality features including:

Expectations framework: Allows you to define data quality constraints
Automated monitoring: Continuously monitors data quality during pipeline execution
Quality metrics tracking: Records and tracks data quality metrics over time
Pipeline health monitoring: Provides visibility into data quality issues
Automated remediation: Can be configured to handle quality violations (e.g., quarantine bad data, stop pipeline)

While other options have some related functionality:

Unity Catalog (A): Primarily for data governance, cataloging, and access control
Data Explorer (B): For exploring and visualizing data, not automated quality monitoring
Delta Lake (C): Provides ACID transactions and schema enforcement, but not automated quality monitoring
Auto Loader (E): For incremental data ingestion, not quality monitoring

DLT's data quality features are specifically designed to automate the monitoring and management of data quality in production pipelines.

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39v3000y01k15e7oaxvp/see?quizType=REAL_EXAM&page=87

## 79. lqd-079

A data engineer has developed a data pipeline to ingest data from a JSON source using Auto Loader, but the engineer has not provided any type inference or schema hints in their pipeline. Upon reviewing the data, the data engineer has noticed that all of the columns in the target table are of the string type despite some of the fields only including float or boolean values.

Which of the following describes why Auto Loader inferred all of the columns to be of the string type?

A. There was a type mismatch between the specific schema and the inferred schema

B. JSON data is a text-based format

C. Auto Loader only works with string data

D. All of the fields had at least one null value

E. Auto Loader cannot infer the schema of ingested data

**Source answer: B**

Explanation

Auto Loader infers all columns as string type when ingesting JSON data because:

JSON is inherently text-based: JSON (JavaScript Object Notation) is a text format that represents data as strings. Even when JSON contains numeric values like 42 or boolean values like true, they are fundamentally represented as text in the JSON file.

Auto Loader's default behavior: When no schema hints or type inference options are provided, Auto Loader treats all JSON data as strings to ensure data ingestion doesn't fail due to type mismatches. This is a safe default approach.

Why other options are incorrect:

Option A: Type mismatch between specific and inferred schema - This would cause errors, not all-string inference.
Option C: Auto Loader only works with string data - False, Auto Loader can handle various data types with proper schema hints.
Option D: All fields had at least one null value - Null values don't force string type inference.
Option E: Auto Loader cannot infer schema - False, Auto Loader can infer schema, but defaults to string for JSON.

Solution: To properly infer types, the data engineer should use schema hints or enable type inference options like cloudFiles.schemaEvolutionMode or provide an explicit schema.

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd39v3000z01k18ur0b8av/see?quizType=REAL_EXAM&page=87

## 80. lqd-080

Which of the following Structured Streaming queries is performing a hop from a Silver table to a Gold table?

A. (spark.readStream.load(rawSalesLocation)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


B. (spark.read.load(rawSalesLocation)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


C. (spark.table("sales")
  .withColumn("avgPrice", col("sales") / col("units"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


D. (spark.table("sales")
  .filter(col("units") > 0)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


E. (spark.table("sales")
  .groupBy("store")
  .agg(sum("sales"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("complete")
  .table("newSales"))


**Source answer: E**

Explanation

In Databricks Lakehouse architecture, data typically flows through different quality tiers:

Bronze: Raw data ingestion
Silver: Cleaned, validated data
Gold: Aggregated, business-ready data for analytics

A hop from Silver to Gold means transforming Silver-level data (already cleaned and validated) into aggregated, business-ready Gold tables.

Let's analyze each option:

Option A: Reads from rawSalesLocation (likely Bronze/raw data) and writes to newSales. This is a Bronze-to-Silver hop, not Silver-to-Gold.

Option B: Uses spark.read.load() (batch read) with writeStream (streaming write) - this is incorrect syntax and doesn't represent a proper hop.

Option C: Reads from sales table (could be Silver) and performs a simple transformation (avgPrice calculation), then writes to newSales. This is a simple transformation but not necessarily a Silver-to-Gold hop as it doesn't involve aggregation.

Option D: Reads from sales table (could be Silver) and performs filtering, then writes to newSales. This is filtering, not aggregation for Gold tables.

Option E: Reads from sales table (Silver), performs aggregation (groupBy and sum), and writes to newSales with complete output mode. This represents a Silver-to-Gold hop because:

It reads from an existing table (sales) which is likely a Silver table
It performs aggregation (groupBy and agg) which is typical for Gold table transformations
It uses complete output mode which is appropriate for aggregated results
The transformation creates business-ready aggregated data suitable for analytics

The key indicators of a Silver-to-Gold hop are:

Reading from an existing table (not raw data)
Performing aggregations or complex business transformations
Creating data suitable for business analytics and reporting

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd39v3001001k1fe1217dw/see?quizType=REAL_EXAM&page=87

## 81. lqd-081

A data engineer wants to create a relational object by pulling data from two tables. The relational object does not need to be used by other data engineers in other sessions. In order to save on storage costs, the data engineer wants to avoid copying and storing physical data.

Which of the following relational objects should the data engineer create?

A. Spark SQL Table

B. View

C. Database

D. Temporary view

E. Delta Table

**Source answer: D**

Explanation

The correct answer is D. Temporary view.

Here's why:

Avoids copying and storing physical data: Temporary views are logical constructs that don't store physical data. They are defined by a query that references existing tables, so no additional storage is required.

Not needed by other data engineers in other sessions: Temporary views are session-scoped, meaning they only exist for the duration of the current Spark session and are not visible to other users or sessions.

Comparison with other options:

A. Spark SQL Table: Tables store physical data, which would incur storage costs.
B. View: While views don't store physical data, they are persistent and visible to other users/sessions, which is unnecessary for this use case.
C. Database: A database is a container for tables/views, not a relational object that pulls data from tables.
E. Delta Table: Delta tables store physical data in Delta Lake format, which would incur storage costs.

Key points:

Temporary views are ideal for session-specific transformations that don't need persistence or sharing.
They provide a cost-effective way to create relational objects without duplicating data.
The syntax in Spark SQL would be: CREATE TEMPORARY VIEW view_name AS SELECT ... FROM table1 JOIN table2 ...

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd7gpo001m01jv9exfahfk/see?quizType=REAL_EXAM&page=111

## 82. lqd-082

Which of the following describes a benefit of creating an external table from Parquet rather than CSV when using a CREATE TABLE AS SELECT statement?

A. Parquet files can be partitioned

B. CREATE TABLE AS SELECT statements cannot be used on files

C. Parquet files have a well-defined schema

D. Parquet files have the ability to be optimized

E. Parquet files will become Delta tables

**Source answer: C**

The correct answer is C because Parquet files have a well-defined schema, which is a key benefit over CSV files. CSV files are schema-less and require schema inference or explicit schema definition, while Parquet files store schema information within the file itself. This makes working with Parquet files more reliable and efficient when using CREATE TABLE AS SELECT statements.

Detailed

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd39v3001201k1t1aq4j0j/see?quizType=REAL_EXAM&page=87

## 83. lqd-083

A data engineering team has two tables. The first table march_transactions is a collection of all retail transactions in the month of March. The second table april_transactions is a collection of all retail transactions in the month of April. There are no duplicate records between the tables. Which of the following commands should be run to create a new table all_transactions that contains all records from march_transactions and april_transactions without duplicate records?

A. CREATE TABLE all_transactions AS SELECT * FROM march_transactions INNER JOIN SELECT * FROM april_transactions;

B. CREATE TABLE all_transactions AS SELECT * FROM march_transactions UNION SELECT * FROM april_transactions;

C. CREATE TABLE all_transactions AS SELECT * FROM march_transactions OUTER JOIN SELECT * FROM april_transactions;

D. CREATE TABLE all_transactions AS SELECT * FROM march_transactions INTERSECT SELECT * FROM april_transactions;

E. CREATE TABLE all_transactions AS SELECT * FROM march_transactions MERGE SELECT * FROM april_transactions;

**Source answer: B**

The UNION operator is the correct choice because:

UNION combines result sets from multiple SELECT statements into a single result set
UNION automatically removes duplicates - which is exactly what's needed since the requirement is to have all records without duplicates
The problem states there are no duplicate records between tables, but UNION ensures no duplicates even if there were

Why other options are incorrect:

A (INNER JOIN): This performs a join operation based on matching columns, not a union of all records
C (OUTER JOIN): This also performs a join operation, not a union of all records
D (INTERSECT): This returns only records that exist in BOTH tables, not all records from both tables
E (MERGE): MERGE is used for upsert operations (UPDATE/INSERT), not for combining all records from two tables

Note: In SQL, UNION ALL would keep duplicates, but UNION removes duplicates. Since the requirement is "without duplicate records," UNION is the correct choice.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9l000001jzqugt74ux/see?quizType=REAL_EXAM&page=88

## 84. lqd-084

A data analysis team has noticed that their Databricks SQL queries are running too slowly when connected to their always-on SQL endpoint. They claim that this issue is present when many members of the team are running small queries simultaneously. They ask the data engineering team for help. The data engineering team notices that each of the team's queries uses the same SQL endpoint.

Which of the following approaches can the data engineering team use to improve the latency of the team's queries?

A. They can increase the cluster size of the SQL endpoint.

B. They can increase the maximum bound of the SQL endpoint's scaling range.

C. They can turn on the Auto Stop feature for the SQL endpoint.

D. They can turn on the Serverless feature for the SQL endpoint.

E. They can turn on the Serverless feature for the SQL endpoint and change the Spot Instance Policy to "Reliability Optimized."

**Source answer: B**

✅ Why B: Increase the maximum bound of the SQL endpoint’s scaling range is correct

The problem describes many users running many small queries at the same time on the same always-on SQL endpoint.
This is a concurrency problem, not a single-query performance problem.

Databricks SQL endpoints scale horizontally, not just vertically.
Increasing the maximum scaling bound allows the endpoint to add more clusters.
More clusters = more parallel query execution, which directly reduces latency for concurrent small queries.

This matches the scenario perfectly.

❌ Why A: Increase the cluster size is not ideal
Increasing cluster size scales vertically (bigger machines).
This helps complex or heavy queries, not many small concurrent queries.
A single larger cluster can still become a bottleneck under high concurrency.
Exam takeaway 🧠
Concurrency issue → scale out (B)
Heavy/complex queries → scale up (A)

This distinction is critical for the Databricks Data Engineer Associate exam.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd3s9l000101jztk5thjl3/see?quizType=REAL_EXAM&page=88

## 85. lqd-085

A data organization leader is upset about the data analysis team’s reports being different from the data engineering team’s reports. The leader believes the siloed nature of their organization’s data engineering and data analysis architectures is to blame.

Which of the following describes how a data lakehouse could alleviate this issue?

A. Both teams would autoscale their work as data size evolves

B. Both teams would use the same source of truth for their work

C. Both teams would reorganize to report to the same department

D. Both teams would be able to collaborate on projects in real-time

E. Both teams would respond more quickly to ad-hoc requests

**Source answer: B**

A data lakehouse is designed to unify the data engineering and data analysis architectures by integrating features of both data lakes and data warehouses. One of the key benefits of a data lakehouse is that it provides a common, centralized data repository (the "lake") that serves as a single source of truth for data storage and analysis. This allows both data engineering and data analysis teams to work with the same consistent data sets, reducing discrepancies and ensuring that the reports generated by both teams are based on the same underlying data.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd3s9m000201jzz6yv31al/see?quizType=REAL_EXAM&page=88

## 86. lqd-086

Which of the following must be specified when creating a new Delta Live Tables pipeline?

A. A key-value pair configuration

B. The preferred DBU/hour cost

C. A path to cloud storage location for the written data

D. A location of a target database for the written data

E. At least one notebook library to be executed

**Source answer: E**

When creating a new Delta Live Tables pipeline, the only mandatory requirement is to specify at least one notebook library to be executed. This notebook contains the pipeline logic and transformations. The other options are either optional or not required:

A. A key-value pair configuration: Optional - configurations can be set but are not mandatory
B. The preferred DBU/hour cost: Not required - cost management is handled differently
C. A path to cloud storage location for the written data: Optional - storage locations can be configured but have defaults
D. A location of a target database for the written data: Optional - database locations can be configured but have defaults

According to Databricks documentation, the minimum requirement is to specify at least one notebook library that contains the pipeline code to be executed.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd3s9m000401jzoohczzv0/see?quizType=REAL_EXAM&page=88

## 87. lqd-087

A data engineer is using the following code block as part of a batch ingestion pipeline to read from a composable table:

transactions_df = (spark.read
    .schema(schema)
    .format("delta")
    .table("transactions")
)


Which of the following changes needs to be made so this code block will work when the transactions table is a stream source?

A. Replace predict with a stream-friendly prediction function

B. Replace schema(schema) with option ("maxFilesPerTrigger", 1)

C. Replace "transactions" with the path to the location of the Delta table

D. Replace format("delta") with format("stream")

E. Replace spark.read with spark.readStream

**Source answer: E**

Explanation

To read from a Delta table as a streaming source in Databricks, you need to use spark.readStream instead of spark.read. The spark.readStream API is specifically designed for streaming data sources and provides the necessary functionality for incremental processing.

Key Points:

spark.readStream vs spark.read:

spark.read is for batch processing (reading data once)
spark.readStream is for streaming processing (reading data incrementally)

Other options analysis:

Option A: Incorrect - There's no predict function in the code, and this is unrelated to streaming
Option B: Incorrect - maxFilesPerTrigger is an optional configuration for controlling micro-batch size, not required for basic streaming
Option C: Incorrect - You can stream from a Delta table using its name (table("transactions")) without needing the path
Option D: Incorrect - format("delta") is correct for Delta tables; there's no format("stream")

Correct streaming code:

transactions_df = (spark.readStream
    .schema(schema)
    .format("delta")
    .table("transactions")
)


This change enables the code to read from the Delta table as a streaming source, processing new data as it arrives.

Source copies: 3; distinct source versions: 3.

Source: https://www.leetquiz.com/quiz/cmkcd7gpr002501jvjv7326ln/see?quizType=REAL_EXAM&page=113

## 88. lqd-088

A data engineer needs to use a Delta table as part of a data pipeline, but they do not know if they have the appropriate permissions. In which of the following locations can the data engineer review their permissions on the table?

A. Databricks Filesystem

B. Jobs

C. Dashboards

D. Repos

E. Data Explorer

**Source answer: E**

Explanation

In Databricks, the Data Explorer is the correct location to review permissions on Delta tables. Here's why:

Data Explorer is Databricks' interface for browsing and managing data assets including tables, views, and databases.

Within Data Explorer, you can:

Navigate to specific tables
View table details and metadata
Check and manage permissions through the Permissions tab
See what access rights you have (SELECT, MODIFY, CREATE, etc.)

The other options are incorrect because:

Databricks Filesystem (DBFS): Used for file storage, not for table permission management
Jobs: Interface for creating and managing job workflows
Dashboards: For creating and viewing data visualizations and reports
Repos: For version control and collaborative development

Best Practice: When working with Delta tables in Databricks, always check Data Explorer to verify your permissions before attempting operations that might fail due to insufficient privileges.

Note: The answer provided in the source text (E) is correct.

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9n000b01jzb43usplh/see?quizType=REAL_EXAM&page=89

## 89. lqd-089

A data engineer has been using a Databricks SQL dashboard to monitor the cleanliness of the input data to an ELT job. The ELT job has its Databricks SQL query that returns the number of input records containing unexpected NULL values. The data engineer wants their entire team to be notified via a messaging webhook whenever this value reaches 100. Which of the following approaches can the data engineer use to notify their entire team via a messaging webhook whenever the number of NULL values reaches 100?

A. They can set up an Alert with a custom template.

B. They can set up an Alert with a new email alert destination.

C. They can set up an Alert with a new webhook alert destination.

D. They can set up an Alert with one-time notifications.

E. They can set up an Alert without notifications.

**Source answer: C**

To achieve this, the data engineer can set up an Alert in the Databricks workspace that triggers when the query results exceed the threshold of 100 NULL values. They can create a new webhook alert destination in the Alert's configuration settings and provide the necessary messaging webhook URL to receive notifications. When the Alert is triggered, it will send a message to the configured webhook URL, which will then notify the entire team of the issue.

Source copies: 9; distinct source versions: 9.

Source: https://www.leetquiz.com/quiz/cmkcd3s9n000d01jz6ssrre17/see?quizType=REAL_EXAM&page=89

## 90. lqd-090

A data engineer has a Python variable table_name that they would like to use in a SQL query. They want to construct a Python code block that will run the query using table_name. They have the following incomplete code block:

(f"SELECT customer_id, spend FROM {table_name}")


Which of the following can be used to fill in the blank to successfully complete the task?

A. spark.delta.sql

B. spark.delta.table

C. spark.table

D. dbutils.sql

E. spark.sql

**Source answer: E**

The correct answer is spark.sql because:

spark.sql() is the primary method in PySpark for executing SQL queries in Databricks.
The code block shows an f-string that constructs a SQL query with the table_name variable interpolated.
The syntax should be: spark.sql(f"SELECT customer_id, spend FROM {table_name}")

Why other options are incorrect:

A. spark.delta.sql: This method doesn't exist in the Databricks/Spark API.
B. spark.delta.table: This is used for Delta table operations, not for executing SQL queries.
C. spark.table: This method is used to create a DataFrame from a table, not to execute SQL queries.
D. dbutils.sql: dbutils doesn't have a .sql method; SQL execution is done through spark.sql().

Key Concept: In Databricks, spark.sql() is the standard way to execute SQL queries from Python code, and it supports string interpolation using f-strings or other string formatting methods.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd3s9o000h01jz286mgjfk/see?quizType=REAL_EXAM&page=90

## 91. lqd-091

A data engineer has been given a new record of data:

id STRING = 'a1'
rank INTEGER = 6 rating FLOAT = 9.4


Which of the following SQL commands can be used to append the new record to an existing Delta table my_table?

A. INSERT INTO my_table VALUES ('a1', 6, 9.4)

B. my_table UNION VALUES ('a1', 6, 9.4)

C. INSERT VALUES ('a1', 6, 9.4) INTO my_table

D. UPDATE my_table VALUES ('a1', 6, 9.4)

E. UPDATE VALUES ('a1', 6, 9.4) my_table

**Source answer: A**

Explanation

Correct Answer: A

Why Option A is correct:

INSERT INTO table_name VALUES (...) is the standard SQL syntax for inserting new records into a table.
The syntax correctly specifies the table name (my_table) and provides the values in the correct order matching the table's column structure.
This command will append the new record to the existing Delta table.

Why other options are incorrect:

Option B: my_table UNION VALUES ('a1', 6, 9.4)

This is not valid SQL syntax for inserting data. UNION is used to combine results of SELECT statements, not for inserting data.
Even if used with SELECT, it would create a new result set but not modify the table.

Option C: INSERT VALUES ('a1', 6, 9.4) INTO my_table

This has incorrect syntax. The correct order is INSERT INTO table_name VALUES (...).
Some database systems might support this syntax, but it's not standard SQL and not guaranteed to work in Databricks/Spark SQL.

Option D: UPDATE my_table VALUES ('a1', 6, 9.4)

UPDATE is used to modify existing records, not to insert new ones.
The syntax is incorrect for UPDATE statements, which require SET clause to specify column updates.

Option E: UPDATE VALUES ('a1', 6, 9.4) my_table

This is completely invalid SQL syntax for any operation.
UPDATE statements require a SET clause and typically a WHERE clause to identify which rows to update.

Key Learning Points:

Use INSERT INTO table_name VALUES (...) to append new records to a table.
Ensure the values are provided in the correct order matching the table's column definitions.
UPDATE is for modifying existing records, not for inserting new ones.
Always use standard SQL syntax for compatibility across different SQL implementations.

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9o000i01jzhzucjmk4/see?quizType=REAL_EXAM&page=90

## 92. lqd-092

A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE. The table is configured to run in Development mode using the Continuous Pipeline Mode. Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline?

A. All datasets will be updated once and the pipeline will shut down

B. The compute resources will be terminated.

C. All datasets will be updated at set intervals until the pipeline is shut down

D. The compute resources will persist until the pipeline is shut down.

E. All datasets will be updated once and the pipeline will persist without any processing

F. The compute resources will persist but go unused.

**Source answer: E**

In Delta Live Tables Development mode with Continuous Pipeline Mode:

Development Mode Behavior: When running in development mode, Delta Live Tables reuses clusters to avoid restart overhead and disables pipeline retries for immediate error detection.

Continuous Pipeline Mode: This mode is designed for streaming workloads where data is continuously processed. However, in development mode, the behavior differs from production mode.

Key Difference: In development mode with continuous pipeline mode, the pipeline will:

Process all available data once
Then persist without further processing (unlike production mode which would continue processing)
The compute resources remain available for additional testing and development

Why not other options:

A/G: The pipeline doesn't shut down completely - it persists for testing
B: Compute resources are not terminated in development mode
C/I: In development mode, datasets are not updated at set intervals continuously
D: While compute persists, the pipeline doesn't shut down
F/H/J: These don't accurately describe the complete behavior

This behavior allows developers to test their pipelines without incurring continuous compute costs while maintaining resources for iterative development.

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9o000k01jzxgl273au/see?quizType=REAL_EXAM&page=90

## 93. lqd-093

A data engineer has a Job with multiple tasks that runs nightly. Each of the tasks runs slowly because the clusters take a long time to start. Which of the following actions can the data engineer perform to improve the start up time for the clusters used for the Job?

A. They can use endpoints available in Databricks SQL

B. They can use jobs clusters instead of all-purpose clusters

C. They can configure the clusters to be single-node

D. They can use clusters that are from a cluster pool

E. They can configure the clusters to autoscale for larger data sizes

**Source answer: D**

Correct Answer: D

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9p000o01jzi7w36l7o/see?quizType=REAL_EXAM&page=91

## 94. lqd-094

A data engineer has joined an existing project and they see the following query in the project repository:

CREATE STREAMING LIVE TABLE loyal_customers AS SELECT customer_id -
FROM STREAM(LIVE.customers) WHERE loyalty_level = 'high';


Which of the following describes why the STREAM function is included in the query?

A. The STREAM function is not needed and will cause an error.

B. The table being created is a live table.

C. The customers table is a streaming live table.

D. The customers table is a reference to a Structured Streaming query on a PySpark DataFrame.

E. The data in the customers table has been updated since its last run.

**Source answer: C**

The STREAM function is used in Databricks SQL to indicate that the source table is a streaming live table. When you use STREAM(LIVE.customers), it means that the customers table is a streaming live table, and you're reading from it as a streaming source. This is necessary when creating a streaming live table that depends on another streaming live table as its source.

Key points:

STREAM() function is used to read from streaming live tables
The query creates a new streaming live table (CREATE STREAMING LIVE TABLE)
The source customers table must be a streaming live table for this syntax to work
This enables incremental processing where the new table will update as new data arrives in the source table

Option A is incorrect because the STREAM function is needed and valid. Option B is incorrect because while the table being created is a live table, that doesn't explain why STREAM is needed. Option D is incorrect because the STREAM function refers to a streaming live table, not a PySpark DataFrame reference. Option E is incorrect because the STREAM function is not related to whether data has been updated.

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd3s9p000q01jzkqksgtfg/see?quizType=REAL_EXAM&page=91

## 95. lqd-095

A single Job runs two notebooks as two separate tasks. A data engineer has noticed that one of the notebooks is running slowly in the Job's current run. The data engineer asks a tech lead for help in identifying why this might be the case. Which of the following approaches can the tech lead use to identify why the notebook is running slowly as part of the Job?

A. They can navigate to the Runs tab in the Jobs UI to immediately review the processing notebook.

B. They can navigate to the Tasks tab in the Jobs UI and click on the active run to review the processing notebook.

C. They can navigate to the Runs tab in the Jobs UI and click on the active run to review the processing notebook.

D. There is no way to determine why a Job task is running slowly.

E. They can navigate to the Tasks tab in the Jobs UI to immediately review the processing notebook.

**Source answer: C**

Explanation

In Databricks, when you need to investigate why a notebook is running slowly as part of a Job, you should:

Navigate to the Runs tab in the Jobs UI - This shows all the runs of the job
Click on the active run - This allows you to see the details of the current execution
Review the processing notebook - From there, you can access the notebook execution details, logs, and metrics to identify performance issues

Why option C is correct:

The Runs tab shows all job executions (historical and current)
Clicking on the active run gives you access to the specific execution details
You can then examine the notebook's execution, view logs, check cluster metrics, and identify bottlenecks

Why other options are incorrect:

A: You cannot "immediately review" from the Runs tab without clicking on the specific run
B: The Tasks tab shows task configurations, not active run details for troubleshooting performance
D: This is incorrect - Databricks provides extensive monitoring and debugging capabilities
E: You cannot "immediately review" from the Tasks tab; you need to navigate to the specific run

Key Databricks UI Navigation:

Jobs → Select your job → Runs tab → Click on active run → View task details and logs
From there, you can access Spark UI, driver logs, and notebook execution details to diagnose performance issues.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75nt000301jwc0e4ekie/see?quizType=REAL_EXAM&page=92

## 96. lqd-096

A data engineer has a single-task Job that runs each morning before they begin working. After identifying an upstream data issue, they need to set up another task to run a new notebook prior to the original task. Which of the following approaches can the data engineer use to set up the new task?

A. They can clone the existing task in the existing Job and update it to run the new notebook.

B. They can create a new task in the existing Job and then add it as a dependency of the original task.

C. They can create a new task in the existing Job and then add the original task as a dependency of the new task.

D. They can create a new job from scratch and add both tasks to run concurrently.

E. They can clone the existing task to a new Job and then edit it to run the new notebook.

**Source answer: B**

Explanation

The correct answer is B because:

Requirement: The data engineer needs to run a new notebook prior to the original task. This means the new task should execute first, followed by the original task.

Task Dependencies in Databricks Jobs: In Databricks, you can set up task dependencies where one task must complete before another starts. When you add a task as a dependency of another task, the dependent task will wait for the upstream task to complete.

Option B Analysis: "They can create a new task in the existing Job and then add it as a dependency of the original task." This means:

Create a new task for the new notebook
Make this new task a dependency of the original task
Result: New task runs first → Original task runs after new task completes

Why other options are incorrect:

A: Cloning the existing task doesn't create a proper dependency chain
C: This would make the original task run first (opposite of what's needed)
D: Creating a new job from scratch is unnecessary and doesn't maintain the existing scheduling
E: Cloning to a new job creates separate jobs without proper coordination

Best Practice: Adding tasks with dependencies in the same job maintains the existing scheduling configuration and ensures proper execution order.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75nt000501jwj7u1xva7/see?quizType=REAL_EXAM&page=92

## 97. lqd-097

A dataset has been defined using Delta Live Tables and includes an expectations clause:

CONSTRAINT valid_timestamp EXPECT (timestamp > '2020-01-01') ON VIOLATION DROP ROW


What is the expected behavior when a batch of data containing data that violates these constraints is processed?

A. Records that violate the expectation are dropped from the target dataset and loaded into a quarantine table.

B. Records that violate the expectation are added to the target dataset and flagged as invalid in a field added to the target dataset.

C. Records that violate the expectation are dropped from the target dataset and recorded as invalid in the event log.

**Source answer: C**

Explanation

In Delta Live Tables (DLT), when you define a constraint with ON VIOLATION DROP ROW, the behavior is:

Records that violate the constraint are dropped from the target dataset - they are not included in the final output table.
The violation is recorded in the event log - DLT tracks these violations for monitoring and debugging purposes.
No quarantine table is automatically created - Option A is incorrect because DLT doesn't automatically load dropped rows into a quarantine table unless explicitly configured to do so.
Records are not added with flags - Option B is incorrect because the DROP ROW action specifically removes the rows, rather than adding them with flags.

Key Points:

ON VIOLATION DROP ROW means violating rows are excluded from the target dataset
Violations are logged in the DLT event log for observability
This is different from ON VIOLATION FAIL UPDATE which would fail the pipeline, or custom handling that might route to quarantine tables
The event log provides visibility into data quality issues without storing the bad data in the main dataset

Source copies: 6; distinct source versions: 6.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75nu000801jwg4yek4l1/see?quizType=REAL_EXAM&page=93

## 98. lqd-098

A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table. The code block used by the data engineer is below:

(spark.table("sales")
.withcolumn("avg_price", col("sales")/ col("units"))
.writestream
.option("checkpointLocation", checkpointpath)
.outputMode("complete")
_____
.table("new_sales"))


If the data engineer only wants the query to execute a micro-batch to process data every 5 seconds, which of the following lines of code should the data engineer use to fill in the blank?

A. trigger("5 seconds")

B. trigger()

C. trigger(once="5 seconds")

D. trigger(processingTime="5 seconds")

E. trigger(continuous="5 seconds")

**Source answer: D**

Explanation

In Apache Spark Structured Streaming, the trigger() method is used to specify how often the streaming query should process data. There are three main trigger types:

ProcessingTime trigger: Processes data at fixed time intervals (micro-batches)
Once trigger: Processes all available data once and then stops
Continuous trigger: Processes data continuously (experimental feature)

For this question, the data engineer wants to execute a micro-batch every 5 seconds. The correct syntax for a processing time trigger is:

trigger(processingTime="5 seconds")


Let's analyze each option:

A. trigger("5 seconds"): This is incorrect because the trigger method requires specifying the trigger type explicitly.
B. trigger(): This would use the default trigger (which processes data as soon as possible), not every 5 seconds.
C. trigger(once="5 seconds"): This is incorrect syntax for the once trigger. The once trigger doesn't take a time parameter.
D. trigger(processingTime="5 seconds"): CORRECT - This specifies a processing time trigger that executes micro-batches every 5 seconds.
E. trigger(continuous="5 seconds"): This is incorrect syntax for continuous trigger. Continuous trigger uses trigger(continuous="1 second") format, but this would process data continuously, not in micro-batches every 5 seconds.

Key Points:

processingTime trigger is used for fixed-interval micro-batch processing
The time interval can be specified as a string like "5 seconds", "1 minute", etc.
This trigger ensures the query processes data in micro-batches at the specified interval, which is exactly what the data engineer needs.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75nu000901jwml6mnhie/see?quizType=REAL_EXAM&page=93

## 99. lqd-099

Which of the following tools is used by Auto Loader process data incrementally?

A. Checkpointing

B. Spark Structured Streaming

C. Data Explorer

**Source answer: B**

Explanation

Auto Loader uses Spark Structured Streaming to process data incrementally. Here's why:

Key Points:

Auto Loader Architecture: Auto Loader is built on top of Spark Structured Streaming, which provides the incremental processing capabilities.

How Auto Loader Works:

Auto Loader monitors cloud storage locations for new files
It uses Structured Streaming's micro-batch processing to incrementally load new data
The process tracks which files have been processed using checkpointing

Checkpointing Role: While checkpointing (Option A) is used by Auto Loader to track processed files and maintain state, it's not the primary tool for incremental processing. Checkpointing is a supporting mechanism.

Data Explorer: This is a Databricks tool for exploring and visualizing data, not related to incremental data processing.

Correct Answer: B. Spark Structured Streaming - This is the underlying engine that enables Auto Loader's incremental processing capabilities.

Additional Context:

Auto Loader provides optimized file discovery and schema inference on top of Structured Streaming
It's designed specifically for incremental data ingestion from cloud storage
The incremental processing happens through Structured Streaming's micro-batch architecture

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75nu000a01jw2wwocma3/see?quizType=REAL_EXAM&page=93

## 100. lqd-100

Which of the following describes the relationship between Gold tables and Silver tables?

A. Gold tables are more likely to contain aggregations than Silver tables.

B. Gold tables are more likely to contain valuable data than Silver tables.

C. Gold tables are more likely to contain a less refined view of data than Silver tables.

D. Gold tables are more likely to contain more data than Silver tables.

E. Gold tables are more likely to contain truthful data than Silver tables.

**Source answer: A**

Explanation

In the Databricks Lakehouse architecture, data flows through different layers with increasing levels of refinement:

Bronze Layer: Raw data ingestion
Silver Layer: Cleaned, validated, and enriched data
Gold Layer: Business-level aggregated data ready for consumption

Why option A is correct:

Gold tables typically contain aggregated, summarized, and business-ready data
They are designed for consumption by business users, analysts, and reporting tools
Aggregations in Gold tables include metrics like daily sales totals, customer lifetime value, or other business KPIs

Why other options are incorrect:

B: Both Silver and Gold tables contain valuable data, but Gold tables are specifically structured for business consumption
C: Gold tables contain a MORE refined view of data than Silver tables (not less)
D: Gold tables typically contain LESS data than Silver tables because they store aggregated/summarized data
E: Both layers should contain truthful data; Silver tables contain validated/cleaned data, while Gold tables contain aggregated business metrics

The key distinction is that Gold tables represent the final, business-ready layer with aggregated data optimized for consumption, while Silver tables contain cleaned and enriched data that serves as the foundation for creating Gold tables.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75nv000c01jwp0vwm571/see?quizType=REAL_EXAM&page=93

## 101. lqd-101

A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE. The table is configured to run in Production mode using the Continuous Pipeline Mode. Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline?

A. All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will persist to allow for additional testing.

B. All datasets will be updated once and the pipeline will persist without any processing. The compute resources will persist but go unused.

C. All datasets will be updated at set intervals until the pipeline is shut down. The compute resources will be deployed for the update and terminated when the pipeline is stopped.

D. All datasets will be updated once and the pipeline will shut down. The compute resources will be terminated.

E. All datasets will be updated once and the pipeline will shut down. The compute resources will persist to allow for additional testing.

**Source answer: C**

Explanation

In Delta Live Tables (DLT), when a pipeline is configured with Continuous Pipeline Mode in Production mode:

Continuous Processing: The pipeline will continuously process data at set intervals, not just once.
Compute Resource Management: In Production mode, compute resources are deployed for the duration of the pipeline run and terminated when the pipeline is stopped.

Key points:

STREAMING LIVE TABLE definitions process streaming data continuously
LIVE TABLE definitions process batch data at each interval
Continuous Pipeline Mode means the pipeline runs continuously, not just once
Production mode optimizes for cost efficiency by terminating compute resources when not in use

Option C correctly describes:

All datasets will be updated at set intervals (continuous processing)
Compute resources will be deployed for updates and terminated when pipeline is stopped (Production mode behavior)

Other options are incorrect because:

Options D and E suggest the pipeline runs only once, which is incorrect for Continuous mode
Options A and B suggest compute resources persist indefinitely, which is not how Production mode works
Option B suggests the pipeline persists without processing, which contradicts Continuous mode

Therefore, option C is the correct answer.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75nv000e01jwio2ofczc/see?quizType=REAL_EXAM&page=93

## 102. lqd-102

A data engineer wants to create a data entity from a couple of tables. The data entity must be used by other data engineers in other sessions. It also must be saved to a physical location. Which of the following data entities should the data engineer create?

A. Database

B. Function

C. View

D. Temporary view

E. Table

**Source answer: E**

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd75nw000g01jwn8gid0i7/see?quizType=REAL_EXAM&page=94

## 103. lqd-103

USING ____

OPTIONS ( url "jdbc:sqlite:/customers.db", dbtable "customer360" )

Which of the following lines of code fills in the above blank to successfully complete the task?

A. org.apache.spark.sql.jdbc

B. autoloader

C. DELTA

D. sqlite

E. org.apache.spark.sql.sqlite

**Source answer: A**

Explanation

The correct answer is A. org.apache.spark.sql.jdbc.

Why this is correct:
The code snippet shows a JDBC connection string with jdbc:sqlite:/customers.db - this indicates a JDBC connection to a SQLite database.
In Spark SQL, when reading from JDBC sources, you use the format org.apache.spark.sql.jdbc or simply jdbc.
The syntax should be: USING org.apache.spark.sql.jdbc or USING jdbc.
Why other options are incorrect:
B. autoloader: Auto Loader is for streaming file ingestion, not JDBC connections.
C. DELTA: Delta format is for Delta Lake tables, not JDBC connections.
D. sqlite: This is not a valid Spark format; Spark doesn't have a native sqlite format.
E. org.apache.spark.sql.sqlite: This format doesn't exist in Spark; JDBC connections use the jdbc format.
Complete code would look like:
USING org.apache.spark.sql.jdbc
OPTIONS (
  url "jdbc:sqlite:/customers.db",
  dbtable "customer360"
)


Or the simplified version:

USING jdbc
OPTIONS (
  url "jdbc:sqlite:/customers.db",
  dbtable "customer360"
)


This code would create a DataFrame by reading from a SQLite database using JDBC driver.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75nw000k01jwwzkb1025/see?quizType=REAL_EXAM&page=94

## 104. lqd-104

A data engineer runs a statement every day to copy the previous day's sales into the table transactions. Each day's sales are in their own file in the location "/transactions/raw". Today, the data engineer runs the following command to complete this task:

COPY INTO transactions
FROM "/transactions/raw"
FILEFORMAT = PARQUET;


After running the command today, the data engineer notices that the number of records in table transactions has not changed. Which of the following describes why the statement might not have copied any new records into the table?

A. The format of the files to be copied were not included with the FORMAT_OPTIONS keyword.

B. The names of the files to be copied were not included with the FILES keyword.

C. The previous day's file has already been copied into the table.

D. The PARQUET file format does not support COPY INTO.

E. The COPY INTO statement requires the table to be refreshed to view the copied rows.

**Source answer: C**

The COPY INTO command in Databricks is designed to be idempotent - it tracks which files have already been copied and will not re-copy them. When the data engineer runs the same COPY INTO statement daily, it will only copy new files that haven't been processed before. If the previous day's file was already copied in a previous run, the command will not copy it again, resulting in no change to the record count.

Key points:

COPY INTO maintains metadata about which files have been processed
It automatically skips files that have already been copied
This prevents duplicate data from being loaded
The other options are incorrect:
A: FILEFORMAT = PARQUET is sufficient for Parquet files
B: FILES keyword is optional; COPY INTO can process all files in a directory
D: PARQUET file format is fully supported by COPY INTO
E: No refresh is needed; changes are immediately visible

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd75nx000l01jwzvl3tl74/see?quizType=REAL_EXAM&page=94

## 105. lqd-105

Which of the following benefits is provided by the array functions from Spark SQL?

A. An ability to work with data in a variety of types at once

B. An ability to work with data within certain partitions and windows

C. An ability to work with time-related data in specified intervals

D. An ability to work with complex, nested data ingested from JSON files

E. An ability to work with an array of tables for procedural automation

**Source answer: D**

Explanation

Array functions in Spark SQL are specifically designed to work with complex, nested data structures, particularly arrays. This is especially useful when dealing with data ingested from JSON files, which often contain nested arrays and complex data structures.

Why D is correct:

JSON files frequently contain nested arrays and complex data structures
Spark SQL array functions (like explode(), array_contains(), array_distinct(), etc.) allow you to manipulate and query these nested arrays
These functions enable you to flatten arrays, filter array elements, and perform operations on array contents

Why other options are incorrect:

A: Working with data in a variety of types at once is more about union operations or type casting, not specifically array functions
B: Working with data within partitions and windows is handled by window functions and partitioning, not array functions
C: Working with time-related data is handled by date/time functions, not array functions
E: Working with an array of tables for procedural automation is not a standard Spark SQL array function capability; this would be more about programmatic table operations

Array functions are essential for processing semi-structured data formats like JSON, where arrays are a common data structure.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75nx000p01jwt8d8f182/see?quizType=REAL_EXAM&page=95

## 106. lqd-106

A data engineer needs to apply custom logic to string column city in table stores for a specific use case. In order to apply this custom logic at scale, the data engineer wants to create a SQL user-defined function (UDF). Which of the following code blocks creates this SQL UDF?

A. CREATE FUNCTION combine_nyc (city STRING)
RETURNS STRING
RETURN CASE
    WHEN city = "brooklyn" THEN "new york"
    ELSE city
END;


B. CREATE UDF combine_nyc(city STRING)
RETURNS STRING
CASE
    WHEN city = "brooklyn" THEN "new york"
    ELSE city




(Note: Option B is incomplete and syntactically incorrect for standard SQL UDF creation.)

**Source answer: A**

Explanation

Option A is the correct syntax for creating a SQL user-defined function (UDF) in Databricks:

Correct Syntax: CREATE FUNCTION is the proper SQL command to create a user-defined function.
Parameter Definition: (city STRING) correctly defines the input parameter.
Return Type: RETURNS STRING properly specifies the return type.
Function Body: The RETURN CASE...END; structure correctly implements the function logic.
Complete Statement: The statement ends with a semicolon, making it syntactically complete.

Option B is incorrect because:

Wrong Command: Uses CREATE UDF instead of CREATE FUNCTION.
Incomplete Syntax: Missing the RETURN keyword before the CASE statement.
Missing END: The CASE statement doesn't have an END keyword.
Missing Semicolon: The statement is incomplete without a closing semicolon.

In Databricks SQL, user-defined functions are created using the CREATE FUNCTION syntax, which allows you to define reusable SQL logic that can be applied at scale across multiple queries and tables.

Source copies: 3; distinct source versions: 3.

Source: https://www.leetquiz.com/quiz/cmkcd75nx000n01jwrfjoq745/see?quizType=REAL_EXAM&page=95

## 107. lqd-107

A data engineer has left the organization. The data team needs to transfer ownership of the data engineer's Delta tables to a new data engineer. The new data engineer is the lead engineer on the data team. Assuming the original data engineer no longer has access, which of the following individuals must be the one to transfer ownership of the Delta tables in Data Explorer?

A. Databricks account representative

B. This transfer is not possible

C. Workspace administrator

D. New lead data engineer

**Source answer: C**

Explanation

In Databricks, when a user leaves the organization and no longer has access, the workspace administrator is the appropriate individual to transfer ownership of Delta tables. Here's why:

Workspace Administrator Role: Workspace administrators have elevated privileges that allow them to manage user permissions and object ownership within the workspace.

Data Explorer Ownership Transfer: In Data Explorer, ownership of Delta tables can be transferred by:

The current owner of the table
A workspace administrator
Users with appropriate permissions (like MODIFY on the table)

Scenario Constraints: Since the original data engineer no longer has access, they cannot perform the transfer. The new lead data engineer cannot transfer ownership because they don't own the tables yet.

Account Representative vs Workspace Administrator:

Databricks account representatives manage account-level settings and billing, not workspace-level object ownership.
Workspace administrators manage workspace-level resources, including user permissions and object ownership.

Transfer is Possible: The transfer is indeed possible through workspace administrator intervention, making option B incorrect.

Correct Answer: C - Workspace administrator

Key Takeaway: In Databricks governance scenarios, workspace administrators serve as the fallback for ownership transfers when original owners are unavailable, ensuring business continuity and data governance compliance.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75ny000t01jwh3oxzulr/see?quizType=REAL_EXAM&page=96

## 108. lqd-108

A data engineer needs to determine whether to use the built-in Databricks Notebooks versioning or version their project using Databricks Repos. Which of the following is an advantage of using Databricks Repos over the Databricks Notebooks versioning?

A. Databricks Repos automatically saves development progress

B. Databricks Repos supports the use of multiple branches

C. Databricks Repos allows users to revert to previous versions of a notebook

D. Databricks Repos provides the ability to comment on specific changes

E. Databricks Repos is wholly housed within the Databricks Lakehouse Platform

**Source answer: B**

Explanation

Correct Answer: B - Databricks Repos supports the use of multiple branches

Why this is correct:

Multiple Branch Support: Databricks Repos integrates with Git repositories, which inherently support branching. This allows data engineers to:

Create feature branches for new development
Maintain stable main/master branches for production code
Create release branches for specific versions
Collaborate effectively using Git workflows

Comparison with Built-in Notebooks Versioning:

Built-in Databricks Notebooks versioning provides basic version history and the ability to revert to previous versions
However, it lacks Git integration and doesn't support branching workflows
Built-in versioning is more like a simple revision history system

Why other options are incorrect:

A: Both Databricks Notebooks versioning and Databricks Repos automatically save development progress. This is not a distinguishing advantage.

C: Both systems allow users to revert to previous versions of a notebook. Built-in versioning provides this functionality through the notebook's revision history.

D: Commenting on specific changes is typically a feature of Git platforms (like GitHub, GitLab, Bitbucket) rather than Databricks Repos itself. Databricks Repos provides Git integration but doesn't inherently provide code review/commenting features within the Databricks interface.

E: Both Databricks Notebooks versioning and Databricks Repos are housed within the Databricks Lakehouse Platform, so this is not a distinguishing advantage.

Key Takeaway: The primary advantage of Databricks Repos over built-in notebook versioning is its Git integration, which enables proper version control workflows including branching, merging, and collaboration through external Git repositories.

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd75ny000u01jwhi675597/see?quizType=REAL_EXAM&page=96

## 109. lqd-109

Which of the following Git operations must be performed outside of Databricks Repos?

A. Commit

B. Pull

C. Push

D. Clone

E. Merge

**Source answer: E**

The correct answer is E. Merge.

Databricks Repos provides integrated Git functionality for many common operations, but there are limitations:

Commit - Can be performed within Databricks Repos
Pull - Can be performed within Databricks Repos
Push - Can be performed within Databricks Repos
Clone - Can be performed within Databricks Repos (you can clone repositories directly into Databricks)
Merge - Cannot be performed within Databricks Repos. Merge operations must be performed outside of Databricks, typically using Git command line or other Git tools.


Databricks Repos supports basic Git operations for version control, but more complex operations like merging branches require external Git tools. This is because Databricks Repos is designed for collaborative development and version control of notebooks and other workspace objects, but doesn't include all the advanced Git features available in full Git clients.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 3; distinct source versions: 3.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75ny000w01jwvu3jzns6/see?quizType=REAL_EXAM&page=96

## 110. lqd-110

Which of the following describes the storage organization of a Delta table?

A. Delta tables are stored in a single file that contains data, history, metadata, and other attributes.

B. Delta tables store their data in a single file and all metadata in a collection of files in a separate location.

C. Delta tables are stored in a collection of files that contain data, history, metadata, and other attributes.

D. Delta tables are stored in a collection of files that contain only the data stored within the table.

E. Delta tables are stored in a single file that contains only the data stored within the table.

**Source answer: C**

Explanation

Delta tables use a storage organization where data is stored in Parquet files, and metadata is stored in JSON files in the _delta_log directory. This creates a collection of files that work together to provide ACID transactions, time travel, and other Delta Lake features.

Key points about Delta table storage:

Data files: Stored as Parquet files containing the actual table data
Transaction log: Stored as JSON files in the _delta_log directory, containing:
Metadata about the table schema
Transaction history
File statistics
Version information
Checkpoint files: Periodic snapshots of the transaction log for faster access

Why other options are incorrect:

A: Incorrect - Delta tables are not stored in a single file; they use multiple files
B: Incorrect - Data is not stored in a single file; it's distributed across multiple Parquet files
D: Incorrect - The collection of files includes more than just data; it includes metadata and transaction logs
E: Incorrect - Delta tables are not single files and contain more than just data

This distributed file organization enables Delta Lake's key features like ACID transactions, scalable metadata handling, and efficient time travel capabilities.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75nz000z01jwsmlkbuzr/see?quizType=REAL_EXAM&page=96

## 111. lqd-111

Which of the following is hosted completely in the control plane of the classic-Databricks architecture?

A. Worker node

B. JDBC data source

C. Databricks web application

D. Databricks Filesystem

E. Driver node

**Source answer: C**

In the classic Databricks architecture, the control plane includes the Databricks web application, which is hosted completely in the control plane. The control plane manages and orchestrates the Databricks workspace, while the data plane (also called the compute plane) includes worker nodes, driver nodes, and the Databricks Filesystem (DBFS). JDBC data sources are external data sources and not part of the Databricks architecture itself.

Key points:

Control Plane: Manages workspace, user interfaces, job scheduling, and cluster management
Data Plane: Contains the actual compute resources (driver and worker nodes) and storage (DBFS)
Databricks web application: The user interface for interacting with Databricks, hosted in the control plane
Worker node & Driver node: Part of the data plane where Spark computations run
Databricks Filesystem (DBFS): Distributed file system in the data plane
JDBC data source: External data source, not part of Databricks architecture

Source copies: 7; distinct source versions: 7.

Source: https://www.leetquiz.com/quiz/cmkcd75nz001101jwsk0hakcp/see?quizType=REAL_EXAM&page=97

## 112. lqd-112

A data engineer has realized that the data files associated with a Delta table are incredibly small. They want to compact the small files to form larger files to improve performance. Which of the following keywords can be used to compact the small files?

A. REDUCE

B. OPTIMIZE

C. COMPACTION

D. REPARTITION

E. VACUUM

**Source answer: B**

Explanation

In Databricks Delta Lake, the OPTIMIZE command is used to compact small files into larger files to improve query performance. Here's why:

OPTIMIZE: This command performs file compaction (also known as bin-packing) on Delta tables. It merges small files into larger ones, which improves read performance by reducing the number of files that need to be read during queries.

Why other options are incorrect:

REDUCE: Not a valid Delta Lake command for file compaction
COMPACTION: While conceptually related, this is not the actual command name in Delta Lake
REPARTITION: This is a Spark transformation that redistributes data across partitions, but it doesn't specifically compact existing small files in a Delta table
VACUUM: This command removes old files that are no longer referenced by the Delta table (files older than the retention period), but it doesn't compact small files

How to use OPTIMIZE:

OPTIMIZE table_name


Or with Z-ordering:

OPTIMIZE table_name
ZORDER BY column_name

Benefits:
Reduces the number of files to read
Improves query performance
Can be combined with Z-ordering for better data skipping

The OPTIMIZE command is specifically designed for this purpose in Delta Lake, making it the correct choice for compacting small files to improve performance.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75o0001a01jw0jmffuqd/see?quizType=REAL_EXAM&page=98

## 113. lqd-113

In which of the following file formats is data from Delta Lake tables primarily stored?

A. Delta

B. CSV

C. Parquet

**Source answer: C**

Explanation

Delta Lake tables store data primarily in Parquet format. Here's why:

Delta Lake is built on top of Parquet: Delta Lake is a storage layer that sits on top of Parquet files, adding ACID transactions, schema enforcement, and time travel capabilities.

Parquet as the underlying format: All data in Delta Lake tables is stored in Parquet files, which are:

Columnar storage format
Highly efficient for analytics workloads
Compressed for storage optimization
Supports predicate pushdown for faster queries

Delta adds metadata: While the actual data is stored in Parquet files, Delta Lake adds:

A transaction log (in JSON format) to track changes
Metadata about the table structure and statistics
Versioning information for time travel

Why not the other options:

Delta (A): Delta is not a file format itself, but rather a storage layer/format that uses Parquet files.
CSV (B): CSV is a row-based text format, not the primary storage format for Delta Lake tables.

Key takeaway: Delta Lake enhances Parquet files with transactional capabilities, making Parquet the fundamental storage format for all data in Delta Lake tables.

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o0001b01jwymbw06hf/see?quizType=REAL_EXAM&page=98

## 114. lqd-114

Which of the following is stored in the Databricks customer's cloud account?

A. Databricks web application

B. Cluster management metadata

C. Repos

D. Data

E. Notebooks

**Source answer: D**

In the Databricks architecture, data is stored in the customer's own cloud account (AWS, Azure, or GCP) rather than in Databricks' infrastructure. This is a key security and compliance feature of Databricks. The Databricks web application, cluster management metadata, repos, and notebooks are stored in Databricks-managed infrastructure. This separation ensures that customers maintain full control and ownership of their data while leveraging Databricks' compute and management capabilities.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75o0001c01jw1jzg87ty/see?quizType=REAL_EXAM&page=98

## 115. lqd-115

Which of the following SQL keywords can be used to convert a table from a long format to a wide format?

A. TRANSFORM

B. PIVOT

C. SUM

D. CONVERT

E. WHERE

**Source answer: B**

Explanation

The correct answer is PIVOT.

Why PIVOT is correct:
PIVOT operation: In SQL, the PIVOT operation is specifically designed to transform data from a long format (multiple rows for each category) to a wide format (multiple columns for each category).
Data transformation: PIVOT rotates data from rows to columns, aggregating values where necessary.
Common use case: This is commonly used to create cross-tabulation reports where you want to see values across different categories as separate columns.
Why other options are incorrect:
TRANSFORM: This is not a standard SQL keyword for converting table formats. It might be used in some specific contexts but not for pivoting data.
SUM: This is an aggregation function that calculates the sum of values, not for converting table formats.
CONVERT: This is typically used for data type conversion (e.g., converting strings to dates), not for changing table structure from long to wide format.
WHERE: This is a clause for filtering rows based on conditions, not for transforming table structure.
Example of PIVOT in SQL:
SELECT *
FROM sales_data
PIVOT (
  SUM(amount)
  FOR product_category IN ('Electronics', 'Clothing', 'Books')
) AS pivoted_table;


This would convert long-format sales data with multiple rows per product category into wide format with separate columns for each product category.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd75o1001f01jwiasd6bpt/see?quizType=REAL_EXAM&page=99

## 116. lqd-116

Which of the following commands will return the number of null values in the member_id column?

A. SELECT count(member_id) FROM my_table;

B. SELECT count(member id)-count null(member_id) FROM my_table;

C. SELECT count_if(member_id IS NULL) FROM my_table;

D. SELECT null member_jd) FROM my_table;

E. SELECT count null(member id) FROM my_table;

**Source answer: C**

Explanation

Let's analyze each option:

Option A: SELECT count(member_id) FROM my_table;

This returns the count of non-null values in the member_id column, not null values.
The COUNT() function in SQL excludes NULL values by default.

Option B: SELECT count(member id)-count null(member_id) FROM my_table;

This has syntax errors:
member id should be member_id (missing underscore)
count null() is not a valid SQL function
Even if corrected, this would try to subtract an invalid function call

Option C: SELECT count_if(member_id IS NULL) FROM my_table; ✓ CORRECT

count_if() is a Spark SQL function that counts rows where the condition is true.
member_id IS NULL correctly identifies null values.
This will return the exact count of null values in the member_id column.

Option D: SELECT null member_jd) FROM my_table;

This has multiple syntax errors:
member_jd appears to be a typo (should be member_id)
Missing opening parenthesis
null is not a function
This is not valid SQL syntax

Option E: SELECT count null(member id) FROM my_table;

This has syntax errors:
member id should be member_id (missing underscore)
count null() is not a valid SQL function
Should be count_if() or use COUNT(*) with a WHERE clause
Alternative Correct Approaches

In Spark SQL, you could also use:

SELECT COUNT(*) FROM my_table WHERE member_id IS NULL;
SELECT SUM(CASE WHEN member_id IS NULL THEN 1 ELSE 0 END) FROM my_table;
Key Learning Points
COUNT(column_name) excludes NULL values
COUNT(*) counts all rows including NULLs
count_if(condition) counts rows where the condition evaluates to TRUE
IS NULL is the correct operator to check for null values in SQL

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75o1001g01jwmjt0j23t/see?quizType=REAL_EXAM&page=99

## 117. lqd-117

A data engineer is attempting to drop a Spark SQL table my_table and runs the following command: DROP TABLE IF EXISTS my_table;

After running this command, the engineer notices that the data files and metadata files have been deleted from the file system.

Which of the following describes why all of these files were deleted?

A. The table was managed

B. The table's data was smaller than 10 GB

C. The table's data was larger than 10 GB

D. The table was external

E. The table did not have a location

**Source answer: A**

Explanation

In Databricks/Spark SQL, there are two types of tables:

Managed Tables (also called internal tables):

The data is managed by the metastore
Both the metadata AND the data files are stored within the system
When you drop a managed table using DROP TABLE, both the metadata AND the underlying data files are deleted

External Tables:

Only the metadata is managed by the metastore
The data files are stored in an external location (like S3, ADLS, etc.)
When you drop an external table using DROP TABLE, only the metadata is deleted, but the underlying data files remain intact

In this scenario, since both the data files and metadata files were deleted when running DROP TABLE IF EXISTS my_table;, this indicates that the table was a managed table.

Key points:

Option A is correct because managed tables have their data lifecycle managed by the metastore
Option D (external table) is incorrect because external tables only delete metadata, not data files
Options B and C (data size) are irrelevant to whether files are deleted
Option E is incorrect because all tables have a location (either managed by the system or specified by the user)

Additional context:

Managed tables are created without specifying a location or using CREATE TABLE without the LOCATION clause
External tables are created using CREATE TABLE ... LOCATION 'path' or CREATE EXTERNAL TABLE syntax
The IF EXISTS clause simply prevents an error if the table doesn't exist, but doesn't affect the deletion behavior

Source copies: 6; distinct source versions: 6.

Source: https://www.leetquiz.com/quiz/cmkcd75o1001k01jw1bnpl0ay/see?quizType=REAL_EXAM&page=99

## 118. lqd-118

In which of the following scenarios should a data engineer use the MERGE INTO command instead of the INSERT INTO command?

A. When the location of the data needs to be changed

B. When the target table is an external table

C. When the source table can be deleted

**Source answer: C**

Explanation

The correct answer is C. When the source table can be deleted.

Why MERGE INTO vs INSERT INTO:

MERGE INTO (also known as UPSERT) is used when you need to:

Update existing records
Insert new records
Delete records
Perform conditional operations based on whether records exist

INSERT INTO is used when you simply want to append new data to a table without checking for existing records.

Analysis of Options:

A. When the location of the data needs to be changed - This is incorrect. Changing data location is typically handled by ALTER TABLE commands or by creating new tables, not by MERGE INTO.

B. When the target table is an external table - This is incorrect. Both MERGE INTO and INSERT INTO can work with external tables in Databricks. The table type doesn't determine which command to use.

C. When the source table can be deleted - This is CORRECT. MERGE INTO is particularly useful when you need to handle scenarios where:

You want to delete records from the target table that don't exist in the source (using DELETE clause)
You're performing incremental updates where some source records might be removed
You need to synchronize two tables completely
Key Use Cases for MERGE INTO:
Incremental data loading - Update existing records and insert new ones
Data synchronization - Keep two tables in sync
Slowly Changing Dimensions (SCD) - Handle type 1 or type 2 SCD patterns
Data deduplication - Update existing duplicates
Example Scenario:

If you have a customer table and receive daily updates, you would use MERGE INTO to:

Update existing customer records
Insert new customers
Optionally delete customers who are no longer in the source

This is why option C is correct - when source data might be deleted or removed, MERGE INTO with DELETE clause is the appropriate command to handle such scenarios.

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o2001m01jws2xlneef/see?quizType=REAL_EXAM&page=100

## 119. lqd-119

A data engineer is working with two tables. Each of these tables is displayed below in its entirety.

sales

customer_id	spend	units
a1	28.94	7
a3	874.12	23
a4	8.99	1

favorite_stores

customer_id	store_id
a1	s1
a2	s1
a4	s2

The data engineer runs the following query to join these tables together:

SELECT
    sales.customer_id,
    sales.spend,
    favorite_stores.store_id
FROM sales
LEFT JOIN favorite_stores
ON sales.customer_id = favorite_stores.customer_id;


Which of the following will be returned by the above query?

A. customer_id	spend	store_id
a1	28.94	s1
a4	8.99	s2

B. customer_id	spend	units	store_id
a1	28.94	7	s1
a4	8.99	1	s2

C. customer_id	spend	store_id
a1	28.94	s1
a3	874.12	NULL
a4	8.99	s2

D. customer_id	spend	store_id
a1	28.94	s1
a2	NULL	s1
a3	874.12	NULL
a4	8.99	s2

E. customer_id	spend	store_id
a1	28.94	s1
a2	NULL	s1
a4	8.99	s2

**Source answer: C**

Explanation

The correct answer is C because:

LEFT JOIN returns all rows from the left table (sales) and matching rows from the right table (favorite_stores).
When there's no match in the right table, NULL values are returned for the right table's columns.
The query selects only sales.customer_id, sales.spend, and favorite_stores.store_id.

Analysis of each row:

a1: Exists in both tables → store_id = s1
a3: Exists only in sales table → store_id = NULL (no match in favorite_stores)
a4: Exists in both tables → store_id = s2
a2: Exists only in favorite_stores → NOT included because LEFT JOIN starts from sales table

Why other options are incorrect:

A: Missing row for a3 (should be included with NULL store_id)
B: Includes units column (not selected in query) and missing row for a3
D: Includes row for a2 (should not be included as it's not in sales table)
E: Includes row for a2 (should not be included) and missing row for a3

Source copies: 7; distinct source versions: 7.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o2001n01jwxjt5q6zs/see?quizType=REAL_EXAM&page=100

## 120. lqd-120

A data engineer has configured a Structured Streaming job to read from a table, manipulate the data, and then perform a streaming write into a new table.

The code block used by the data engineer is below.

spark.readStream \
    .table("sales") \
    .withColumn("avg_price", col("sales") / col("units")) \
    .writeStream \
    .option("checkpointLocation", checkpointPath) \
    .outputMode("complete") \
    ._______ \
    .table("new_sales")


If the data engineer only wants the query to process all of the available data in as many batches as required, which of the following lines of code should the data engineer use to fill in the blank?

A. processingTime(1)

B. trigger(availableNow=True)

C. trigger(parallelBatch=True)

**Source answer: B**

Explanation

In Apache Spark Structured Streaming, the trigger() method controls how often the streaming query processes data. The availableNow=True trigger is specifically designed for processing all available data in multiple batches.

Key Points:

trigger(availableNow=True): This trigger processes all currently available data in the source, but does so in multiple micro-batches rather than a single batch. This is ideal for scenarios where you want to process all data but maintain the streaming semantics and avoid overwhelming the system with a single large batch.

Why not the other options:

processingTime(1): This would trigger the query every 1 second, which would continuously process data as it arrives, not just the currently available data.
trigger(parallelBatch=True): This is not a valid trigger option in Structured Streaming.

Use Case: The availableNow trigger is particularly useful for:

Processing backlogged data
One-time data migration tasks
Batch-like processing while maintaining streaming semantics
Processing all available data without running continuously

This trigger ensures that all currently available data is processed efficiently while maintaining the benefits of the streaming execution model.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd75o2001p01jwzgsj3sdk/see?quizType=REAL_EXAM&page=100

## 121. lqd-121

Which of the following describes the type of workloads that are always compatible with Auto Loader?

A. Streaming workloads

B. Machine learning workloads

C. Serverless workloads

D. Batch workloads

E. Dashboard workloads

**Source answer: A, D**

Auto Loader is a Databricks feature designed for incremental data ingestion that supports both streaming and batch workloads.

Key points:

Streaming workloads - Auto Loader is primarily designed as a streaming solution that can continuously ingest new files as they arrive in cloud storage.
Batch workloads - Auto Loader can also be used in batch mode to process existing files incrementally.
Compatibility - Auto Loader is specifically built for data ingestion workloads, not for machine learning, serverless, or dashboard workloads.

Why other options are incorrect:

Machine learning workloads - These are typically handled by MLflow, Databricks Runtime for ML, or other ML frameworks, not Auto Loader.
Serverless workloads - While Auto Loader can run on serverless compute, it's not a workload type itself.
Dashboard workloads - These refer to BI/visualization workloads typically handled by tools like Databricks SQL, Tableau, or Power BI.

Auto Loader's primary use case is incremental data ingestion from cloud storage into Delta Lake, making it compatible with both streaming and batch data processing patterns.

Source copies: 5; distinct source versions: 5.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o3001v01jwjyagclqm/see?quizType=REAL_EXAM&page=101

## 122. lqd-122

Which of the following approaches should be used to send the Databricks Job owner an email in the case that the Job fails?

A. Manually programming in an alert system in each cell of the Notebook

B. Setting up an Alert in the Job page

C. Setting up an Alert in the Notebook

D. There is no way to notify the Job owner in the case of Job failure

E. MLflow Model Registry Webhooks

**Source answer: B**

Explanation

The correct answer is B. Setting up an Alert in the Job page.

Why this is correct:
Job-level alerts: Databricks provides built-in alerting capabilities at the Job level, allowing you to configure email notifications for various job states including failure.
Job page configuration: You can set up alerts directly in the Job configuration page under the "Notifications" section.
Automated notification: This approach automatically sends notifications to the job owner when the job fails, without requiring manual programming.
Why other options are incorrect:
A. Manually programming in an alert system in each cell of the Notebook: This is inefficient and error-prone. While technically possible, it's not the recommended approach as Databricks provides built-in alerting features.
C. Setting up an Alert in the Notebook: Alerts are configured at the Job level, not the Notebook level. Notebooks don't have built-in alerting features for job failures.
D. There is no way to notify the Job owner in the case of Job failure: This is incorrect - Databricks provides multiple ways to notify job owners of failures.
E. MLflow Model Registry Webhooks: This is for MLflow model lifecycle events, not for job failure notifications.
How to set up job alerts in Databricks:
Navigate to the Job configuration page
Go to the "Notifications" section
Add email addresses to receive notifications
Configure which events trigger notifications (e.g., job start, success, failure)
Save the job configuration

This built-in feature ensures reliable, centralized alerting without the need for custom code in notebooks.

Source copies: 3; distinct source versions: 3.

Source: https://www.leetquiz.com/quiz/cmkcd75o3001y01jwvca1x39w/see?quizType=REAL_EXAM&page=101

## 123. lqd-123

Which of the following approaches can be used to identify the owner of new_table?

A. Review the Permissions tab in the table's page in Data Explorer

B. All of these options can be used to identify the owner of the table

C. Review the Owner field in the table's page in Data Explorer

D. Review the Owner field in the table's page in the cloud storage solution

E. There is no way to identify the owner of the table

**Source answer: C**

Explanation

In Databricks, the owner of a table can be identified by reviewing the Owner field in the table's page in Data Explorer. This is the correct approach because:

Data Explorer is the primary interface in Databricks for managing and viewing table metadata.
The Owner field specifically displays who owns the table, which is typically the user who created the table or was assigned ownership.
The Permissions tab (Option A) shows permissions and access controls but doesn't necessarily show the owner directly.
Option D is incorrect because cloud storage solutions don't have table pages with owner fields - this is a Databricks-specific feature.
Option E is incorrect because there is definitely a way to identify table owners in Databricks.
Option B is incorrect because not all options are valid - only Option C is correct.

Correct Answer: C - Review the Owner field in the table's page in Data Explorer

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd75o4002301jwvaplyyn7/see?quizType=REAL_EXAM&page=102

## 124. lqd-124

Which of the following describes when to use the CREATE STREAMING LIVE TABLE (formerly CREATE INCREMENTAL LIVE TABLE) syntax over the CREATE LIVE TABLE syntax when creating Delta Live Tables (DLT) tables using SQL?

A. CREATE STREAMING LIVE TABLE should be used when the subsequent step in the DLT pipeline is static.

B. CREATE STREAMING LIVE TABLE should be used when data needs to be processed incrementally.

C. CREATE STREAMING LIVE TABLE is redundant for DLT and it does not need to be used.

D. CREATE STREAMING LIVE TABLE should be used when data needs to be processed through complicated aggregations.

E. CREATE STREAMING LIVE TABLE should be used when the previous step in the DLT pipeline is static.

**Source answer: B**

Explanation

Correct Answer: B

CREATE STREAMING LIVE TABLE (formerly CREATE INCREMENTAL LIVE TABLE) should be used when data needs to be processed incrementally. This syntax is specifically designed for streaming or incremental data processing scenarios in Delta Live Tables (DLT).

Why this is correct:

Incremental Processing: CREATE STREAMING LIVE TABLE is designed to handle data that arrives continuously or in batches, processing only new or changed data rather than reprocessing the entire dataset.
Streaming Use Cases: This syntax is ideal for real-time data ingestion, change data capture (CDC), and other scenarios where data needs to be processed as it arrives.
Efficiency: It enables more efficient processing by avoiding full table scans and only processing new data.

Why other options are incorrect:

A: Incorrect - The subsequent step being static doesn't determine whether to use streaming tables. The decision is based on how the current table processes data.
C: Incorrect - CREATE STREAMING LIVE TABLE is not redundant; it serves a specific purpose for incremental/streaming data processing.
D: Incorrect - Complicated aggregations can be performed in both static and streaming tables. The choice depends on whether data arrives incrementally, not on the complexity of transformations.
E: Incorrect - The previous step being static doesn't determine whether to use streaming tables. A streaming table can process data from static sources incrementally.

Key Takeaway: Use CREATE STREAMING LIVE TABLE when you need to process data incrementally (streaming data, CDC, or batch updates), and use CREATE LIVE TABLE for static, batch-oriented processing where the entire dataset is processed at once.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd7gpk000w01jvt8y1e4lx/see?quizType=REAL_EXAM&page=107

## 125. lqd-125

An engineering manager wants to monitor the performance of a recent project using a Databricks SQL query. For the first week following the project's release, the manager wants the query results to be updated every minute. However, the manager is concerned that the compute resources used for the query will be left running and cost the organization a lot of money beyond the first week of the project's release.

Which of the following approaches can the engineering team use to ensure the query does not cost the organization any money beyond the first week of the project's release?

A. They can set a limit to the number of DBUs that are consumed by the SQL Endpoint.

B. They can set the query's refresh schedule to end after a certain number of refreshes.

C. They cannot ensure the query does not cost the organization money beyond the first week of the project's release.

D. They can set a limit to the number of individuals that are able to manage the query's refresh schedule.

E. They can set the query's refresh schedule to end on a certain date in the query scheduler.

**Source answer: E**

Explanation

The correct answer is E because Databricks SQL queries with scheduled refreshes can be configured with an end date in the query scheduler. This allows the engineering team to:

Set up the query to refresh every minute during the first week
Configure the schedule to automatically end after the first week
Ensure that no further compute resources are consumed beyond that period

Why other options are incorrect:

A: Setting a limit to the number of DBUs consumed by the SQL Endpoint would limit overall endpoint usage but wouldn't specifically stop this query's scheduled refreshes after the first week.
B: Setting the query's refresh schedule to end after a certain number of refreshes could work, but option E is more precise since it allows ending on a specific date (after exactly one week).
C: This is incorrect because Databricks provides mechanisms to control scheduled query execution.
D: Limiting who can manage the query's refresh schedule doesn't prevent the query from continuing to run and incurring costs.

Best Practice: When setting up time-bound monitoring queries in Databricks SQL, always configure an end date in the scheduler to prevent unnecessary costs from ongoing refreshes.

Source copies: 4; distinct source versions: 4.

Source: https://www.leetquiz.com/quiz/cmkcd7gpl001101jvw43lxrt6/see?quizType=REAL_EXAM&page=108

## 126. lqd-126

Where in the Spark UI can one diagnose a performance problem induced by not leveraging predicate push-down?

A. In the Executor's log file, by grepping for "predicate push-down"

B. In the Stage's Detail screen, in the Completed Stages table, by noting the size of data read from the Input column

C. In the Storage Detail screen, by noting which RDDs are not stored on disk

D. In the Delta Lake transaction log, by noting the column statistics

E. In the Query Detail screen, by interpreting the Physical Plan

**Source answer: E**

The correct answer is E. In the Query Detail screen, by interpreting the Physical Plan.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpm001e01jvcyg8hjga/see?quizType=REAL_EXAM&page=109

## 127. lqd-127

A data analyst has developed a query that runs against Delta table. They want help from the data engineering team to implement a series of tests to ensure the data returned by the query is clean. However, the data engineering team uses Python for its tests rather than SQL.

Which of the following operations could the data engineering team use to run the query and operate with the results in PySpark?

A. SELECT * FROM sales

B. spark.delta.table

C. spark.sql

D. There is no way to share data between PySpark and SQL.

E. spark.table

**Source answer: C, E**

Explanation

In PySpark, there are multiple ways to execute SQL queries and work with the results:

Correct Options:

C. spark.sql - This is the primary method to execute SQL queries in PySpark. It returns a DataFrame that can be used for further data processing and testing.
E. spark.table - This method can be used to reference a table that has been registered in the Spark session, which could include the results of a query if it's saved as a temporary view.

Incorrect Options:

A. SELECT * FROM sales - This is just a SQL query string, not a PySpark operation. It needs to be wrapped in spark.sql() to execute.
B. spark.delta.table - This is not a valid PySpark method. The correct way to work with Delta tables is spark.read.format("delta").table() or spark.table() if the table is registered.
D. There is no way to share data between PySpark and SQL - This is incorrect. PySpark and SQL can share data through DataFrames, temporary views, and Delta tables.

How to implement the solution:

# Method 1: Using spark.sql()
query = "SELECT * FROM sales WHERE amount > 1000"
df = spark.sql(query)

# Now you can run tests on the DataFrame
# Example test: check for null values
null_count = df.filter(df.amount.isNull()).count()
assert null_count == 0, f"Found {null_count} null values in amount column"

# Method 2: Using spark.table() if the query result is saved as a view
spark.sql("CREATE OR REPLACE TEMP VIEW clean_sales AS SELECT * FROM sales WHERE amount > 1000")
df = spark.table("clean_sales")


Both spark.sql() and spark.table() allow the data engineering team to work with SQL query results in PySpark for implementing data quality tests.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source: https://www.leetquiz.com/quiz/cmkcd7gpo001n01jvy0ay7ux2/see?quizType=REAL_EXAM&page=111

## 128. lqd-128

Which of the following queries is performing a streaming hop from raw data to a Bronze table?

A. (spark.table("sales")
  .groupBy("store")
  .agg(sum("sales"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("complete")
  .table("newSales"))


B. (spark.table("sales")
  .filter(col("units") > 0)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


C. (spark.table("sales")
  .withColumn("avgPrice", col("sales") / col("units"))
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


D. (spark.read.load(rawSalesLocation)
  .write
  .mode("append")
  .table("newSales"))


E. (spark.readStream.load(rawSalesLocation)
  .writeStream
  .option("checkpointLocation", checkpointPath)
  .outputMode("append")
  .table("newSales"))


**Source answer: E**

Explanation

Option E is the correct answer because it represents a streaming hop from raw data to a Bronze table. Here's why:

Key Characteristics of a Streaming Hop:
Reads from raw data source - Uses spark.readStream.load(rawSalesLocation) to read streaming data from raw files
Streaming write - Uses .writeStream to write as a streaming job
Checkpointing - Includes .option("checkpointLocation", checkpointPath) for fault tolerance
Append mode - Uses .outputMode("append") which is appropriate for streaming writes to Bronze tables
Why Other Options Are Incorrect:

Option A, B, C: These all read from spark.table("sales") which means they're reading from an existing table (likely a Bronze or Silver table), not from raw data. They're performing transformations on existing tables, not the initial ingestion from raw data.

Option D: This uses batch processing (spark.read.load) not streaming, and doesn't include checkpointing, which is essential for streaming jobs.

Bronze Table Context:

In Databricks medallion architecture:

Bronze tables store raw, unprocessed data as it arrives from source systems
Streaming hops to Bronze tables typically involve reading from raw data sources (files, Kafka, etc.) and writing to Delta tables with minimal or no transformations
The checkpoint location ensures exactly-once processing semantics and fault tolerance

Option E correctly demonstrates the pattern for streaming ingestion from raw data files into a Bronze table.

Source copies: 5; distinct source versions: 5.

Source: https://www.leetquiz.com/quiz/cmkcd7gpr002601jvqlknp3l3/see?quizType=REAL_EXAM&page=113

## 129. lqd-129

Which of the following statements regarding the relationship between Silver tables and Bronze tables is always true?

A. Silver tables contain a less refined, less clean view of data than Bronze data.

B. Silver tables contain aggregates while Bronze data is unaggregated.

C. Silver tables contain more data than Bronze tables.

D. Silver tables contain a more refined and cleaner view of data than Bronze tables.

E. Silver tables contain less data than Bronze tables.

**Source answer: D**

In the Databricks Lakehouse architecture, the medallion architecture consists of three layers: Bronze, Silver, and Gold. Bronze tables contain raw, unprocessed data ingested from source systems. Silver tables contain cleaned, validated, and enriched data that has been transformed from Bronze tables. Gold tables contain aggregated, business-level data for reporting and analytics. Therefore, Silver tables always contain a more refined and cleaner view of data than Bronze tables, making option D the correct answer.

Key Points:

Bronze: Raw, unprocessed data
Silver: Cleaned, validated, enriched data
Gold: Aggregated, business-level data
The transformation from Bronze to Silver involves data quality checks, deduplication, schema enforcement, and enrichment.

Source copies: 4; distinct source versions: 4.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmkcd7gpr002801jv81r1cxb7/see?quizType=REAL_EXAM&page=114

## 130. lqd-130

A developer has successfully configured their credentials for Databricks Repos and cloned a remote Git repository. They do not have privileges to make changes to the main branch, which is the only branch currently visible in their workspace.

Which approach allows this user to share their code updates without the risk of overwriting the work of their teammates?

A. Use Repos to checkout all changes and send the git diff log to the team.

B. Use Repos to create a fork of the remote repository, commit all changes, and make a pull request on the source repository.

C. Use Repos to pull changes from the remote Git repository; commit and push changes to a branch that appeared as changes were pulled.

D. Use Repos to merge all differences and make a pull request back to the remote repository.

E. Use Repos to create a new branch, commit all changes, and push changes to the remote Git repository.

**Source answer: E**

Explanation

The correct answer is E because:

Creating a new branch is the standard Git workflow for developers who don't have write access to the main branch. This allows them to work independently without affecting the main codebase.

Committing all changes to the new branch ensures their work is saved locally.

Pushing changes to the remote Git repository makes their branch available to teammates for review and collaboration.

This approach avoids overwriting teammates' work because:

The developer works on an isolated branch
Changes can be reviewed via pull requests
The main branch remains protected
Teammates can see and review the changes before merging

Why other options are incorrect:

A: Sending git diff logs is not a proper collaboration method and doesn't integrate changes into the repository.
B: Creating a fork is unnecessary when you already have access to clone the repository; creating a branch within the same repository is more efficient.
C: This option is unclear about what "branch that appeared as changes were pulled" means and doesn't specify creating a new branch for the developer's work.
D: Merging differences directly could overwrite teammates' work and doesn't follow the proper branch-based workflow.

Best Practice: In Databricks Repos, when you don't have privileges to modify the main branch, you should:

Create a new branch from the main branch
Make your changes and commit them
Push the branch to the remote repository
Create a pull request for code review
Once approved, a maintainer with appropriate privileges can merge your changes.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gps002i01jvxcx4iskb/see?quizType=REAL_EXAM&page=115

## 131. lqd-131

In order to prevent accidental commits to production data, a senior data engineer has instituted a policy that all development work will reference clones of Delta Lake tables. After testing both DEEP and SHALLOW CLONE, development tables are created using SHALLOW CLONE.

A few weeks after initial table creation, the cloned versions of several tables implemented as Type 1 Slowly Changing Dimension (SCD) stop working. The transaction logs for the source tables show that VACUUM was run the day before.

Which statement describes why the cloned tables are no longer working?

A. Because Type 1 changes overwrite existing records, Delta Lake cannot guarantee data consistency for cloned tables.

B. Running VACUUM automatically invalidates any shallow clones of a table; DEEP CLONE should always be used when a cloned table will be repeatedly queried.

C. Tables created with SHALLOW CLONE are automatically deleted after their default retention threshold of 7 days.

D. The metadata created by the CLONE operation is referencing data files that were purged as invalid by the VACUUM command.

E. The data files compacted by VACUUM are not tracked by the cloned metadata; running REFRESH on the cloned table will pull in recent changes.

**Source answer: D**

Explanation

Correct Answer: D

Why D is correct:

SHALLOW CLONE creates a new table that references the same underlying data files as the source table, but with its own separate metadata.
When VACUUM is run on the source table, it removes data files that are no longer needed based on the retention period (default 7 days).
The shallow clone's metadata still points to these data files that have been physically deleted by VACUUM.
When queries try to access the cloned table, they fail because the referenced data files no longer exist.

Why other options are incorrect:

A: Type 1 SCD behavior (overwriting existing records) doesn't inherently prevent Delta Lake from maintaining consistency for cloned tables. This is unrelated to the VACUUM issue.

B: VACUUM doesn't automatically invalidate shallow clones. The issue is that VACUUM removes data files that shallow clones depend on, not that it invalidates them automatically.

C: SHALLOW CLONE tables are not automatically deleted after 7 days. The 7-day reference is likely confusing it with the default retention period for VACUUM.

E: Running REFRESH won't help because the data files have been physically deleted. REFRESH updates metadata but cannot recreate deleted data files.

Key Learning Points:

SHALLOW CLONE creates a metadata-only copy that references the original data files.
DEEP CLONE copies both metadata AND data files, creating an independent copy.
VACUUM removes data files older than the retention period (default 7 days).
For development tables that need to persist, use DEEP CLONE or ensure VACUUM isn't run on source tables while clones are in use.
Consider adjusting the retention period or using DEEP CLONE for long-term development work.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpt002j01jv0ashr7ps/see?quizType=REAL_EXAM&page=115

## 132. lqd-132

You are performing a join operation to combine values from a static userLookup table with a streaming DataFrame streamingDF. Which code block attempts to perform an invalid stream-static join?

A. userLookup.join(streamingDF, ["userid"], how="inner")

B. streamingDF.join(userLookup, ["user_id"], how="outer")

C. streamingDF.join(userLookup, ["user_id"], how="left")

D. streamingDF.join(userLookup, ["userid"], how="inner")

E. userLookup.join(streamingDF, ["user_id"], how="right")

**Source answer: B**

Explanation

In Apache Spark Structured Streaming, stream-static joins have specific restrictions:

Stream-static joins must be inner or left outer joins when the streaming DataFrame is on the left side of the join.
The streaming DataFrame must be the left side for left outer joins.
The streaming DataFrame can be either side for inner joins.
Right outer joins and full outer joins are NOT supported for stream-static joins.

Let's analyze each option:

A. userLookup.join(streamingDF, ["userid"], how="inner") - VALID: This is an inner join where the static table is on the left and streaming DataFrame is on the right. Inner joins are supported with streaming DataFrame on either side.

B. streamingDF.join(userLookup, ["user_id"], how="outer") - INVALID: This is a full outer join (how="outer"). Full outer joins are NOT supported in stream-static joins.

C. streamingDF.join(userLookup, ["user_id"], how="left") - VALID: This is a left outer join with the streaming DataFrame on the left side. Left outer joins are supported when the streaming DataFrame is on the left.

D. streamingDF.join(userLookup, ["userid"], how="inner") - VALID: This is an inner join with the streaming DataFrame on the left side. Inner joins are supported with streaming DataFrame on either side.

E. userLookup.join(streamingDF, ["user_id"], how="right") - VALID: This is a right outer join where the static table is on the left and streaming DataFrame is on the right. Right outer joins are equivalent to left outer joins with the streaming DataFrame on the left side, so they are supported.

Key Points:

Full outer joins (how="outer") are the only join type that is completely unsupported for stream-static joins.
The column names (userid vs user_id) don't affect the validity of the join type itself.
The question asks for the code block that attempts to perform an invalid stream-static join, which is option B.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpt002k01jv7dr6wmx7/see?quizType=REAL_EXAM&page=115

## 133. lqd-133

Where in the Spark UI are two of the primary indicators that a partition is spilling to disk?

A. Query’s detail screen and Job’s detail screen

B. Stage’s detail screen and Executor’s log files

C. Driver’s and Executor’s log files

D. Executor’s detail screen and Executor’s log files

E. Stage’s detail screen and Query’s detail screen

**Source answer: B**

Explanation

In the Spark UI, the primary indicators that a partition is spilling to disk are found in:

Stage's detail screen - This shows metrics for each stage, including spill metrics (disk spill bytes, memory spill bytes, etc.)
Executor's log files - These contain detailed logging information about spill events during task execution
Why other options are incorrect:
A: Query's detail screen provides high-level query information but not detailed spill metrics for individual partitions
C: Driver's log files don't typically contain partition-level spill information; spill happens at executor level
D: Executor's detail screen shows resource usage but not specific spill indicators
E: Query's detail screen doesn't show partition-level spill details
Key Points:
Spilling occurs when data doesn't fit in memory and needs to be written to disk
The Stage detail screen in Spark UI provides aggregated spill statistics for each stage
Executor logs contain detailed messages about when and how much data is spilled during task execution
Monitoring these indicators helps identify memory pressure and optimize Spark job performance

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpt002l01jvhnjg4gbk/see?quizType=REAL_EXAM&page=116

## 134. lqd-134

A task orchestrator has been configured to run two hourly tasks. First, an outside system writes Parquet data to a directory mounted at /mnt/raw_orders/. After this data is written, a Databricks job containing the following code is executed:

(spark.readStream
  .format("parquet")
  .load("/mnt/raw_orders/")
  .withWatermark("time", "2 hours")
  .dropDuplicates(["customer_id", "order_id"])
  .writeStream
  .trigger(once=True)
  .table("orders")
)


Assume that the fields customer_id and order_id serve as a composite key to uniquely identify each order, and that the time field indicates when the record was queued in the source system.

If the upstream system is known to occasionally enqueue duplicate entries for a single order hours apart, which statement is correct?

A. Duplicate records enqueued more than 2 hours apart may be retained and the orders table may contain duplicate records with the same customer_id and order_id.

B. All records will be held in the state store for 2 hours before being deduplicated and committed to the orders table.

C. The orders table will contain only the most recent 2 hours of records and no duplicates will be present.

D. Duplicate records arriving more than 2 hours apart will be dropped, but duplicates that arrive in the same batch may both be written to the orders table.

E. The orders table will not contain duplicates, but records arriving more than 2 hours late will be ignored and missing from the table.

**Source answer: A**

Explanation

This question tests understanding of Structured Streaming's watermarking and deduplication behavior.

Key Concepts:

Watermarking: withWatermark("time", "2 hours") defines a watermark that tracks the maximum event time seen in the data. Records with event time older than max_event_time - 2 hours are considered "late" and may be dropped.
dropDuplicates() with watermark: When dropDuplicates() is used with a watermark, Spark maintains state for deduplication only for records within the watermark window. Records older than the watermark threshold are considered "too late" and their state may be cleaned up.
Trigger(once=True): This runs the streaming query once, processing all available data as a single batch.

Why Option A is correct:

The watermark is set to 2 hours, meaning Spark will maintain state for deduplication for records within a 2-hour window of the maximum event time.
If duplicate records arrive more than 2 hours apart, the state for the first record may have been cleaned up by the time the second duplicate arrives (since it's outside the 2-hour watermark window).
When the state is cleaned up, Spark no longer "remembers" that it has seen the first record, so the second duplicate will be processed as a new record.
This means duplicates arriving more than 2 hours apart may both be written to the orders table.

Why other options are incorrect:

B: Records are not held for 2 hours before deduplication; watermarking affects state cleanup, not processing delay.
C: The table will contain all records, not just the most recent 2 hours. Watermarking affects state cleanup, not which records are written.
D: This is partially correct about duplicates arriving more than 2 hours apart being dropped, but incorrect about duplicates in the same batch. dropDuplicates() works within a batch, so duplicates in the same batch would be dropped.
E: Records arriving more than 2 hours late may be dropped, but the main issue is that duplicates arriving far apart may both be retained due to state cleanup.

Important Note: The trigger(once=True) means this runs as a batch job, but the watermark logic still applies to state management for deduplication.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpt002m01jvl5ta0vm8/see?quizType=REAL_EXAM&page=116

## 135. lqd-135

A junior data engineer is migrating a workload from a relational database system to the Databricks Lakehouse. The source system uses a star schema, leveraging foreign key constraints and multi-table inserts to validate records on write. Which consideration will impact the decisions made by the engineer while migrating this workload?

A. Databricks only allows foreign key constraints on hashed identifiers, which avoid collisions in highly-parallel writes.

B. Databricks supports Spark SQL and JDBC; all logic can be directly migrated from the source system without refactoring.

C. Committing to multiple tables simultaneously requires taking out multiple table locks and can lead to a state of deadlock.

D. All Delta Lake transactions are ACID compliant against a single table, and Databricks does not enforce foreign key constraints.

E. Foreign keys must reference a primary key field; multi-table inserts must leverage Delta Lake's upsert functionality.

**Source answer: D**

Explanation

Correct Answer: D

This is the correct answer because it accurately describes key architectural differences between traditional relational databases and Databricks Lakehouse:

Delta Lake ACID compliance: Delta Lake provides ACID (Atomicity, Consistency, Isolation, Durability) transactions, but these are guaranteed within a single table, not across multiple tables in a single transaction.

No foreign key constraint enforcement: Databricks does not enforce foreign key constraints at the database level. While you can define foreign key relationships in your data model for documentation purposes, Databricks will not validate or enforce these constraints during write operations.

Why other options are incorrect:

A: Incorrect - Databricks does not enforce foreign key constraints at all, regardless of the identifier type.
B: Incorrect - While Databricks supports Spark SQL and JDBC, the underlying architecture is different from traditional RDBMS. Multi-table inserts with foreign key validation cannot be directly migrated without refactoring.
C: Incorrect - This describes a traditional RDBMS concern with table locking, but Delta Lake uses optimistic concurrency control rather than table-level locking.
E: Incorrect - While Delta Lake has upsert functionality (MERGE), this is not specifically related to foreign key constraints, which Databricks doesn't enforce.

Migration Implications: When migrating from a traditional RDBMS with foreign key constraints to Databricks Lakehouse, the data engineer must:

Implement data quality checks separately (using tools like Delta Live Tables expectations or custom validation logic)
Handle referential integrity at the application level
Consider using Delta Lake's MERGE operations for upserts
Understand that multi-table transactions with rollback across tables are not natively supported

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpt002n01jvw77xf5nc/see?quizType=REAL_EXAM&page=116

## 136. lqd-136

A table named user_ltv is being used to create a view that will be used by data analysts on various teams. Users in the workspace are configured into groups, which are used for setting up data access using ACLs.

The user_ltv table has the following schema: email STRING, age INT, ltv INT

The following view definition is executed:

CREATE VIEW user_ltv_no_minors AS
SELECT email, age, ltv
FROM user_ltv
WHERE
    CASE
        WHEN is_member("auditing") THEN TRUE
        ELSE age >= 18
    END


An analyst who is not a member of the auditing group executes the following query:

SELECT * FROM user_ltv_no_minors


Which statement describes the results returned by this query?

A. All columns will be displayed normally for those records that have an age greater than 17; records not meeting this condition will be omitted.

B. All age values less than 18 will be returned as null values, all other columns will be returned with the values in user_ltv.

C. All values for the age column will be returned as null values, all other columns will be returned with the values in user_ltv.

D. All records from all columns will be displayed with the values in user_ltv.

E. All columns will be displayed normally for those records that have an age greater than 18; records not meeting this condition will be omitted.

**Source answer: A**

Why the correct answer is A

The WHERE clause logic is:

CASE
  WHEN is_member("auditing") THEN TRUE
  ELSE age >= 18
END

The analyst is not in the auditing group
Therefore, the filter age >= 18 is applied
Mathematically, age >= 18 is exactly the same as “age greater than 17”

So the query returns:

✅ All columns (email, age, ltv)
✅ Only rows where age >= 18
❌ Rows with age < 18 are completely omitted

This is precisely what option A states.

❌ Why other options are incorrect
B & C: Rows are filtered out, not masked with NULL
D: Not all records are returned
E: Incorrect wording — “greater than 18” excludes age 18

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002p01jvcf964cgk/see?quizType=REAL_EXAM&page=116

## 137. lqd-137

The data governance team is reviewing code used for deleting records for compliance with GDPR. The following logic has been implemented to propagate delete requests from the user_lookup table to the user_aggregates table.

(spark.read
  .format("delta")
  .option("readChangeData", True)
  .option("startingTimestamp", '2021-08-22 00:00:00')
  .option("endingTimestamp", '2021-08-29 00:00:00')
  .table("user_lookup")
  .createOrReplaceTempView("changes"))

spark.sql("""
DELETE FROM user_aggregates
WHERE user_id IN (
  SELECT user_id
  FROM changes
  WHERE _change_type='delete'
)
""")


Assuming that user_id is a unique identifying key and that all users that have requested deletion have been removed from the user_lookup table, which statement describes whether successfully executing the above logic guarantees that the records to be deleted from the user_aggregates table are no longer accessible and why?

A. No; the Delta Lake DELETE command only provides ACID guarantees when combined with the MERGE INTO command.

B. No; files containing deleted records may still be accessible with time travel until a VACUUM command is used to remove invalidated data files.

C. Yes; the change data feed uses foreign keys to ensure delete consistency throughout the Lakehouse.

D. Yes; Delta Lake ACID guarantees provide assurance that the DELETE command succeeded fully and permanently purged these records.

E. No; the change data feed only tracks inserts and updates, not deleted records.

**Source answer: B**

Explanation

Correct Answer: B

Why B is correct:

Delta Lake's Time Travel Feature: Delta Lake maintains a transaction log that enables time travel functionality. When records are deleted using the DELETE command, they are marked as deleted in the transaction log but the actual data files containing those records are not immediately removed from storage.

Data Accessibility via Time Travel: Deleted records remain accessible through time travel queries until the data files are physically removed by running the VACUUM command. This means that even after a successful DELETE operation, the data can still be accessed by:

Querying previous versions of the table
Using time travel syntax like SELECT * FROM table VERSION AS OF <version> or SELECT * FROM table TIMESTAMP AS OF <timestamp>

GDPR Compliance Implications: For GDPR compliance, organizations need to ensure that personal data is truly inaccessible, not just logically deleted. The VACUUM command must be executed with appropriate retention settings to physically remove the data files containing deleted records.

Change Data Feed (CDF) Context: The code uses CDF to read delete operations from the user_lookup table, which correctly identifies records marked for deletion. However, the DELETE operation on user_aggregates only logically removes records - the physical data files remain until VACUUM.

Why other options are incorrect:

A: Incorrect because Delta Lake DELETE command does provide ACID guarantees on its own - it's not dependent on MERGE INTO.
C: Incorrect because change data feed doesn't use foreign keys; it tracks changes (inserts, updates, deletes) but doesn't enforce referential integrity.
D: Incorrect because while Delta Lake provides ACID guarantees for the transaction, it doesn't immediately purge records from storage - they remain accessible via time travel.
E: Incorrect because the change data feed does track deleted records (as shown by _change_type='delete'), so this statement is factually wrong.

Key Takeaway: For GDPR compliance, organizations must not only execute DELETE operations but also manage data retention policies and run VACUUM to ensure deleted data is physically inaccessible.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002q01jv3ck9pvme/see?quizType=REAL_EXAM&page=116

## 138. lqd-138

The data engineering team has been tasked with configuring connections to an external database that does not have a supported native connector with Databricks. The external database already has data security configured by group membership. These groups map directly to user groups already created in Databricks that represent various teams within the company.

A new login credential has been created for each group in the external database. The Databricks Utilities Secrets module will be used to make these credentials available to Databricks users.

Assuming that all the credentials are configured correctly on the external database and group membership is properly configured on Databricks, which statement describes how teams can be granted the minimum necessary access to using these credentials?

A. "Manage" permissions should be set on a secret key mapped to those credentials that will be used by a given team.

B. "Read" permissions should be set on a secret key mapped to those credentials that will be used by a given team.

C. "Read" permissions should be set on a secret scope containing only those credentials that will be used by a given team.

D. "Manage" permissions should be set on a secret scope containing only those credentials that will be used by a given team. No additional configuration is necessary as long as all users are configured as administrators in the workspace where secrets have been added.

**Source answer: C**

Explanation

Correct Answer: C - "Read" permissions should be set on a secret scope containing only those credentials that will be used by a given team.

Why this is correct:

Principle of Least Privilege: Teams should only have access to the credentials they need, not all credentials. By creating separate secret scopes for each team's credentials, you can isolate access appropriately.

Secret Scope vs Secret Key Permissions:

Secret Scope level: Controls who can read secrets within that scope
Secret Key level: Controls who can read individual secrets within a scope

Since each team needs access to their specific credentials only, creating separate scopes with "Read" permissions for each team is the most secure approach.

Why not "Manage" permissions: "Manage" permissions allow users to modify or delete secrets, which is unnecessary for simply using credentials to connect to an external database. Teams only need "Read" access to retrieve the credentials.

Why not secret key-level permissions: While you could set permissions at the secret key level within a shared scope, this is less secure because:

Users could potentially see what other secrets exist in the scope (even if they can't read them)
Scope-level isolation provides better security boundaries
It's easier to manage and audit when each team has its own scope

Why not the last option: The statement "No additional configuration is necessary as long as all users are configured as administrators" is incorrect because:

Making all users administrators violates the principle of least privilege
Administrators have broad access to all workspace resources, which is unnecessary and insecure
It doesn't provide the minimum necessary access required
Best Practice Implementation:
Create separate secret scopes for each team (e.g., team-a-credentials, team-b-credentials)
Store each team's database credentials in their respective scope
Grant "Read" permissions on each scope to the corresponding Databricks group
Teams can then use dbutils.secrets.get() to retrieve their credentials when connecting to the external database

This approach ensures each team has access only to their own credentials while maintaining security and auditability.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002r01jvurtyhsk2/see?quizType=REAL_EXAM&page=116

## 139. lqd-139

Which statement describes a key benefit of an end-to-end test?

A. Makes it easier to automate your test suite

B. Pinpoints errors in the building blocks of your application

C. Provides testing coverage for all code paths and branches

D. Closely simulates real world usage of your application

E. Ensures code is optimized for a real-life workflow

**Source answer: D**

Explanation

End-to-end testing is a methodology that tests the entire application flow from start to finish, simulating real user scenarios. The key benefit of end-to-end testing is that it closely simulates real world usage of your application.

Let's analyze why the other options are incorrect:

A. Makes it easier to automate your test suite - While automation is important for testing, this is not the primary benefit of end-to-end tests specifically. Many types of tests can be automated.

B. Pinpoints errors in the building blocks of your application - This is actually the benefit of unit testing, not end-to-end testing. Unit tests focus on individual components or "building blocks."

C. Provides testing coverage for all code paths and branches - This describes comprehensive test coverage, which is achieved through a combination of different test types (unit, integration, end-to-end), not just end-to-end tests alone.

E. Ensures code is optimized for a real-life workflow - While end-to-end tests can help identify performance issues, optimization is not their primary purpose. Performance testing would be more appropriate for optimization.

Key characteristics of end-to-end testing:

Tests the complete application flow
Simulates real user scenarios and workflows
Validates system integration and data flow
Tests from the user's perspective
Helps identify issues that occur when different components interact

This type of testing is crucial for ensuring that all integrated components work together as expected in production-like environments.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002u01jvuwffbsvv/see?quizType=REAL_EXAM&page=117

## 140. lqd-140

The Databricks CLI is used to trigger a run of an existing job by passing the job_id parameter. The response that the job run request has been submitted successfully includes a field run_id. Which statement describes what the number alongside this field represents?

A. The job_id and number of times the job has been run are concatenated and returned.

B. The total number of jobs that have been run in the workspace.

C. The number of times the job definition has been run in this workspace.

D. The job_id is returned in this field.

E. The globally unique ID of the newly triggered run.

**Source answer: E**

Explanation

In Databricks, when you trigger a job run using the CLI or API, the response includes a run_id field. This run_id is a globally unique identifier for that specific job run instance.

Key points:

Globally unique: Each job run gets a unique identifier that distinguishes it from all other job runs in the workspace
Not concatenated with job_id: The run_id is not simply a concatenation of job_id and run count
Not a simple counter: It's not just a sequential number of how many times the job has been run
Not the job_id itself: The run_id is different from the job_id
Not workspace-wide job count: It doesn't represent the total number of jobs run in the workspace

This unique run_id is essential for:

Tracking the specific run's status and progress
Retrieving logs and results for that particular execution
Monitoring and debugging individual job runs
Referencing the run in subsequent API calls

When you submit a job run request successfully, Databricks generates and returns this unique identifier to allow you to monitor and manage that specific execution.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002v01jvfa5lrwad/see?quizType=REAL_EXAM&page=117

## 141. lqd-141

The data science team has created and logged a production model using MLflow. The model accepts a list of column names and returns a new column of type DOUBLE.

The following code correctly imports the production model, loads the customers table containing the customer_id key column into a DataFrame, and defines the feature columns needed for the model.

model = mlflow.pyfunc.spark_udf(spark, model_uri="models:/churn/prod")
df = spark.table("customers")
columns = ["account_age", "time_since_last_seen", "app_rating"]


Which code block will output a DataFrame with the schema "customer_id LONG, predictions DOUBLE"?

A. df.map(lambda x: model(x[columns])).select("customer_id, predictions")

B. df.select("customer_id", model(*columns).alias("predictions"))

C. model.predict(df, columns)

D. df.select("customer_id", pandas_udf(model, columns).alias("predictions"))

E. df.apply(model, columns).select("customer_id, predictions")

**Source answer: B**

Explanation

Correct Answer: B

Why Option B is correct:

model = mlflow.pyfunc.spark_udf(spark, model_uri="models:/churn/prod") creates a Spark UDF from the MLflow model
The UDF can be used directly in DataFrame operations
model(*columns) applies the UDF to the specified columns using the unpacking operator *
.alias("predictions") renames the resulting column to "predictions"
df.select("customer_id", model(*columns).alias("predictions")) selects both the customer_id column and the predictions column, resulting in the desired schema

Why other options are incorrect:

Option A: Uses df.map() which is not the correct way to apply UDFs in Spark DataFrames. The map() function is for RDD operations, not DataFrame operations.
Option C: model.predict(df, columns) is not a valid method for MLflow Spark UDFs. MLflow Spark UDFs are callable functions, not objects with a .predict() method.
Option D: Uses pandas_udf() which is unnecessary since mlflow.pyfunc.spark_udf() already creates a Spark UDF. This would create redundant UDF wrapping.
Option E: df.apply() is not a valid DataFrame method in PySpark. The correct method for applying functions row-wise is withColumn() or using UDFs in select() statements.

Key Concepts:

MLflow's pyfunc.spark_udf() creates a Spark User-Defined Function (UDF) that can be used in DataFrame operations
Spark UDFs can be applied to columns using the unpacking operator * when passing multiple columns
The select() method is used to choose specific columns from a DataFrame
The alias() method renames columns in the resulting DataFrame

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpu002w01jva76tpf1p/see?quizType=REAL_EXAM&page=117

## 142. lqd-142

Which statement describes the default execution mode for Databricks Auto Loader?

A. Cloud vendor-specific queue storage and notification services are configured to track newly arriving files; the target table is materialized by directly querying all valid files in the source directory.

B. New files are identified by listing the input directory; the target table is materialized by directly querying all valid files in the source directory.

C. Webhooks trigger a Databricks job to run anytime new data arrives in a source directory; new data are automatically merged into target tables using rules inferred from the data.

D. New files are identified by listing the input directory; new files are incrementally and idempotently loaded into the target Delta Lake table.

E. Cloud vendor-specific queue storage and notification services are configured to track newly arriving files; new files are incrementally and idempotently loaded into the target Delta Lake table.

**Source answer: D**

Explanation

Correct Answer: D

Auto Loader's default execution mode uses directory listing to identify new files, not cloud notification services. Here's why:

Default Mode (Directory Listing): When you don't explicitly configure cloud notification services, Auto Loader defaults to listing the input directory to discover new files. This is option D.

Incremental and Idempotent Loading: Auto Loader processes files incrementally (only new files since last run) and idempotently (same files won't be processed multiple times).

Cloud Notification Mode (Option E): This is the optimized mode that uses cloud-specific services (AWS SQS/SNS, Azure Event Grid, GCP Pub/Sub), but it's not the default. You need to explicitly configure this mode.

Why not other options:

A: Incorrect - describes cloud notification services but with direct querying instead of incremental loading
B: Incorrect - describes directory listing but with direct querying instead of incremental loading
C: Incorrect - describes webhooks which is not how Auto Loader works
E: Incorrect - describes the optimized cloud notification mode, not the default mode

Key Takeaway: Auto Loader defaults to directory listing for file discovery, which is simpler to set up but may have scalability limits with very large directories. The cloud notification mode provides better performance but requires additional configuration.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpv002z01jv0qd579pv/see?quizType=REAL_EXAM&page=118

## 143. lqd-143

A large company seeks to implement a near real-time solution involving hundreds of pipelines with parallel updates of many tables with extremely high volume and high velocity data.

Which of the following solutions would you implement to achieve this requirement?

A. Use Databricks High Concurrency clusters, which leverage optimized cloud storage connections to maximize data throughput.

B. Partition ingestion tables by a small time duration to allow for many data files to be written in parallel.

C. Configure Databricks to save all data to attached SSD volumes instead of object storage, increasing file I/O significantly.

D. Isolate Delta Lake tables in their own storage containers to avoid API limits imposed by cloud vendors.

E. Store all tables in a single database to ensure that the Databricks Catalyst Metastore can load balance overall throughput.

**Source answer: A**

Explanation

Correct Answer: A

Why Option A is correct:

High Concurrency clusters are specifically designed for scenarios with hundreds of pipelines and parallel updates:

They provide optimized cloud storage connections that maximize data throughput
They handle high concurrency workloads efficiently
They are built for scenarios with many concurrent users/jobs accessing the same data

The scenario described requires:

Near real-time processing
Hundreds of pipelines
Parallel updates of many tables
Extremely high volume and high velocity data

High Concurrency clusters address these requirements by:

Using optimized cloud storage connections (AWS S3, Azure Blob Storage, Google Cloud Storage)
Providing better throughput for concurrent operations
Handling many parallel file operations efficiently

Why other options are incorrect:

B. Partition ingestion tables by a small time duration:

While partitioning can help with parallel writes, it doesn't address the core requirement of handling hundreds of concurrent pipelines
Partitioning alone doesn't optimize cloud storage connections for high throughput

C. Configure Databricks to save all data to attached SSD volumes:

Databricks primarily uses cloud object storage (S3, ADLS, GCS) for persistent storage
Attached SSD volumes are typically for temporary/scratch space, not for persistent data storage
This approach would not scale for extremely high volume data

D. Isolate Delta Lake tables in their own storage containers:

While this might help with organization, it doesn't address throughput requirements
Could actually increase complexity and potentially reduce performance due to more API calls

E. Store all tables in a single database:

This would likely create contention and bottlenecks rather than improve throughput
The Catalyst Metastore doesn't load balance based on database organization
This approach contradicts best practices for large-scale data management

Key Takeaway: For scenarios with hundreds of pipelines, parallel updates, and extremely high volume/high velocity data, Databricks High Concurrency clusters are specifically designed to maximize throughput through optimized cloud storage connections and efficient handling of concurrent operations.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpv003101jvbls5fvvk/see?quizType=REAL_EXAM&page=118

## 144. lqd-144

Which describes a method of installing a Python package scoped at the notebook level to all nodes in the currently active cluster?

A. Run source env/bin/activate in a notebook setup script

B. Use b in a notebook cell

C. Use %pip install in a notebook cell

D. Use %sh pip install in a notebook cell

E. Install libraries from PyPI using the cluster UI

**Source answer: C**

Explanation

In Databricks, there are several ways to install Python packages, but the question specifically asks for a method that installs packages scoped at the notebook level to all nodes in the currently active cluster.

Let's analyze each option:

A. Run source env/bin/activate in a notebook setup script

This activates a virtual environment but doesn't install packages
Not a method for installing packages

B. Use b in a notebook cell

This appears to be incomplete or incorrect syntax
There's no standard b command for installing packages in Databricks

C. Use %pip install in a notebook cell ✓ CORRECT

The %pip install magic command installs packages at the notebook level
When run in a notebook cell, it installs packages to all nodes in the currently active cluster
This is the recommended method for notebook-scoped installations

D. Use %sh pip install in a notebook cell

This uses the %sh magic command to run shell commands
While it can install packages, it only installs them on the driver node, not all worker nodes
Not scoped to all nodes in the cluster

E. Install libraries from PyPI using the cluster UI

This installs packages at the cluster level, not notebook level
These packages are available to all notebooks using the cluster
Not scoped at the notebook level as requested

Key Points:

%pip install is the magic command specifically designed for notebook-scoped package installation
It ensures packages are installed on all nodes (driver and workers) in the active cluster
The installation is temporary and only persists for the duration of the notebook session
This is different from cluster-level installations which are permanent and affect all notebooks using that cluster

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpv003201jvhl1lx4gn/see?quizType=REAL_EXAM&page=118

## 145. lqd-145

You are a retailer that wants to integrate your online sales capabilities with different in-home assistants, such as Google Home. You need to interpret customer voice commands and issue an order to the backend systems. Which solutions should you choose?

A. Speech-to-Text API

B. Cloud Natural Language API

C. Dialogflow Enterprise Edition

D. AutoML Natural Language

**Source answer: C**

Explanation

For interpreting customer voice commands and issuing orders to backend systems through in-home assistants like Google Home, Dialogflow Enterprise Edition is the most appropriate solution.

Why Dialogflow Enterprise Edition is correct:

Natural Language Understanding (NLU): Dialogflow is specifically designed for building conversational interfaces that can understand user intent and extract parameters from natural language input.
Voice Command Processing: It can handle speech-to-text conversion and natural language understanding in an integrated way.
Context Management: Dialogflow maintains conversation context, which is essential for multi-turn dialogues in voice-based ordering systems.
Integration with Google Home: Dialogflow has native integration capabilities with Google Assistant and Google Home devices.
Backend Integration: It can easily connect to backend systems through webhooks or APIs to process orders.

Why other options are less suitable:

Speech-to-Text API (A): Only converts speech to text but doesn't understand the intent or meaning behind the words.
Cloud Natural Language API (B): Analyzes text for sentiment, entities, and syntax but isn't designed for conversational interfaces or intent recognition.
AutoML Natural Language (D): Used for building custom text classification models but lacks the conversational interface capabilities needed for voice assistants.

Key capabilities needed for this scenario:

Voice input processing
Intent recognition (e.g., "I want to order a pizza")
Entity extraction (e.g., pizza type, size, toppings)
Contextual understanding across multiple turns
Integration with backend order processing systems

Dialogflow Enterprise Edition provides all these capabilities in a unified platform specifically designed for building conversational agents.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmkcd7gpw003401jvxyyez4bz/see?quizType=REAL_EXAM&page=118

## 146. lqd-146

How do you reference another DLT table within the same DLT pipeline using SQL?

A. FROM stream(table)

B. FROM catalog.schema.table

C. FROM live.table_name

D. FROM dlt_table

**Source answer: C**

In Delta Live Tables (DLT) using SQL, the live schema prefix is used to reference other tables and views that are defined within the same pipeline.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbx000001jxsuafm6ab/see?quizType=REAL_EXAM&page=144

## 147. lqd-147

What is the primary purpose of 'Dynamic File Pruning' in Databricks?

A. To skip scanning irrelevant files in a large table based on a filter applied to a joined smaller table.

B. To automatically delete files unaccessed for 90 days.

C. To compress small files during query runtime.

D. To remove duplicate columns from a SELECT statement.

**Source answer: A**

Dynamic File Pruning significantly improves join performance by pruning (skipping) files in a large fact table based on filter criteria derived from a joined dimension table at runtime.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbx000101jxa9h0ylty/see?quizType=REAL_EXAM&page=144

## 148. lqd-148

Which command is used to add a new 'identity' column to an existing Delta table?

A. ALTER TABLE ... ADD COLUMN id BIGINT AUTO_INCREMENT

B. UPDATE TABLE ... SET id = row_number()

C. ALTER TABLE ... ADD COLUMN id BIGINT GENERATED ALWAYS AS IDENTITY

D. CREATE IDENTITY ON table_name (id)

**Source answer: C**

The correct syntax to add an identity column to an existing Delta table is ALTER TABLE ... ADD COLUMN ... GENERATED ALWAYS AS IDENTITY (or GENERATED BY DEFAULT AS IDENTITY). This feature is native to Delta Lake and ensures unique, auto-incrementing values.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbx000201jx320n05yo/see?quizType=REAL_EXAM&page=144

## 149. lqd-149

In a medallion architecture, why is it recommended to store the Bronze layer in Delta format even if the data is raw?

A. Because only Delta supports JSON string extraction.

B. Because Delta format automatically encrypts data.

C. Because Delta files are significantly smaller than Parquet.

D. To take advantage of Schema Enforcement and Time Travel even at the earliest stage.

**Source answer: D**

Storing the Bronze layer in Delta format brings all the benefits of Delta Lake, such as ACID transactions, Time Travel, Schema Enforcement, and easy streaming integration, right from the raw data ingestion phase.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pby000301jx3lu4vtk9/see?quizType=REAL_EXAM&page=144

## 150. lqd-150

What happens if a user accidentally runs 'VACUUM table RETAIN 0 HOURS'?

A. All files are immediately deleted.

B. The command fails due to a built-in safety check (unless explicitly disabled).

C. Only historical files older than 0 hours are deleted.

D. The command is ignored completely.

**Source answer: B**

By default, running a VACUUM command with a retention period of less than 168 hours (7 days) will throw an error. This built-in safety check prevents the accidental deletion of historical files that might still be in use by concurrent read operations or streaming jobs. To bypass this, the configuration spark.databricks.delta.retentionDurationCheck.enabled must be explicitly set to false.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pby000401jx0wtgg96a/see?quizType=REAL_EXAM&page=144

## 151. lqd-151

What is the correct syntax to hint Spark to broadcast a small table during a join?

A. OPTIMIZE FOR BROADCAST

B. SET spark.join.type='BROADCAST'

C. /*+ BROADCAST(small_table) */

D. WITH (BROADCAST)

**Source answer: C**

The correct syntax to apply a broadcast join hint in Spark SQL is to use a comment block right after the SELECT statement: SELECT /*+ BROADCAST(table_name) */ .... This instructs the Catalyst optimizer to broadcast the specified table to all worker nodes, speeding up the join.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pby000501jx491qzqid/see?quizType=REAL_EXAM&page=145

## 152. lqd-152

What is the primary difference between a Materialized View and a Streaming Table in a 2026 Lakeflow pipeline?

A. MV is only stored in the Silver layer.

B. Streaming Tables do not support Unity Catalog governance.

C. MV ensures data consistency by re-calculating results; Streaming Tables only append new data.

D. Only Streaming Tables can be scheduled.

**Source answer: C**

In Databricks Delta Live Tables (and Lakeflow), a Materialized View (MV) incrementally computes and maintains the exact result of a query, correctly handling updates, deletes, and aggregations. A Streaming Table is designed for append-only streaming data, processing each new input record exactly once.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmq247pby000601jxg1ao9sns/see?quizType=REAL_EXAM&page=145

## 153. lqd-153

When querying a table's Change Data Feed (CDF) for deleted records, which column should be filtered?

A. version_type

B. _change_type

C. _is_active

D. _operation

**Source answer: B**

When reading from a Delta table's Change Data Feed (CDF), Databricks automatically appends metadata columns to the query results. The _change_type column indicates the type of change for each row. To find deleted records, you filter where _change_type = 'delete'. Other values include insert, update_preimage, and update_postimage.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pby000701jxhcbu5shf/see?quizType=REAL_EXAM&page=145

## 154. lqd-154

How does Serverless SQL handle scaling differently than Classic SQL?

A. It scales down to zero instantly when idle and scales up instantly on demand.

B. Users manually assign extra nodes when slow.

C. It scales vertically by adding RAM to a single node.

D. It has a fixed size to guarantee costs.

**Source answer: A**

Serverless SQL warehouses in Databricks differ from Classic SQL warehouses primarily through their rapid elasticity. Because Databricks manages a fleet of warm compute instances behind the scenes, serverless warehouses can scale up almost instantly to handle concurrent demand and scale down to zero almost immediately when idle. This removes the slow startup times and long idle auto-stop wait times associated with Classic compute.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmq247pby000801jxgekxn9sl/see?quizType=REAL_EXAM&page=145

## 155. lqd-155

Which Unity Catalog privilege allows a user to see that a catalog exists in the UI without granting access to its data?

A. USAGE

B. SELECT

C. BROWSE

D. READ METADATA

**Source answer: C**

In Unity Catalog, the BROWSE privilege enables users to discover data by viewing the metadata (names, descriptions, existence) of securable objects like catalogs, schemas, and tables in the UI (Catalog Explorer) or via search. However, it does not grant them SELECT permission to read the actual data, nor does it grant USAGE, which is required to actually traverse the catalog or schema to query the objects within it.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pby000901jxwtbqgcc7/see?quizType=REAL_EXAM&page=145

## 156. lqd-156

In an Auto Loader job, what is the purpose of setting cloudFiles.schemaLocation?

A. To define the final Delta table path.

B. To persist the inferred schema for restarts and evolution.

C. To specify the source bucket.

D. To store the streaming checkpoint offsets.

**Source answer: B**

In a Databricks Auto Loader job, the cloudFiles.schemaLocation option specifies a directory where Auto Loader stores the inferred schema. By persisting the schema here, Auto Loader can accurately track schema evolution over time, identify new columns, and safely recover the schema state across pipeline restarts. (Note: Checkpoint offsets are stored in a separate checkpoint directory, though often managed closely together).

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000a01jxsro9pyul/see?quizType=REAL_EXAM&page=145

## 157. lqd-157

A data engineer wants to implement 'Lakeflow Connect'. Which source type is this feature specifically designed to handle natively?

A. Unstructured binary files.

B. IoT sensor data arriving via MQTT.

C. Relational databases and SaaS apps like Salesforce.

D. Emails sent to a workspace inbox.

**Source answer: C**

Databricks Lakeflow Connect is a feature designed to provide native, fully-managed connectors that simplify the ingestion of data from enterprise systems into the Lakehouse. It natively handles sources like relational databases (e.g., MySQL, PostgreSQL, SQL Server) and enterprise SaaS applications (e.g., Salesforce, ServiceNow, Workday).

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000b01jxftael762/see?quizType=REAL_EXAM&page=145

## 158. lqd-158

Which SQL command reveals the physical execution plan (e.g., verifying a Broadcast Join is used)?

A. DESCRIBE HISTORY

B. SHOW TBLPROPERTIES

C. ANALYZE TABLE

D. EXPLAIN EXTENDED

**Source answer: D**

The EXPLAIN command (and its variants like EXPLAIN EXTENDED) provides the logical and physical execution plans for a given SQL query, allowing you to verify how Spark will execute it, including details like Broadcast Joins.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000c01jxspvqg6wh/see?quizType=REAL_EXAM&page=146

## 159. lqd-159

What is the biggest risk of using Shallow Clones if the original production table is physically moved to a new bucket?

A. Storage costs will immediately double.

B. The clone will auto-move with the data.

C. The clone will break because its pointers to the original files are now invalid.

D. The production table becomes locked as read-only.

**Source answer: C**

A shallow clone only stores metadata and references the data files of the original table. If the original data files are moved or deleted directly (bypassing Delta management), the shallow clone's file pointers become invalid and it breaks.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000d01jxo3kxshiw/see?quizType=REAL_EXAM&page=146

## 160. lqd-160

If a DLT pipeline uses APPLY CHANGES INTO and a source record has a NULL sequence value, what happens?

A. DLT uses the system time automatically.

B. The record is dropped or causes the update to fail.

C. It is logged as the oldest history version.

D. It overwrites all history.

**Source answer: B**

In Delta Live Tables APPLY CHANGES INTO, a sequence column is required to correctly order operations. A NULL sequence value is invalid and causes the system to be unable to establish logical ordering, usually resulting in the record being dropped or causing a failure.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000e01jxjd66zue8/see?quizType=REAL_EXAM&page=146

## 161. lqd-161

What is a key technical restriction of using Serverless Jobs?

A. They only support SQL.

B. They have a strict 15-minute execution limit.

C. They cannot use manual cluster init scripts or custom Docker images.

D. They can only process CSV files.

**Source answer: C**

Serverless compute abstracts away the underlying infrastructure. Therefore, it does not support cluster-level customizations like manual init scripts or custom Docker containers that rely on direct OS/infrastructure access.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000f01jx9wymux40/see?quizType=REAL_EXAM&page=146

## 162. lqd-162

Which system table in Unity Catalog shows which specific columns are accessed most frequently?

A. _delta_log

B. system.billing.usage

C. system.access.column_lineage

D. stdout execution logs

**Source answer: C**

Unity Catalog provides built-in system tables for monitoring and auditing. The system.access.column_lineage table tracks lineage and access patterns at the column level, allowing users to understand which columns are frequently queried or depend on each other.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pbz000g01jxbn87m0vx/see?quizType=REAL_EXAM&page=146

## 163. lqd-163

A data engineer is using 'Liquid Clustering' on a table. How does this improve on traditional Z-Ordering?

A. It allows the data to be stored as a single giant file.

B. It converts Parquet files into a proprietary binary format.

C. It automatically encrypts the data.

D. It supports incremental clustering, adapting to query patterns without full rewrites.

**Source answer: D**

Liquid Clustering provides more flexibility than traditional Z-Ordering. It incrementally clusters data as it is written or optimized, and allows clustering keys to be changed without needing to rewrite the entire table. It efficiently adapts to changing query patterns.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmq247pc0000h01jxuhqwavs3/see?quizType=REAL_EXAM&page=146

## 164. lqd-164

Which file in a Databricks Asset Bundle (DAB) allows defining different cluster settings for 'Dev' and 'Prod' environments?

A. config.json

B. databricks.yml (using targets)

C. .gitignore

D. requirements.txt

**Source answer: B**

In Databricks Asset Bundles (DABs), the databricks.yml file is the central configuration file. You can define multiple targets (such as dev, staging, prod) within this file to specify environment-specific cluster settings, variables, and deployment behaviors.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000i01jx83ystipj/see?quizType=REAL_EXAM&page=146

## 165. lqd-165

A team needs to filter rows dynamically so UK analysts only see UK data. Which Unity Catalog feature handles this?

A. Shallow Clones

B. Column-level Security

C. Row-Level Security (RLS) Filter Functions

D. Creating separate Views manually

**Source answer: C**

Unity Catalog supports Row-Level Security (RLS) using filter functions. These allow you to define rules that evaluate dynamically based on the current user's identity or group memberships, limiting the rows returned to only those they are authorized to see.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000j01jxmukktmar/see?quizType=REAL_EXAM&page=147

## 166. lqd-166

In Unity Catalog, what is the difference between a Storage Credential and an External Location?

A. Credential is for S3; Location is for ADLS.

B. Credential holds the IAM identity; Location maps a path to that identity.

C. Credential is public; Location is private.

D. Credential creates managed tables; Location creates external tables.

**Source answer: B**

In Unity Catalog, a Storage Credential encapsulates a cloud IAM identity (like an AWS IAM role or Azure Service Principal) granting access to cloud storage. An External Location references a specific cloud storage path and associates it with a Storage Credential to authorize access to that exact location.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000k01jxt07sx9yu/see?quizType=REAL_EXAM&page=147

## 167. lqd-167

In Auto Loader, setting schemaEvolutionMode to 'rescue' causes new, unexpected columns to be:

A. Ignored and dropped.

B. Saved in a dedicated rescued data column.

C. Instantly added to the target schema.

D. Rejected and causes a stream failure.

**Source answer: B**

In Databricks Auto Loader, setting the schema evolution mode to 'rescue' (or using the default behavior which includes a rescued data column) captures any unexpected columns, mismatched data types, or malformed data into a dedicated JSON column (usually _rescued_data). This prevents data loss and stream failures while handling unexpected schema changes.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000l01jxqfgtaozy/see?quizType=REAL_EXAM&page=147

## 168. lqd-168

An engineer needs to physically roll a Delta table back to its state from 48 hours ago due to corruption. Which command is best?

A. RESTORE TABLE

B. VACUUM

C. SHALLOW CLONE

D. Time Travel SELECT

**Source answer: A**

The RESTORE TABLE command physically reverts a Delta table to a prior state based on a timestamp or version number. It modifies the table state to point to the historical version, rolling back any accidental or corruptive changes.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000m01jx5h7i83aq/see?quizType=REAL_EXAM&page=147

## 169. lqd-169

A company wants to share data with an external client using Delta Sharing. The client uses a different cloud provider and does not have a Databricks workspace. How do they access the data?

A. They must create a Databricks 'Community Edition' workspace.

B. By using an open-source Delta Sharing connector and a secure credential file.

C. They must use a VPN to connect directly.

D. They can only view the data as a static CSV export.

**Source answer: B**

Delta Sharing is an open standard that allows data sharing across different platforms. The recipient does not need a Databricks workspace. Instead, the provider can generate a secure credential file (.share file), which the recipient can use with open-source Delta Sharing connectors in their preferred tool (like Pandas, Spark, or Power BI) to securely query the shared data.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000n01jxnqu1grrg/see?quizType=REAL_EXAM&page=147

## 170. lqd-170

A join between two tables spills to disk because default shuffle partitions are too low. What is the modern way to optimize this?

A. Manually set spark.sql.shuffle.partitions to 2000.

B. Increase cluster RAM size.

C. Enable Adaptive Query Execution (AQE) to dynamically coalesce partitions.

D. Convert data to standard Parquet format.

**Source answer: C**

Adaptive Query Execution (AQE) dynamically optimizes query execution plans based on runtime statistics. One of its features is dynamically coalescing shuffle partitions, which optimizes the number of shuffle partitions based on actual data sizes to help prevent spilling to disk and improve execution speed.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc0000o01jx08kyepul/see?quizType=REAL_EXAM&page=147

## 171. lqd-171

Which DLT-specific command automatically manages versioning for a Slowly Changing Dimension (SCD) Type 2 table?

A. MERGE INTO

B. INSERT OVERWRITE

C. APPLY CHANGES INTO

D. CREATE LIVE TABLE

**Source answer: C**

In Delta Live Tables (DLT), the APPLY CHANGES INTO (in SQL) or apply_changes() (in Python) API is used to perform Change Data Capture (CDC). It can automatically manage versioning for Slowly Changing Dimension (SCD) Type 1 and Type 2 tables.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc1000p01jxjnfbmcya/see?quizType=REAL_EXAM&page=147

## 172. lqd-172

An engineer wants to add a new column to a Delta table by simply including it in a write operation. Which Spark option is used?

A. .option('overwriteSchema', 'true')

B. .option('mergeSchema', 'true')

C. .option('enforceSchema', 'false')

D. .option('autoSchema', 'true')

**Source answer: B**

To automatically evolve the schema of a Delta table when appending or overwriting data, you can use the .option("mergeSchema", "true") option. This will safely add new columns present in the DataFrame to the Delta table schema without breaking existing data.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc1000q01jxc1io7nli/see?quizType=REAL_EXAM&page=148

## 173. lqd-173

Which SQL syntax automatically assigns a new, unique incrementing integer to every row inserted?

A. AUTO_INCREMENT

B. GENERATED ALWAYS AS IDENTITY

C. SERIAL

D. DEFAULT NEXTVAL()

**Source answer: B**

In Databricks (Delta Lake), the syntax to create an auto-incrementing identity column is GENERATED ALWAYS AS IDENTITY or GENERATED BY DEFAULT AS IDENTITY. This ensures each new row receives a unique incrementing integer.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc1000s01jxu6t1ykci/see?quizType=REAL_EXAM&page=148

## 174. lqd-174

Which SQL command allows a user to view data in a table but explicitly prevents modification or deletion?

A. GRANT USAGE

B. GRANT SELECT

C. GRANT MODIFY

D. GRANT ALL PRIVILEGES

**Source answer: B**

The GRANT SELECT command provides read-only access to a table or view, allowing users to query and view data without granting them the ability to modify, insert, or delete the data (which would require MODIFY privileges).

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc1000t01jxhgxejsuw/see?quizType=REAL_EXAM&page=148

## 175. lqd-175

An administrator needs to audit which users have queried the 'salaries' table. Where do they look?

A. The _delta_log directory.

B. Cluster stdout logs.

C. The workspace trash bin.

D. The Unity Catalog System Tables (e.g., system.access).

**Source answer: D**

Unity Catalog provides System Tables that contain centralized, workspace-wide operational data. This includes audit logs (such as system.access.audit), which track user access, permissions, and query events across the Databricks account.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc1000w01jx3ru4dokt/see?quizType=REAL_EXAM&page=148

## 176. lqd-176

A notebook in a production Job needs to process data based on a 'region' parameter passed by the job. How should it retrieve this?

A. os.environ.get('region')

B. dbutils.widgets.get('region')

C. sys.argv[1]

D. spark.conf.get('region')

**Source answer: B**

In Databricks, parameters are passed to notebooks using widgets. dbutils.widgets.get('parameter_name') is the standard and correct way to retrieve job parameters (like task values or base parameters) passed to a notebook running as a task in a Databricks Job.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc2000x01jx3zd20cqi/see?quizType=REAL_EXAM&page=149

## 177. lqd-177

An engineer runs a VACUUM command. What is the default retention period before files are permanently deleted?

A. 24 hours

B. 7 days

C. 30 days

D. 0 hours

**Source answer: B**

The VACUUM command removes data files that are no longer referenced by a Delta table and are older than the retention threshold. By default, this threshold is 7 days (168 hours) to prevent accidental data loss and allow for point-in-time recovery via Time Travel.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc2000z01jxk813a3jl/see?quizType=REAL_EXAM&page=149

## 178. lqd-178

A team needs to ingest data directly from an external Salesforce instance. Which feature natively simplifies this?

A. Delta Sharing

B. Unity Catalog Federation

C. Lakeflow Connect

D. Databricks Repos

**Source answer: C**

Databricks Lakeflow Connect provides native, built-in connectors to easily ingest data from enterprise applications like Salesforce, ServiceNow, and databases directly into the Databricks Lakehouse. Unity Catalog Federation is for federating queries across external databases, Delta Sharing is for data sharing, and Databricks Repos is for Git integration.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc2001001jxit7r49ze/see?quizType=REAL_EXAM&page=149

## 179. lqd-179

A column 'json_payload' contains JSON strings. Which function converts these strings into a Spark Struct type?

A. to_json()

B. get_json_object()

C. from_json()

D. explode()

**Source answer: C**

The from_json() function parses a column containing a JSON string and converts it into a Spark Struct type (or Map/Array type) based on a provided schema. to_json() does the reverse (Struct to JSON string), get_json_object() extracts a specific string field from a JSON string, and explode() flattens arrays/maps into rows.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc2001201jx0444ls89/see?quizType=REAL_EXAM&page=149

## 180. lqd-180

What is the primary purpose of the 'databricks.yml' file in a Databricks Asset Bundle (DAB)?

A. To define the project's resources (Jobs, Pipelines) and deployment environments (Dev, Prod).

B. To store the user's personal Git credentials.

C. To act as a schema definition for the Delta tables.

D. To provide the row-level data for a unit test.

**Source answer: A**

Databricks Asset Bundles (DABs) use the databricks.yml file as the central configuration file. It defines the bundle metadata, resources (such as jobs, DLT pipelines, and models), and target environments (e.g., dev, staging, prod) for deployment.

Source copies: 2; distinct source versions: 2.

Source versions mark different answer text. See the preserved versions in the HTML/JSON collection.

Source: https://www.leetquiz.com/quiz/cmq247pc2001301jxhusd4egk/see?quizType=REAL_EXAM&page=149

## 181. lqd-181

A data engineer wants a fast copy of a table for testing, created in seconds without doubling storage costs. Which command is best?

A. SHALLOW CLONE

B. DEEP CLONE

C. CREATE TABLE AS SELECT

D. INSERT INTO

**Source answer: A**

A SHALLOW CLONE creates a copy of a table that only clones the metadata, not the underlying data files. This makes it extremely fast to create and does not increase storage costs immediately, which is ideal for short-lived testing.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001401jx2w1fslzn/see?quizType=REAL_EXAM&page=150

## 182. lqd-182

What is the primary technical goal of the 'Silver' layer?

A. Store raw logs for audit.

B. Serve high-level dashboards.

C. Provide a cleaned, filtered, and joined dataset as a source of truth.

D. Archive data long-term.

**Source answer: C**

In the Medallion Architecture, the Bronze layer stores raw data, the Silver layer provides a cleaned, filtered, and joined dataset acting as an enterprise source of truth, and the Gold layer is aggregated for BI and dashboards.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001601jxrgyp0jo1/see?quizType=REAL_EXAM&page=150

## 183. lqd-183

An Auto Loader stream is processing a folder with 50 million files. Listing takes 20 minutes before data flows. What is the solution?

A. Increase maxFilesPerTrigger

B. Enable File Notification mode

C. Increase cluster size

D. Z-Order the source directory

**Source answer: B**

Auto Loader's file notification mode is designed for directories with a massive number of files. Instead of listing directories (which takes a long time), it relies on cloud provider event services (like AWS SQS, Azure Event Grid) to receive notifications when new files arrive.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001701jxhckwj0to/see?quizType=REAL_EXAM&page=150

## 184. lqd-184

In a Job with multiple tasks, how can 'Task A' share a generated ID with 'Task B' downstream?

A. dbutils.jobs.taskValues.set()

B. Write to a DBFS file

C. Cluster environment variables

D. Notebook Widgets

**Source answer: A**

Databricks provides task values (dbutils.jobs.taskValues.set() and dbutils.jobs.taskValues.get()) to easily and securely pass small pieces of information, such as generated IDs or processing flags, between tasks within a Databricks Job workflow.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001801jx4fx4mdc9/see?quizType=REAL_EXAM&page=150

## 185. lqd-185

Which SQL structure is most efficient to view only the most recent update for each 'order_id' based on 'transaction_timestamp'?

A. GROUP BY

B. SELECT DISTINCT

C. Window Function (row_number() OVER ...)

D. Self-Join

**Source answer: C**

A Window Function using row_number() OVER (PARTITION BY order_id ORDER BY transaction_timestamp DESC) is the most efficient and standard SQL approach to isolate the latest record per ID without losing other column data. Databricks SQL makes this even easier by allowing the QUALIFY clause to filter the results in one step.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001901jx2p0rkcs3/see?quizType=REAL_EXAM&page=150

## 186. lqd-186

A downstream application needs a feed of every row-level insert, update, and delete made to a Silver table. Which feature provides this?

A. Deep Clone

B. Time Travel

C. Change Data Feed (CDF)

D. Vacuum

**Source answer: C**

Change Data Feed (CDF) allows you to track row-level changes between versions of a Delta table, capturing inserts, updates, and deletes along with the metadata. This is ideal for sending data changes to downstream applications incrementally.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc3001b01jx2u8j0s1e/see?quizType=REAL_EXAM&page=151

## 187. lqd-187

When joining a 10-billion-row table with a 5,000-row lookup table, which optimization avoids a massive data shuffle?

A. Z-Ordering

B. Broadcast Join

C. Partitioning

D. Liquid Clustering

**Source answer: B**

When joining a massive table with a very small lookup table (e.g., 5,000 rows), using a Broadcast Join (Broadcast Hash Join) is highly optimal. Spark broadcasts the smaller table to all worker nodes, avoiding a massive data shuffle of the large table over the network.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001c01jx2mwe8s57/see?quizType=REAL_EXAM&page=151

## 188. lqd-188

A data engineer needs to securely map an S3 bucket in Unity Catalog so users can query it without seeing raw access keys. What is used?

A. Secret Scope

B. DBFS Mount Point

C. Global Init Script

D. External Location and Storage Credential

**Source answer: D**

In Unity Catalog, you secure access to cloud storage (like an S3 bucket) using Storage Credentials (which securely encapsulate the IAM roles or access keys) and External Locations (which map a storage path to a storage credential). This allows users to access the data without ever seeing or handling raw access keys, unlike legacy DBFS mounts.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001d01jxkf2frjxr/see?quizType=REAL_EXAM&page=151

## 189. lqd-189

Which Databricks feature enables secure data sharing with external partners who do not have a Databricks workspace?

A. Unity Catalog Federation

B. Workspace Export

C. Delta Sharing

D. Public Dashboards

**Source answer: C**

Delta Sharing is an open standard protocol for secure data sharing with other organizations regardless of which computing platforms they use. It allows securely sharing data with external partners who do not use Databricks without requiring them to copy the data or create a Databricks account.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001e01jx3gywll8v/see?quizType=REAL_EXAM&page=151

## 190. lqd-190

What is a major operational benefit of using Serverless SQL Warehouses?

A. They allow SSH access to nodes.

B. They provide instant startup times for compute nodes.

C. They allow manual selection of node RAM sizes.

D. They are cheaper for jobs that run 24/7.

**Source answer: B**

Serverless SQL Warehouses abstract away infrastructure management and provide near-instant startup times for compute resources, which is a major operational benefit for ad-hoc querying and highly concurrent BI workloads. Serverless compute removes the need for managing instances and cluster configurations.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001f01jx5zs1h4r3/see?quizType=REAL_EXAM&page=151

## 191. lqd-191

Using Unity Catalog, how do you correctly reference a table named 'sales' in the 'retail' schema of the 'prod' catalog?

A. retail.sales

B. prod/retail/sales

C. cluster.prod.sales

D. prod.retail.sales

**Source answer: D**

Unity Catalog uses a 3-tier namespace format: catalog.schema.table. Therefore, a table named 'sales' in the 'retail' schema of the 'prod' catalog is correctly referenced as prod.retail.sales.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001g01jxj9loeh80/see?quizType=REAL_EXAM&page=151

## 192. lqd-192

In the Unity Catalog 3-tier namespace, what is the default catalog name if one is not explicitly specified?

A. default

B. main

C. root

D. hive_metastore

**Source answer: D**

For workspaces that were upgraded to Unity Catalog and have legacy tables, hive_metastore is often used as the default catalog for backward compatibility when a 2-tier namespace is referenced and no specific default catalog is configured. (Note: Some newly created workspaces may set main or a workspace-specific name as the default catalog, but hive_metastore represents the legacy default).

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc4001i01jx3so1kmpg/see?quizType=REAL_EXAM&page=152

## 193. lqd-193

An engineer needs to change the data types and properties of a table. Which privilege is required?

A. SELECT

B. USAGE

C. MODIFY

D. ALL PRIVILEGES (or Ownership)

**Source answer: D**

To alter a table's schema (such as changing data types or properties), a user typically needs to be the owner of the table or have ALL PRIVILEGES. The MODIFY privilege only allows inserting, updating, and deleting data, not altering the table's structure.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc5001j01jx0lrk0mbf/see?quizType=REAL_EXAM&page=152

## 194. lqd-194

Why might a dashboard take a few minutes to show updated results after a 'Refresh' button is clicked?

A. The data is being compressed.

B. The dashboard requires manual admin approval.

C. The assigned SQL Warehouse was stopped (Auto-Stop) and needs a few minutes to start up.

D. The internet connection is slowing query execution.

**Source answer: C**

If Auto-Stop is enabled, a SQL Warehouse will stop after a period of inactivity to save costs. When a dashboard refresh is triggered, the warehouse must start up again, which takes a few minutes before queries can run.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc5001l01jxwziks0gm/see?quizType=REAL_EXAM&page=152

## 195. lqd-195

Which Python f-string syntax correctly evaluates the variables 'store' and 'id' into a string like 'nyc_101'?

A. {store}{id}

B. f'{store}{id}'

C. f"(store)_(id)"

D. f"store_id"

**Source answer: B**

Python f-strings require the f prefix and curly braces {} to evaluate variables. Option B is valid f-string syntax (though it doesn't explicitly include an underscore, it is the only syntactically correct f-string evaluating variables among the choices, assuming the underscore might be part of the variable's value). Option C uses parentheses which will not evaluate the variables, treating them as literal text.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc7002401jx3kaa82va/see?quizType=REAL_EXAM&page=155

## 196. lqd-196

15. An external process appends Parquet files to a directory, but Databricks queries aren’t seeing them due to caching. What is the most reliable long-term solution?

A. Restart the Databricks cluster hourly.

B. Convert the table format to Delta Lake.

C. Run REFRESH TABLE before every read operation.

D. Move the files to a different cloud region.

**Source answer: B**

Delta Lake maintains an ACID-compliant transaction log that keeps a single source of truth of the files in the directory. By converting from plain Parquet to Delta Lake, Databricks will automatically consult the transaction log for the latest snapshot, completely eliminating the need to manually execute REFRESH TABLE or clear Spark's directory listings cache.

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/cmq247pc9002d01jx46gb7b76/see?quizType=REAL_EXAM&page=156

## 197. lqd-197

A data analyst has a SQL query against a Delta table, and the data engineering team wants to execute that query and work with its results in PySpark. Which operation should they use?

A. SELECT * FROM sales

B. spark.delta.table

C. spark.sql

D. spark.table

**Source answer: C**

spark.sql("<query>") executes a SQL query and returns a PySpark DataFrame, which can then be tested and transformed with Python. spark.table is appropriate when loading a table by name, but the requirement specifically describes executing an existing query.

Sign in to unlock 🔓
Powered By
GPT 5.6 Luna powered

Source copies: 1; distinct source versions: 1.

Source: https://www.leetquiz.com/quiz/r0oy4yf0cyj1t2sictjiy836/see?quizType=REAL_EXAM&page=161
