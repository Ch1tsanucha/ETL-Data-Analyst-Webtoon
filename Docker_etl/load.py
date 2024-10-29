import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database connection parameters from environment variables
db_params = {
    'dbname': os.getenv('DB_NAME'),  # Database name
    'user': os.getenv('DB_USER'),          # Username
    'password': os.getenv('DB_PASSWORD'),      # Password
    'host': os.getenv('DB_HOST'),        # Host
    'port': os.getenv('DB_PORT')              # Port
}

# Read data from CSV into a DataFrame
df = pd.read_csv('data.csv')

try:
    # Establish the connection
    conn = psycopg2.connect(**db_params)
    print("Connection established.")

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # SQL command to drop the table if it exists
    drop_table_query = """
    DROP TABLE IF EXISTS public.webtoon;
    """
    
    # Execute the drop table command
    cursor.execute(drop_table_query)
    print("Old table 'webtoon' deleted if it existed.")

    # SQL command to create the new table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS public.webtoon (
        id SERIAL PRIMARY KEY,      -- Unique ID for each record
        category VARCHAR(255),      -- Category of the webtoon
        name VARCHAR(255),          -- Name of the webtoon
        author VARCHAR(255),        -- Author of the webtoon
        synopsis TEXT,              -- Synopsis of the webtoon
        read_number BIGINT,         -- Number of reads
        subscribe_number BIGINT,    -- Number of subscribers
        rate_number DECIMAL(3,2),   -- Rating (e.g., 9.74)
        date_first DATE,            -- First release date
        like_first BIGINT           -- Number of likes on first release
    );
    """

    # Execute the create table command
    cursor.execute(create_table_query)
    print("Table 'webtoon' created successfully.")

    # Insert data from DataFrame into the webtoon table
    for index, row in df.iterrows():
        insert_query = """
        INSERT INTO public.webtoon (category, name, author, synopsis, read_number, subscribe_number, rate_number, date_first, like_first)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (row['Category'], row['Name'], row['Author'], row['Synopsis'], 
                                       row['Read_Number'], row['Subscribe_Number'], row['Rate_Number'], 
                                       row['Date_First'], row['Like_First']))
    
    print(f"Inserted {len(df)} rows into 'webtoon' table.")

    # Commit the changes to the database
    conn.commit()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Connection closed.")
