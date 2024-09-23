import mysql.connector
import os
import sys

# Retrieve the database password from the environment variable
db_password = os.getenv('DB_PASSWORD')
if not db_password:
    sys.exit("Error: The DB_PASSWORD environment variable is not set.")


# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="intent_based_segmentation"
)

cursor = connection.cursor()


# Insert aggregated data into user_activity_summary from all relevant sources
cursor.execute("""
    INSERT INTO user_activity_summary (user_id, total_clicks, avg_time_spent, total_search_queries)
    SELECT
        c.user_id,
        COUNT(DISTINCT c.url) AS total_clicks,                -- Total clicks from clickstream
        ROUND((AVG(c.time_spent) + AVG(a.time_spent)) / 2, 2) AS avg_time_spent,  -- Average time spent across both clickstream and article views
        COUNT(DISTINCT s.query) AS total_search_queries       -- Total search queries from search_queries
    FROM
        clickstream c
    LEFT JOIN
        search_queries s ON c.user_id = s.user_id
    LEFT JOIN
        article_views a ON c.user_id = a.user_id
    GROUP BY
        c.user_id
""")

# Commit the changes
connection.commit()

# Close the connection
connection.close()
