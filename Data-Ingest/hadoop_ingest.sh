
#!/bin/bash
hdfs dfs -put /home/talentum/ProjectDBDA/data_ingest/*.cs
mv /home/talentum/ProjectDBDA/data_ingest/*.csv  /home/talentum/ProjectDBDA/old_data

