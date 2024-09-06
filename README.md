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

## Technologies Used

- Python (with Pandas, Matplotlib, and Scikit-learn)
- SQL (for data aggregation)
- K-Means Clustering (for segmentation)
- MySQL (as the data warehouse)
