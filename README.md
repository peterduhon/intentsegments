# Intent-Based User Segmentation

This repository contains a Python script that processes user interaction data (e.g., clickstream, search queries, and article views) and applies machine learning algorithms to segment users based on their intent.

## Features
- **SQL Data Aggregation**: Extracts and aggregates data from user behavior (clickstream, search queries, and article views).
- **KMeans Clustering**: Segments users into three categories based on engagement (Low, Moderate, High).
- **Data Visualization**: Generates a scatter plot visualizing user segmentation based on clicks and time spent.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/peterduhon/intentsegments.git
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv segmentation_env
    source segmentation_env/bin/activate  # For Windows use: segmentation_env\Scripts\activate
    ```

3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python load_and_train_model.py
    ```

## Data Sources
- **Clickstream Data**: Records user clicks and time spent on specific URLs.
- **Search Queries**: Tracks user search behavior.
- **Article Views**: Logs the time spent reading articles by users.

## Technologies
- Python
- MySQL
- SQLAlchemy
- KMeans Clustering
- Matplotlib for visualization
