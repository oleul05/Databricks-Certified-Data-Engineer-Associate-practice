# LeetQuiz May 2026 syllabus review

[Exam guide](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf)

Human study-priority judgments against the listed objectives. Similar foundational concepts are kept even when product names changed; cosmetic updates are yellow. Behavior and answer corrections are disclosed separately. This is not an official Databricks excluded-question list.

Downloaded bank: 197 reviewed → 147 kept, 50 excluded. Original refined bank: 77 reviewed and retained.

This audit records the syllabus-filtering stage. The subsequent ExamTopics overlap audit in ../examtopics-deduplication-audit.md records additional removals from the active sets. The raw downloaded collection and all source versions remain in downloads.

## Excluded downloaded questions

| Source ID | Question | Reason |
| --- | --- | --- |
| lqd-009 | Question 6  Two junior data engineers are authoring separate parts of a single data pipeline notebook. They are working on separate Git branches so they can pair program on the same notebook simultaneously. A senior data engineer experienced in Databricks suggests there is a better alternative for this type of collaboration.  Which of the following supports the senior data engineer’s claim? | Notebook coauthoring feature trivia is not a listed Git-development objective. |
| lqd-012 | Question 11  A data engineering team needs to query a Delta table to extract rows that all meet the same condition. However, the team has noticed that the query is running slowly. The team has already tuned the size of the data files. Upon investigating, the team has concluded that the rows meeting the condition are sparsely located throughout each of the data files.  Based on the scenario, which of the following optimization techniques could speed up the query? | Legacy Z-Ordering-specific layout selection is not a cosmetic rename to Liquid Clustering; the current guide names Liquid Clustering and predictive optimization. |
| lqd-013 | Question 12  A data engineer needs to create a database called customer360 at the location /customer/customer360. The data engineer is unsure if one of their colleagues has already created the database.  Which of the following commands should the data engineer run to complete this task? | Legacy Hive/DBFS database location or external-Parquet cache behavior is outside the Unity Catalog-focused operations in the guide. |
| lqd-016 | Question 15 A data engineering team has created a series of tables using Parquet data stored in an external system. The team is noticing that after appending new rows to the data in the external system, their queries within Databricks are not returning the new rows. They identify the caching of the previous data as the cause of this issue.  Which of the following approaches will ensure that the data returned by queries is always up-to-date? | Legacy Hive/DBFS database location or external-Parquet cache behavior is outside the Unity Catalog-focused operations in the guide. |
| lqd-020 | Question 22  A data analyst has provided a data engineering team with the following Spark SQL query:  SELECT district,        avg(sales) FROM store_sales_20220101 GROUP BY district;   The data analyst would like the data engineering team to run this query every day. The date at the end of the table name (20220101) should automatically be replaced with the current date each time the query is run.  Which of the following approaches could be used by the data engineering team to efficiently automate this process? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-026 | Question 24  A data engineer needs to dynamically create a table name string using three Python variables: region, store, and year. An example of a table name is below when region = "nyc", store = "100", and year = "2021":  nyc100_sales_2021  Which of the following commands should the data engineer use to construct the table name in Python? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-037 | Question 36 A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE.  The table is configured to run in Development mode using the Triggered Pipeline Mode.  Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline? | Development/production and continuous/triggered declarative-pipeline compute lifecycle trivia is not listed. |
| lqd-038 | Question 42  A data engineering team has been using a Databricks SQL query to monitor the performance of an ELT job. The ELT job is triggered by a specific number of input records being ready to process. The Databricks SQL query returns the number of minutes since the job's most recent runtime.  Which of the following approaches can enable the data engineering team to be notified if the ELT job has not been run in an hour? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-043 | Question 41  An engineering manager uses a Databricks SQL query to monitor their team's progress on fixes related to customer-reported bugs. The manager checks the results of the query every day, but they are manually rerunning the query each day and waiting for the results.  Which of the following approaches can the manager use to ensure the results of the query are updated each day? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-044 | A data engineer has created a new database using the following command: CREATE DATABASE IF NOT EXISTS customer360;  In which of the following locations will the customer360 database be located? | Legacy Hive/DBFS database location or external-Parquet cache behavior is outside the Unity Catalog-focused operations in the guide. |
| lqd-048 | Question 43  A data engineering manager has noticed that each of the queries in a Databricks SQL dashboard takes a few minutes to update when they manually click the “Refresh” button. They are curious why this might be occurring, so a team member provides a variety of reasons on why the delay might be occurring. Which of the following reasons fails to explain why the dashboard might be taking a few minutes to update? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-052 | A data engineer only wants to execute the final block of a Python program if the Python variable day_of_week is equal to 1 and the Python variable review_period is True.  Which of the following control flow statements should the data engineer use to begin this conditionally executed code block? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-058 | CREATE TABLE customersInFrance  CREATE TABLE customersInFrance _______ AS SELECT id,        firstName,        lastName, FROM customerLocations WHERE country = 'FRANCE';   A senior data engineer mentions that it is organization policy to include a table property indicating that the new table includes personally identifiable information (PII). Which of the following lines of code fills in the above blank to successfully complete the task? | PII COMMENT syntax alone does not implement the listed masking, row filters, or ABAC policies. |
| lqd-062 | A data analyst has a series of queries in a SQL program. The data analyst wants this program to run every day. They only want the final query in the program to run on Sundays. They ask for help from the data engineering team to complete this task. Which of the following approaches could be used by the data engineering team to complete this task? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-064 | A data engineer needs to apply custom logic to identify employees with more than 5 years of experience in array column employees in table stores. The custom logic should create a new column exp_employees that is an array of all of the employees with more than 5 years of experience for each row. In order to apply this custom logic at scale, the data engineer wants to use the FILTER higher-order function. Which of the following code blocks successfully completes this task? | Higher-order array FILTER/custom SQL UDF creation and PIVOT are not the explicitly listed explode, column manipulation, and DataFrame aggregation objectives. |
| lqd-076 | A data engineer that is new to using Python needs to create a Python function to add two integers together and return the sum. Which of the following code blocks can the data engineer use to complete this task? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-089 | A data engineer has been using a Databricks SQL dashboard to monitor the cleanliness of the input data to an ELT job. The ELT job has its Databricks SQL query that returns the number of input records containing unexpected NULL values. The data engineer wants their entire team to be notified via a messaging webhook whenever this value reaches 100. Which of the following approaches can the data engineer use to notify their entire team via a messaging webhook whenever the number of NULL values reaches 100? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-092 | A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE. The table is configured to run in Development mode using the Continuous Pipeline Mode. Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline? | Development/production and continuous/triggered declarative-pipeline compute lifecycle trivia is not listed. |
| lqd-101 | A Delta Live Table pipeline includes two datasets defined using STREAMING LIVE TABLE. Three datasets are defined against Delta Lake table sources using LIVE TABLE. The table is configured to run in Production mode using the Continuous Pipeline Mode. Assuming previously unprocessed data exists and all definitions are valid, what is the expected outcome after clicking Start to update the pipeline? | Development/production and continuous/triggered declarative-pipeline compute lifecycle trivia is not listed. |
| lqd-106 | A data engineer needs to apply custom logic to string column city in table stores for a specific use case. In order to apply this custom logic at scale, the data engineer wants to create a SQL user-defined function (UDF). Which of the following code blocks creates this SQL UDF? | Higher-order array FILTER/custom SQL UDF creation and PIVOT are not the explicitly listed explode, column manipulation, and DataFrame aggregation objectives. |
| lqd-115 | Which of the following SQL keywords can be used to convert a table from a long format to a wide format? | Higher-order array FILTER/custom SQL UDF creation and PIVOT are not the explicitly listed explode, column manipulation, and DataFrame aggregation objectives. |
| lqd-122 | Which of the following approaches should be used to send the Databricks Job owner an email in the case that the Job fails? | Job email-notification setup is outside the listed task/control-flow, scheduling, and UI-status objectives. |
| lqd-125 | An engineering manager wants to monitor the performance of a recent project using a Databricks SQL query. For the first week following the project's release, the manager wants the query results to be updated every minute. However, the manager is concerned that the compute resources used for the query will be left running and cost the organization a lot of money beyond the first week of the project's release.  Which of the following approaches can the engineering team use to ensure the query does not cost the organization any money beyond the first week of the project's release? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-126 | Where in the Spark UI can one diagnose a performance problem induced by not leveraging predicate push-down? | Predicate push-down plans, EXPLAIN syntax, and Dynamic File Pruning feature trivia are not the listed stage-metric bottlenecks or tuning parameters. |
| lqd-131 | In order to prevent accidental commits to production data, a senior data engineer has instituted a policy that all development work will reference clones of Delta Lake tables. After testing both DEEP and SHALLOW CLONE, development tables are created using SHALLOW CLONE.  A few weeks after initial table creation, the cloned versions of several tables implemented as Type 1 Slowly Changing Dimension (SCD) stop working. The transaction logs for the source tables show that VACUUM was run the day before.  Which statement describes why the cloned tables are no longer working? | Shallow/deep clone behavior and clone-specific recovery are not listed basic managed/external table operations. |
| lqd-134 | A task orchestrator has been configured to run two hourly tasks. First, an outside system writes Parquet data to a directory mounted at /mnt/raw_orders/. After this data is written, a Databricks job containing the following code is executed:  (spark.readStream   .format("parquet")   .load("/mnt/raw_orders/")   .withWatermark("time", "2 hours")   .dropDuplicates(["customer_id", "order_id"])   .writeStream   .trigger(once=True)   .table("orders") )   Assume that the fields customer_id and order_id serve as a composite key to uniquely identify each order, and that the time field indicates when the record was queued in the source system.  If the upstream system is known to occasionally enqueue duplicate entries for a single order hours apart, which statement is correct? | Streaming watermark horizon/state-retention semantics are beyond the listed basic DataFrame deduplication objective. |
| lqd-137 | The data governance team is reviewing code used for deleting records for compliance with GDPR. The following logic has been implemented to propagate delete requests from the user_lookup table to the user_aggregates table.  (spark.read   .format("delta")   .option("readChangeData", True)   .option("startingTimestamp", '2021-08-22 00:00:00')   .option("endingTimestamp", '2021-08-29 00:00:00')   .table("user_lookup")   .createOrReplaceTempView("changes"))  spark.sql(""" DELETE FROM user_aggregates WHERE user_id IN (   SELECT user_id   FROM changes   WHERE _change_type='delete' ) """)   Assuming that user_id is a unique identifying key and that all users that have requested deletion have been removed from the user_lookup table, which statement describes whether successfully executing the above logic guarantees that the records to be deleted from the user_aggregates table are no longer accessible and why? | Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives. |
| lqd-138 | The data engineering team has been tasked with configuring connections to an external database that does not have a supported native connector with Databricks. The external database already has data security configured by group membership. These groups map directly to user groups already created in Databricks that represent various teams within the company.  A new login credential has been created for each group in the external database. The Databricks Utilities Secrets module will be used to make these credentials available to Databricks users.  Assuming that all the credentials are configured correctly on the external database and group membership is properly configured on Databricks, which statement describes how teams can be granted the minimum necessary access to using these credentials? | Legacy dbutils secret-scope ACL configuration is outside the listed Unity Catalog UI/SQL privileges and masking objectives. |
| lqd-139 | Which statement describes a key benefit of an end-to-end test? | Generic end-to-end testing terminology is not one of the listed CI/CD deployment objectives. |
| lqd-141 | The data science team has created and logged a production model using MLflow. The model accepts a list of column names and returns a new column of type DOUBLE.  The following code correctly imports the production model, loads the customers table containing the customer_id key column into a DataFrame, and defines the feature columns needed for the model.  model = mlflow.pyfunc.spark_udf(spark, model_uri="models:/churn/prod") df = spark.table("customers") columns = ["account_age", "time_since_last_seen", "app_rating"]   Which code block will output a DataFrame with the schema "customer_id LONG, predictions DOUBLE"? | MLflow model inference and Dialogflow voice integration are outside this data-engineering exam outline. |
| lqd-143 | A large company seeks to implement a near real-time solution involving hundreds of pipelines with parallel updates of many tables with extremely high volume and high velocity data.  Which of the following solutions would you implement to achieve this requirement? | Legacy extreme-throughput cluster-topology guarantees cannot be retained through a product-name-only update. |
| lqd-145 | You are a retailer that wants to integrate your online sales capabilities with different in-home assistants, such as Google Home. You need to interpret customer voice commands and issue an order to the backend systems. Which solutions should you choose? | MLflow model inference and Dialogflow voice integration are outside this data-engineering exam outline. |
| lqd-147 | What is the primary purpose of 'Dynamic File Pruning' in Databricks? | Predicate push-down plans, EXPLAIN syntax, and Dynamic File Pruning feature trivia are not the listed stage-metric bottlenecks or tuning parameters. |
| lqd-148 | Which command is used to add a new 'identity' column to an existing Delta table? | Identity-column generation/ALTER restrictions are outside the listed basic column manipulation and table-lifecycle objectives. |
| lqd-153 | When querying a table's Change Data Feed (CDF) for deleted records, which column should be filtered? | Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives. |
| lqd-158 | Which SQL command reveals the physical execution plan (e.g., verifying a Broadcast Join is used)? | Predicate push-down plans, EXPLAIN syntax, and Dynamic File Pruning feature trivia are not the listed stage-metric bottlenecks or tuning parameters. |
| lqd-159 | What is the biggest risk of using Shallow Clones if the original production table is physically moved to a new bucket? | Shallow/deep clone behavior and clone-specific recovery are not listed basic managed/external table operations. |
| lqd-160 | If a DLT pipeline uses APPLY CHANGES INTO and a source record has a NULL sequence value, what happens? | Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives. |
| lqd-162 | Which system table in Unity Catalog shows which specific columns are accessed most frequently? | System-table lineage/access-frequency and query-audit lookups are not the listed governance controls. |
| lqd-169 | A company wants to share data with an external client using Delta Sharing. The client uses a different cloud provider and does not have a Databricks workspace. How do they access the data? | Delta Sharing recipients/connectors are not listed in the guide. |
| lqd-171 | Which DLT-specific command automatically manages versioning for a Slowly Changing Dimension (SCD) Type 2 table? | Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives. |
| lqd-173 | Which SQL syntax automatically assigns a new, unique incrementing integer to every row inserted? | Identity-column generation/ALTER restrictions are outside the listed basic column manipulation and table-lifecycle objectives. |
| lqd-175 | An administrator needs to audit which users have queried the 'salaries' table. Where do they look? | System-table lineage/access-frequency and query-audit lookups are not the listed governance controls. |
| lqd-181 | A data engineer wants a fast copy of a table for testing, created in seconds without doubling storage costs. Which command is best? | Shallow/deep clone behavior and clone-specific recovery are not listed basic managed/external table operations. |
| lqd-186 | A downstream application needs a feed of every row-level insert, update, and delete made to a Silver table. Which feature provides this? | Detailed Delta Change Data Feed fields, GDPR propagation code, and SCD Type 2 sequence handling are not listed ingestion/cleaning objectives. |
| lqd-189 | Which Databricks feature enables secure data sharing with external partners who do not have a Databricks workspace? | Delta Sharing recipients/connectors are not listed in the guide. |
| lqd-192 | In the Unity Catalog 3-tier namespace, what is the default catalog name if one is not explicitly specified? | A fixed default catalog name is workspace/session dependent; default-catalog trivia is not an explicit objective. |
| lqd-194 | Why might a dashboard take a few minutes to show updated results after a 'Refresh' button is clicked? | SQL-editor/dashboard refresh schedules, alert destinations, and refresh behavior are not Lakeflow Jobs scheduling or run-history monitoring. |
| lqd-195 | Which Python f-string syntax correctly evaluates the variables 'store' and 'id' into a string like 'nyc_101'? | Standalone Python strings, functions, and control-flow syntax are not listed; Lakeflow Jobs conditional tasks are the listed control-flow objective. |
| lqd-196 | 15. An external process appends Parquet files to a directory, but Databricks queries aren’t seeing them due to caching. What is the most reliable long-term solution? | Legacy Hive/DBFS database location or external-Parquet cache behavior is outside the Unity Catalog-focused operations in the guide. |

## Retained questions and objective mapping

| Source ID | Section | Objective |
| --- | --- | --- |
| lqd-001 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-002 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-003 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-004 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-005 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-006 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-007 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-008 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-010 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-011 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-014 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-015 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-017 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-018 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-019 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-021 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-022 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-023 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-024 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-025 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-027 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-028 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-029 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-030 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-031 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-032 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-033 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-034 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-035 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-036 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-039 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-040 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-041 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-042 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-045 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-046 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-047 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-049 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-050 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-051 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-053 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-054 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-055 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-056 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-057 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-059 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-060 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-061 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-063 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-065 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-066 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-067 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-068 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-069 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-070 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-071 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-072 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-073 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-074 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-075 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-077 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-078 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-079 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-080 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-081 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-082 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-083 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-084 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-085 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-086 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-087 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-088 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-090 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-091 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-093 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-094 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-095 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-096 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-097 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-098 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-099 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-100 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-102 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-103 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-104 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-105 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-107 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-108 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-109 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-110 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-111 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-112 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-113 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-114 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-116 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-117 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-118 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-119 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-120 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-121 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-123 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-124 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-127 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-128 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-129 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-130 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-132 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-133 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-135 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-136 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-140 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-142 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-144 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-146 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-149 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-150 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-151 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-152 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-154 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-155 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-156 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-157 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-161 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-163 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-164 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-165 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-166 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-167 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-168 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-170 | Optimization | Section 6: job run monitoring, Spark bottlenecks/tuning, library/startup diagnosis, or Delta file-layout maintenance supporting optimization. |
| lqd-172 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-174 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-176 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-177 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-178 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-179 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-180 | CI/CD | Section 5: workspace Git development, environment configuration, bundles, or CLI management of automated workspace assets. |
| lqd-182 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-183 | Ingestion | Section 2: batch/streaming/incremental ingestion, Auto Loader schema/discovery, COPY INTO, connectors, JDBC, and nested input. |
| lqd-184 | Lakeflow Jobs | Section 4: notebook/pipeline tasks, parameters, dependencies, retries, scheduling, and task control flow. |
| lqd-185 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-187 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |
| lqd-188 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-190 | Platform | Section 1: platform architecture, Delta Lake/Unity Catalog foundations, or compute characteristics and workload selection. |
| lqd-191 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-193 | Governance | Section 7: Unity Catalog managed/external lifecycle, hierarchy, UI/SQL privileges, ownership, or row filters. |
| lqd-197 | Transformation | Section 3: reading/cleaning Bronze, DataFrame/SQL joins, column/row manipulation, deduplication, aggregates, Gold objects, or validation. |

## Corrections beyond product renames

### lqd-005

- Updated legacy database USAGE assumptions to Unity Catalog parent privileges, qualified the table, and quoted the principal.

### lqd-010

- Restored the full schema/command and question prompt from a complete downloaded source version.

### lqd-014

- Kept the managed-versus-external creation concept; replaced legacy DBFS storage assumptions with Unity Catalog managed storage.

### lqd-028

- Corrected the source example to use spark.readStream.table before writeStream; spark.table produces a batch DataFrame.

### lqd-032

- Corrected the source example to use spark.readStream.table before writeStream; spark.table produces a batch DataFrame.

### lqd-047

- Qualified the Unity Catalog table, quoted the principal, and clarified the scope of ALL PRIVILEGES.

### lqd-050

- Corrected the source answer from increasing warehouse size to using serverless SQL for a cold-start delay.

### lqd-055

- Updated the legacy USAGE-for-discovery question to the Unity Catalog BROWSE privilege; this is a behavior correction, not a product rename.

### lqd-059

- Qualified the Unity Catalog schema and clarified that ALL PRIVILEGES is not ownership and does not include every privilege.

### lqd-080

- Corrected the source example to use spark.readStream.table before writeStream; spark.table produces a batch DataFrame.

### lqd-090

- Restored the missing command placeholder in the downloaded prompt.

### lqd-094

- Removed a stray minus sign and legacy LIVE qualifier, and corrected the claim that STREAM requires a streaming-table source.

### lqd-098

- Corrected the source example to use spark.readStream.table before writeStream; spark.table produces a batch DataFrame.

### lqd-103

- Restored the full schema/command and question prompt from a complete downloaded source version.

### lqd-107

- Replaced the legacy workspace-admin-only ownership claim with Unity Catalog authorization.

### lqd-109

- Removed the obsolete claim that merge must be performed outside the workspace; the Git branch-integration concept is retained.

### lqd-117

- Updated immediate-deletion wording to the Unity Catalog recovery and asynchronous-purge behavior.

### lqd-118

- Restored the target-key matching scenario missing from the downloaded choices; deleting the source table is not a reason to choose MERGE.

### lqd-121

- Clarified the ambiguous workload question and removed the incorrect second marked answer for conventional batch workloads.

### lqd-127

- Clarified SQL-query execution and corrected the extra marked spark.table option for this requirement.

### lqd-136

- Updated the membership check to account groups for Unity Catalog while retaining the same row-security condition.

### lqd-142

- Made the discovery-mode assumption explicit rather than claiming that all Auto Loader configurations have a fixed default.

### lqd-146

- Updated the legacy LIVE namespace requirement while retaining the pipeline dataset-reference concept.

### lqd-152

- Scoped the append-only claim to an append-only source; it is not a universal statement about every streaming-table flow.

### lqd-154

- Removed unsupported instant-scale-to-zero and instant-startup guarantees.

### lqd-170

- Corrected the source recommendation to coalesce partitions when the stated problem is too few large partitions.

### lqd-174

- Clarified that granting SELECT does not explicitly deny or revoke pre-existing modification privileges.

### lqd-190

- Replaced the absolute instant-startup guarantee with fast startup.

### lqd-193

- Specified the ALTER operations and corrected the least-privilege answer to MODIFY.

## Yellow name updates

| Old term | Updated term |
| --- | --- |
| CREATE STREAMING LIVE TABLE | CREATE OR REFRESH STREAMING TABLE |
| CREATE INCREMENTAL LIVE TABLE | CREATE OR REFRESH STREAMING TABLE |
| CREATE OR REFRESH LIVE TABLE | CREATE OR REFRESH MATERIALIZED VIEW |
| CREATE LIVE TABLE | CREATE OR REFRESH MATERIALIZED VIEW |
| STREAMING LIVE TABLE | STREAMING TABLE |
| LIVE TABLE | MATERIALIZED VIEW |
| Databricks Lakehouse Platform | Databricks Data Intelligence Platform |
| Databricks Lakehouse Architecture | Databricks Data Intelligence Platform architecture |
| Delta Live Tables | Lakeflow Spark Declarative Pipelines |
| Delta Live Table | Lakeflow Spark Declarative Pipeline |
| DLT | Lakeflow Spark Declarative Pipelines |
| Databricks Asset Bundles | Declarative Automation Bundles |
| Databricks Asset Bundle | Declarative Automation Bundle |
| Databricks Repos | Databricks Git Folders |
| Databricks Repo | Databricks Git Folder |
| Repos | Git Folders |
| SQL endpoint | SQL warehouse |
| SQL endpoints | SQL warehouses |
| Data Explorer | Catalog Explorer |
| Databricks Jobs | Lakeflow Jobs |
| Databricks Job | Lakeflow Job |
| Jobs UI | Lakeflow Jobs UI |
| Jobs page | Jobs & Pipelines page |
| is_member | is_account_group_member |
