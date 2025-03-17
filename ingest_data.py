import argparse

from datetime import datetime

import pandas as pd

parser = argparse.ArgumentParser(description = 'Ingest data from a CSV file into a database')

#user ,password, host, port, database name,table name

parser.add_argument('user',help ='user name for postrgres')
parser.add_argument('pass',help ='password for postrgres')
parser.add_argument('host',help ='host for postrgres')
parser.add_argument('port',help ='port for postrgres')
parser.add_argument('db',help ='database name for postrgres')
parser.add_argument('table-name',help ='name of the table where we will write the results')
parser.add_argument('url',help ='path to the CSV file to ingest')

args = parser.parse_args()
print(args.accumulate(args.integers))

df = pd.read_csv('/Users/allakkihome/Downloads/yellow_tripdata_2021-01.csv')


print(pd.io.sql.get_schema(df,name = "yellow_taxi"))



df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


from sqlalchemy import create_engine


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

engine.connect()


print(pd.io.sql.get_schema(df,name = 'taxi',con=engine))



import psycopg2



df_iter = pd.read_csv('/Users/allakkihome/Downloads/yellow_tripdata_2021-01.csv',iterator =True,chunksize =100000)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)



df.head(n=0).to_sql(name ='taxi', con = engine,if_exists = 'replace')


get_ipython().run_line_magic('time', "df.head(n=0).to_sql(name ='taxi_data', con = engine,if_exists = 'append')")

with engine.connect() as conn:
    result = conn.execute('SELECT COUNT(*) FROM yellow_taxi_data')
    print(result.fetchall())  

df_iter = pd.read_csv('/Users/allakkihome/Downloads/yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

# Looping through each chunk and writing it to the database
for chunk in df_iter:
    # This assumes you have already created the engine
    chunk.to_sql(name='taxi', con=engine, if_exists='append', index=False)

print("Data successfully written to the taxi table!")


with engine.connect() as conn:
    result = conn.execute("SELECT COUNT(*) FROM taxi")
    print(result.fetchall())







