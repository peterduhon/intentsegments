# Standard library imports
import os
import sys
import random
import datetime
import urllib.parse

# Third-party imports
from dotenv import load_dotenv
import mysql.connector


# Load environment variables from .env file
load_dotenv()

# Debugging: Print the environment variable
# print(f"DB_PASSWORD from os.environ: {os.environ.get('DB_PASSWORD')}")

db_password = os.getenv('DB_PASSWORD')
if not db_password:
    sys.exit("Error: The DB_PASSWORD environment variable is not set.")

# URL-encode the password
db_password_encoded = urllib.parse.quote_plus(db_password)

# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="intent_based_segmentation"
)

cursor = connection.cursor()

# Function to generate synthetic article views data
def generate_article_views_data(num_records):
    data = []
    for _ in range(num_records):
        user_id = random.randint(1, 1000)  # Assuming user IDs range from 1 to 1000
        timestamp = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
        article_id = random.randint(1, 100)  # Assuming 100 different articles
        time_spent = random.randint(30, 300)  # Time spent in seconds
        data.append((user_id, timestamp, article_id, time_spent))
    return data

# Generate 1000 records of synthetic data for article_views
article_views_data = generate_article_views_data(1000)

# Insert data into the article_views table
insert_query = "INSERT INTO article_views (user_id, timestamp, article_id, time_spent) VALUES (%s, %s, %s, %s)"
cursor.executemany(insert_query, article_views_data)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
