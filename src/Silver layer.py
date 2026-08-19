# Databricks notebook source
from pyspark.sql.functions import col

# --------------------------------
# SILVER LAYER
# --------------------------------

# Bronze Delta path
bronze_path = "/Volumes/etlpipelineincome/default/bronze/raw_income"

# Silver output path
silver_path = "/Volumes/etlpipelineincome/default/bronze/silver/clean_income"

# Read Bronze Delta
df_silver = spark.read \
    .format("delta") \
    .load(bronze_path)

# Remove duplicate rows
df_silver = df_silver.dropDuplicates()

# Remove rows containing NULL values
df_silver = df_silver.dropna()

# Show cleaned data
df_silver.show(10)

# Check schema
df_silver.printSchema()

# Save Silver as Delta
df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .save(silver_path)

print("Silver layer created successfully")

# COMMAND ----------

df_silver.columns

# COMMAND ----------

# Delete old Silver Delta table
dbutils.fs.rm(
    "/Volumes/etlpipelineincome/default/bronze/silver/clean_income",
    True
)

print("Old Silver table deleted")

# COMMAND ----------

from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans

# --------------------------------
# PATHS
# --------------------------------

bronze_path = "/Volumes/etlpipelineincome/default/bronze/raw_income"

silver_path = "/Volumes/etlpipelineincome/default/bronze/silver/clean_income"

# --------------------------------
# 1. READ BRONZE
# --------------------------------

df_silver = spark.read \
    .format("delta") \
    .load(bronze_path)

# --------------------------------
# 2. CLEAN DATA
# --------------------------------

df_silver = df_silver.dropDuplicates()

df_silver = df_silver.dropna()

# --------------------------------
# 3. CREATE FEATURES
# --------------------------------

assembler = VectorAssembler(
    inputCols=["Income", "SpendingScore"],
    outputCol="features"
)

df_silver = assembler.transform(df_silver)

# --------------------------------
# 4. SCALE FEATURES
# --------------------------------

scaler = StandardScaler(
    inputCol="features",
    outputCol="scaled_features",
    withMean=True,
    withStd=True
)

scaler_model = scaler.fit(df_silver)

df_silver = scaler_model.transform(df_silver)

# --------------------------------
# 5. K-MEANS
# --------------------------------

kmeans = KMeans(
    k=4,
    seed=42,
    featuresCol="scaled_features",
    predictionCol="KMeans_Cluster"
)

kmeans_model = kmeans.fit(df_silver)

df_silver = kmeans_model.transform(df_silver)

import matplotlib.pyplot as plt

# Convert required columns to Pandas
plot_df = df_silver.select(
    "Income",
    "SpendingScore",
    "KMeans_Cluster"
).toPandas()

# Scatter plot
plt.figure(figsize=(10, 6))

plt.scatter(
    plot_df["Income"],
    plot_df["SpendingScore"],
    c=plot_df["KMeans_Cluster"],
    s=50
)

plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("K-Means Customer Segmentation")
plt.colorbar(label="K-Means Cluster")

plt.show()

# --------------------------------
# 6. VIEW RESULT
# --------------------------------

df_silver.select(
    "CustomerID",
    "Income",
    "SpendingScore",
    "KMeans_Cluster"
).show(20)

# --------------------------------
# 7. SAVE SILVER
# --------------------------------

df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .save(silver_path)

print("Silver layer with K-Means created successfully")