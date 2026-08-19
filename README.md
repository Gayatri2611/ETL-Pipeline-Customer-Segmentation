# ETL Pipeline & Customer Segmentation

## 📌 Project Overview

This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** using **PySpark and Databricks** to process customer income and spending data.

The pipeline follows a **Bronze → Silver → Gold** architecture. The processed data is then used for **K-Means customer segmentation** and visualized through a **Power BI dashboard**.

## 🏗️ Architecture

```text
Raw CSV Data
     ↓
Bronze Layer
(Raw Data)
     ↓
Silver Layer
(Cleaned & Transformed Data)
     ↓
Gold Layer
(Analytics-Ready Data)
     ↓
K-Means Clustering
     ↓
Customer Segments
     ↓
Power BI Dashboard
```

## 🛠️ Technologies Used

* Python
* PySpark
* Databricks
* Delta Lake
* K-Means Clustering
* Power BI
* Git & GitHub
* Jupyter Notebook

## 📊 Dataset

The project uses a customer income and spending dataset containing **200 customer records**.

Key attributes include:

* Customer ID
* Income
* Spending Score

These features are used to identify groups of customers with similar characteristics.

## 🔄 ETL Pipeline

### 🥉 Bronze Layer

The Bronze layer stores the raw customer data after ingestion.

Main operations:

* Read source CSV data
* Preserve the original data structure
* Store the ingested data for further processing

### 🥈 Silver Layer

The Silver layer performs data preparation and transformation.

Main operations include:

* Data cleaning
* Data transformation
* Selecting relevant features
* Preparing the dataset for machine learning

### 🥇 Gold Layer

The Gold layer contains analytics-ready data used for customer segmentation.

The processed customer data is passed to the machine learning stage for clustering.

## 🤖 Customer Segmentation

**K-Means clustering** is used to group customers based on their income and spending behavior.

The resulting clusters represent different customer segments that can be analyzed for business decision-making.

## 📈 Power BI Dashboard

The final segmented data is visualized using **Power BI**.

The dashboard helps analyze:

* Customer distribution
* Income and spending patterns
* Customer segments
* Cluster-level insights

## 📂 Project Structure

```text
ETL-Pipeline-Customer-Segmentation/
│
├── data/
│   └── Income_Spending_200Rows.csv
│
├── images/
│   ├── bronze_layer.png
│   ├── silver_layer.png
│   ├── kmeans_clusters.png
│   └── powerbi_dashboard.png
│
├── notebooks/
│   ├── Bronze layer.ipynb
│   ├── Silver layer.ipynb
│   └── Gold layer.ipynb
│
├── powerbi/
│   └── Customer_Segmentation_Report.pbix
│
└── src/
```

## 🎯 Project Outcome

The project demonstrates how raw customer data can be transformed through an **ETL pipeline**, prepared for machine learning, segmented using **K-Means clustering**, and finally presented through an interactive **Power BI dashboard**.

## 👩‍💻 Author

**Gayatri Jadhav**

GitHub: [Gayatri2611](https://github.com/Gayatri2611)
