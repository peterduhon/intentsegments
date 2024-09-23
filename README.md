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

## Roadmap: Intent-Based User Segmentation

| **Timeline**     | **Goals**                                                                                               | **Features**                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Current State**| - Segment users based on clicks, search queries, and time spent.                                         | - K-Means clustering with 3 segments: Low, Moderate, Highly Engaged.<br>- Visualizations of user segmentation.<br>- SQL and Python used for data processing.         |
| **3-Month**      | - Introduce real-time capabilities and more granular segmentation.                                       | - **Real-time data ingestion** using tools like **Kafka**.<br>- Increase segments from 3 to 5-7.<br>- Incorporate more data sources (e.g., video engagement, social media).<br>- Experiment with new clustering models.<br>- Start **A/B testing** segment performance. |
| **6-Month**      | - Scale platform, add predictive models, and cross-device tracking.                                      | - Add **predictive analytics** (XGBoost, Random Forest) to forecast user behavior.<br>- Implement **cross-device identity matching** with CDPs like **Segment**.<br>- Automated feedback loops for dynamic segment adjustments.<br>- Customize segmentation models for specific industries (e-commerce, media).<br>- **Multi-channel support** (email, SMS, push notifications). |
| **1-Year**       | - Fully scalable hybrid segmentation platform, RTB integration, advanced AI models.                     | - **Hybrid segmentation** combining ID-based and real-time approaches.<br>- Integrate with **Real-Time Bidding (RTB)** systems.<br>- Implement deep learning models (LSTM) for predicting evolving user intent.<br>- Dynamic user profiles tracking long-term and short-term behaviors.<br>- Monetize high-value segments via dynamic pricing.<br>- Optimize for **global expansion** with multi-language support. |



---

### **Current State of the Project**:

The **Intent-Based User Segmentation** project currently segments users into three engagement categories—**Low Engagement**, **Moderate Engagement**, and **Highly Engaged**—based on user interaction data, including **total clicks**, **search queries**, and **time spent on articles and clicks**. A clustering algorithm (K-Means) was applied to assign users to these segments, and the results are visualized using scatter plots to show distinct user segments.

#### **Current Features**:
- User interaction data (clickstream, search queries, article views) is aggregated from the database.
- Machine learning (K-Means clustering) is applied to create user segments.
- Visualizations present the engagement levels of users, allowing AdTech strategies to be tailored accordingly.
- SQL and Python are used for data aggregation, feature engineering, and model deployment.

---

### **3-Month Milestone**:

#### **Goal**: Introduce more granular segmentation and enhanced real-time capabilities.

- **Real-Time Data Ingestion**: Move towards real-time data processing, using event-driven tools like **Apache Kafka** or **Amazon Kinesis** to process clickstream and engagement data as it happens. 
- **Granular Segments**: Increase the number of segments beyond the current three (e.g., 5-7 segments) for more nuanced user targeting.
- **Add More Data Sources**: Integrate additional sources of user behavior data, such as video engagement, app usage, or social media interactions, to create a more holistic view of user intent.
- **Improve Model Accuracy**: Test alternative clustering models (e.g., **DBSCAN**, **Agglomerative Clustering**) to improve segmentation accuracy.
- **A/B Testing**: Begin experimenting with the performance of various segments, running A/B tests to compare the effectiveness of different ad strategies.

---

### **6-Month Milestone**:

#### **Goal**: Scale the platform and introduce predictive modeling.

- **Predictive Modeling**: Add **predictive analytics** to forecast future user behavior based on historical data, using machine learning models such as **XGBoost** or **Random Forest**. Predict the likelihood of a user becoming highly engaged or churning.
- **Cross-Device Identity Matching**: Implement **cross-device tracking** (using CDPs like **Segment** or **Tealium**) to ensure users are recognized across desktop, mobile, and tablet devices for better segmentation.
- **Automated Feedback Loops**: Automate the feedback loops to ensure that segment definitions dynamically adjust based on changing user behaviors.
- **Customization by Industry**: Customize segmentation models based on industry needs (e.g., e-commerce, media, financial services), offering industry-specific intent signals.
- **Multi-Channel Support**: Expand to support segmentation across **email**, **SMS**, and **push notifications**, integrating engagement data from these channels.

---

### **1-Year Milestone**:

#### **Goal**: Build out a fully scalable, real-time intent-based segmentation platform.

- **Full Integration with D/Cipher-Like Systems**: Build a hybrid segmentation system that combines both **ID-based** and **real-time targeting** approaches, fully integrating with a D/Cipher-like **Intent Targeting** tool.
- **Real-Time Bidding (RTB) Integration**: Integrate with **RTB (Real-Time Bidding)** systems to allow advertisers to bid on high-intent users in real-time, increasing the platform's ad revenue potential.
- **Advanced AI Models**: Incorporate deep learning models (e.g., **LSTM** for sequence prediction) to identify evolving user intent based on behavioral patterns across multiple sessions.
- **User Segment Profiles**: Build dynamic user profiles that track behavioral shifts over time, combining **historical behavior** and **real-time adjustments** for precision targeting.
- **Monetization of Segments**: Implement dynamic pricing for different user segments, allowing premium advertisers to bid more for the **Highly Engaged** users, while advertisers with broader goals target **Moderate Engagement** or **Low Engagement** users.
- **Global Expansion**: Optimize for multi-language and global scalability, allowing for broader adoption across international markets.

---

### **New Features & Considerations**:

- **Dynamic Segment Adjustment**: Implement dynamic recalibration of user segments based on both long-term trends and short-term fluctuations in behavior.
- **User Intent Scoring**: Introduce a **real-time user intent score** that evolves during a session, allowing for more fluid adjustments to ad targeting strategies.
- **Privacy-First Approach**: Focus on **privacy-preserving technologies** like **differential privacy** and **federated learning** to comply with GDPR/CCPA while maintaining high-quality data for segmentation.
- **Deeper Cross-Channel Analytics**: Integrate deeper cross-channel analytics to understand how users move between social, email, and web channels, using those insights for better segmentation.

---

This roadmap outlines a comprehensive plan for growing the **Intent-Based User Segmentation** project into a fully scalable AdTech tool. It focuses on scaling both the technical infrastructure and machine learning models to enhance real-time capabilities, predictive analytics, and cross-channel tracking.

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
