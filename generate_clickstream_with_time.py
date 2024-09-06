import random
import datetime
import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="iP@d2814ii",  # Replace with your MySQL password
    database="intent_based_segmentation"
)

cursor = connection.cursor()

# Function to generate synthetic data for clickstream with time_spent
def generate_clickstream_data(num_records):
    data = []
    for _ in range(num_records):
        user_id = random.randint(1, 1000)
        timestamp = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
        url = f"https://example.com/page{random.randint(1, 100)}"
        referrer = random.choice(["https://google.com", "https://facebook.com", "https://twitter.com", None])
        device = random.choice(["desktop", "mobile", "tablet"])
        time_spent = random.randint(5, 300)  # Time spent in seconds (between 5 and 300 seconds)
        data.append((user_id, timestamp, url, referrer, device, time_spent))
    return data

# Generate and insert clickstream data with time_spent into the database
clickstream_data = generate_clickstream_data(1000)
for record in clickstream_data:
    cursor.execute("""
        INSERT INTO clickstream (user_id, timestamp, url, referrer, device, time_spent)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, record)

# Commit the changes
connection.commit()

# Close the connection
connection.close()

print("Clickstream data with time_spent added to the database.")
