import pandas as pd
import psycopg2
import os

# Read the CSV file
df = pd.read_csv("/Users/dennismain/Documents/Netflix_algorithm/data.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="netflix_db",  
    user="postgres",             
    password="netflix_project",    
    port=5432
)
print(conn.get_dsn_parameters())
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS public.events (
    timestamp TIMESTAMP,
    user_id VARCHAR,
    movie_id VARCHAR,
    genre VARCHAR,
    action VARCHAR,
    duration INT
);
""")
conn.commit()

# Insert data
for row in df.itertuples(index=False):
    cur.execute("""
INSERT INTO public.events (timestamp, user_id, movie_id, genre, action, duration)
VALUES (%s, %s, %s, %s, %s, %s)
""", tuple(row))

conn.commit()
cur.close()
conn.close()

print("✅ Data successfully inserted into PostgreSQL!(or already exists)")