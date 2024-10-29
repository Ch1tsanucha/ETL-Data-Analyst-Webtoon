import psycopg2
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
