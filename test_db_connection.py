import psycopg2
import dj_database_url
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch DATABASE_URL
database_url = os.getenv("DATABASE_URL")

if not database_url:
    print("Error: DATABASE_URL not found in environment variables.")
    exit(1)

print(f"Testing connection to: {database_url.split('@')[1] if '@' in database_url else '...'}")

# Parse the URL
db_config = dj_database_url.parse(database_url)

# Connect to the database
try:
    connection = psycopg2.connect(
        user=db_config['USER'],
        password=db_config['PASSWORD'],
        host=db_config['HOST'],
        port=db_config['PORT'],
        dbname=db_config['NAME']
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")
