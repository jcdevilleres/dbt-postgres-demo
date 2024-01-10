# This is the Pythons script required to push the loans dataset to the PostgreSQL database
# I used the default values for host, user, password, and connection strings. Pleasure ensure that yours are updated correctly

import psycopg2
import csv

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="changeitnow!",
    host="localhost",
    port="5432"
)

# Create a cursor object using the connection
cur = conn.cursor()

# Path to your CSV file
csv_file_path = 'dataset/loan.csv'

# SQL statement to copy data from CSV into the 'loans' table
copy_sql = """
    COPY loans FROM stdin WITH CSV HEADER
    DELIMITER as ','
"""

# Open the CSV file and execute the COPY statement
with open(csv_file_path, 'r', encoding='utf-8') as f:
    cur.copy_expert(sql=copy_sql, file=f)
    conn.commit()

# Close cursor and connection
cur.close()
conn.close()
