"""
1. Import necessary libraries. 
2. Load source MySQL and destination Postgres connection details.
3. Build connection strings and create database engines.
4. Read products table from MySQL and load into a dataframe.
5. Write dataframe to products table in Postgres. (raw schema)
"""

# %%
#Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
# %%
# Load environment variables from .env file
load_dotenv()
# %%
os.environ['MYSQL_USER']

# %%
# MySQL database connection details 
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_host = os.environ['MYSQL_HOST']
mysql_db = os.environ['MYSQL_DB']

# Postgres database connection details 
pg_user = os.environ['PG_USER']
pg_password = os.environ['PG_PASSWORD']
pg_host = os.environ['PG_HOST']
pg_db = os.environ['PG_DB']
# %%
# Build connection strings
mysql_conn_string = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_string = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_string)
pg_engine = create_engine(pg_conn_string)
# %%
# Read products table from MySQL
df = pd.read_sql('SELECT * FROM products', mysql_engine)
# %%
df
# %%
# Write dataframe to products table in Postgres (raw schema)
df.to_sql('products', pg_engine, schema='raw', if_exists='append', index=False)

# %%

print(f'{len(df)} records loaded into Postgres products table.')