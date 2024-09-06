from sqlalchemy import create_engine
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create the SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:iP%40d2814ii@localhost/intent_based_segmentation')

# Updated query to fetch data from multiple sources
query = """
    SELECT 
        c.user_id,                                         -- User ID from clickstream
        COUNT(DISTINCT c.url) AS total_clicks,             -- Total clicks from clickstream
        COUNT(DISTINCT s.query) AS total_search_queries,   -- Total search queries
        ROUND(AVG(a.time_spent), 2) AS avg_time_spent_on_articles,  -- Avg time spent on articles
        ROUND(AVG(c.time_spent), 2) AS avg_time_spent_on_clicks     -- Avg time spent on clicks
    FROM 
        clickstream c
    LEFT JOIN 
        search_queries s ON c.user_id = s.user_id
    LEFT JOIN 
        article_views a ON c.user_id = a.user_id
    GROUP BY 
        c.user_id;
"""

# Load the data into a pandas DataFrame
df = pd.read_sql(query, engine)

# Fill NaN values with the mean of each column
df.fillna(df.mean(), inplace=True)

# Print the first few rows to verify the data
print(df.head())

# Run the KMeans clustering algorithm to segment users based on their engagement
X = df[['total_clicks', 'total_search_queries', 'avg_time_spent_on_articles', 'avg_time_spent_on_clicks']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['segment'] = kmeans.fit_predict(X)

# Mapping numeric labels to meaningful names
segment_names = {
    0: 'Low Engagement',
    1: 'Moderate Engagement',
    2: 'Highly Engaged'
}

# Add a new column for human-readable segment names
df['segment_name'] = df['segment'].map(segment_names)

# Optional: Print the first few rows to check the mapping
print(df[['user_id', 'segment', 'segment_name']].head())

# Visualize with the Final Chart Example
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['total_clicks'], df['avg_time_spent_on_articles'], c=df['segment'], cmap='viridis')
plt.colorbar(scatter, label='Segment')
plt.title('User Segmentation based on Clicks and Article Time Spent')
plt.xlabel('Total Clicks')
plt.ylabel('Average Time Spent on Articles (seconds)')

# Legend with segment names
legend_labels = [mpatches.Patch(color=plt.cm.viridis(segment / 2), label=segment_names[segment]) for segment in segment_names]
plt.legend(handles=legend_labels, title='Segment')

# Show plot
plt.show()

# Close the connection
engine.dispose()
