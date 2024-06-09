**combine_CSVs.py** - Combines any number of csv files into one, as long as they have the same structure.

**csv_to_sql.py** - takes a csv file as input and generates a sql script from the data. The resulting script will take the name of the csv file as the table name. Note: only creates varchar, integer, and number data types.
- usage: python3 csv_to_sql.py <example.csv>
 
**airflow_startup.sh** - shell script to install all of the requirements on a cli (ec2 instance usually for me) to get airflow installed and running.

**api_ingestion.py** - python script to ingest json data from a public or private api, and convert it to a csv file.

**basic_rest_api.py** - boilerplate for a Flask rest api. Works with sqlite database as functionality for adding, deleting, and updating records.

**combine_mp3s.py** - python script to combine mp3 audio files into one continuous file.
