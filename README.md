# ETL-Pipeline
This is a Automated Data Pipeline . This project implements an automated end-to-end data pipeline using Apache Hadoop, Spark, and Hive, orchestrated by Apache Airflow. The pipeline ingests data from the local file system, uploads it to HDFS, transforms it using Spark, stores the cleaned data in Hive tables, and finally exports it back to the local system. Airflow DAGs manage and schedule each step, ensuring modular, scalable, and fault-tolerant data processing.

Architecture : (This Pipeline is accordance with the Linux Virtual Machine ) The data will come to local file system data_ingest folder.It will be loaded to HDFS in raw format. The raw data in data_ingest will be moved to old_data directory making data_ingest folder always ready for new fresh data. From HDFS spark will take over and transform the data and load the clean data in hive . Hive can provide SQL like queries on data and finally from Hive data is exported to local file system (hive_export directory). All this is automated by Airflow.

Files Discription:

notebook.py : Transformation and loading

csv_export.hive : Hive script for exporting data into local

hadoop_ingest.sh : shell script , it will upload data to hdfs

hadoo_clear.sh : it will remove raw data from hadoop once it is loaded into spark

      +--------------------+
      | data_ingest/ (new) |
      +--------+-----------+
               |
     Move to: old_data/
               |
       Upload to HDFS
               ↓
     +------------------+
     |     HDFS (raw)   |
     +--------+---------+
              ↓
   Spark Transformation (cleaning, parsing)
              ↓
     +------------------+
     |   Hive (cleaned) |
     +--------+---------+
              ↓
   Export to hive_export/ (local)
              ↓
     Orchestrated by Airflow DAG
