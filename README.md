# Intent-Based User Segmentation

This repository contains a Python-based project that processes user interaction data from multiple sources, including clickstream, search queries, and article views, to segment users based on their intent. The project demonstrates how machine learning techniques like K-Means clustering can be applied to identify different user engagement levels based on their behavior data.

## Key Features

- **Data Processing**: Aggregates user behavior data from multiple sources (clickstream, search queries, article views) using SQL.
- **User Segmentation**: Uses the K-Means clustering algorithm to segment users into groups based on their interaction patterns.
- **Visualization**: Provides clear visualizations of user segments based on total clicks and average time spent on articles, helping to understand different levels of engagement.
- **Integration**: The solution can be integrated into existing data pipelines or deployed as a standalone tool for analyzing user intent.

## How It Works

1. **Data Aggregation**: SQL queries are used to pull and aggregate user interaction data from various sources into a summary table.
2. **Clustering**: The data is then segmented using the K-Means algorithm, clustering users into different groups based on their activity.
3. **Visualization**: The segments are visualized to provide insights into user behavior, helping to identify low, moderate, and high-engagement users.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/peterduhon/intentsegments.git
    cd intentsegments
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the segmentation model:
    ```bash
    python load_and_train_model.py
    ```

## Visualizations

The script will generate scatter plots that show user engagement based on total clicks and time spent, with each user assigned to one of three segments:

- **Low Engagement**
- **Moderate Engagement**
- **Highly Engaged**


<img width="849" alt="Screenshot 2024-09-05 at 9 27 37 PM" src="https://github.com/user-attachments/assets/a943aeea-32b5-47d6-be5f-9255cf7afa8f">

  

## Technologies Used

- Python (with Pandas, Matplotlib, and Scikit-learn)
- SQL (for data aggregation)
- K-Means Clustering (for segmentation)
- MySQL (as the data warehouse)

---

### Skills Deployed

This project demonstrates a wide array of skills, particularly in the areas of **Data Science**, **Machine Learning**, **SQL**, and **Python**. Below is a breakdown of the key skills and technologies deployed throughout the project:

#### **1. SQL Skills:**
- **Data Aggregation**: SQL was used to gather and aggregate user interaction data from multiple sources, including clickstream data, search queries, and article views. Queries such as `GROUP BY`, `JOIN`, and `COUNT()` were used to consolidate data for each user.
- **Data Manipulation**: Using SQL, we manipulated and cleaned the data, including handling missing values (`NULL`) and calculating summary statistics like total clicks, average time spent on articles, and search queries. The project showcases complex SQL queries with multiple joins and the use of functions like `AVG()`, `ROUND()`, and `COUNT()`.
- **Database Management**: Created and altered database tables to store aggregated data, demonstrating schema design and optimization techniques.
- **Data Modeling**: The database schema design facilitated efficient storage of clickstream, article views, and search query data. SQL queries extracted essential features for clustering analysis.

#### **2. Python Skills:**
- **Data Processing with Pandas**: Utilized Python's `pandas` library for data manipulation and analysis. After loading the SQL data into a DataFrame, we performed data cleaning, including filling in missing values and calculating new columns.
- **Machine Learning (K-Means Clustering)**: Implemented K-Means clustering using `scikit-learn` to segment users based on multiple engagement metrics like total clicks, average time spent on articles, and search queries. The project demonstrates knowledge of unsupervised learning methods and clustering algorithms.
- **Data Visualization**: Used `matplotlib` to create scatter plots, color-coding users based on their engagement segments. This visualization helps in understanding the distribution of user behaviors and patterns, providing insights into user segments.
- **SQLAlchemy for Database Interaction**: Leveraged `SQLAlchemy` to interact with the MySQL database, demonstrating ORM (Object Relational Mapping) capabilities for clean and scalable database interaction.
  
#### **3. Data Science and Analytics Skills:**
- **Feature Engineering**: Engineered features such as total clicks, average time spent on articles, and total search queries to feed into the K-Means clustering model, showcasing a strong understanding of how to create meaningful features from raw data.
- **Clustering and Segmentation**: Applied K-Means clustering to segment users into distinct groups based on engagement behaviors, identifying "Low Engagement," "Moderate Engagement," and "Highly Engaged" users. This is critical for intent-based targeting.
- **Handling Missing Data**: Managed missing data by filling NaN values with column means, ensuring data quality and completeness before applying machine learning algorithms.
- **Real-Time Data and Batch Processing**: This project shows how to deal with data in both batch and real-time environments, particularly using SQL for batch data aggregation and Python for real-time model scoring.

#### **4. AdTech Domain Knowledge:**
- **Intent-Based Segmentation**: The core goal of this project—segmenting users based on their engagement metrics (clicks, search queries, and time spent on articles)—is directly applicable to advertising technology (AdTech), where intent-based targeting is key for improving ad relevancy and effectiveness.
- **User Behavior Analysis**: Demonstrates the ability to analyze user behavior across different digital touchpoints, such as websites and articles, creating actionable user segments.
