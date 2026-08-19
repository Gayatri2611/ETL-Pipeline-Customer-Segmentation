# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Income_Spending_ETL") \
    .getOrCreate()

# Source file
source_path = "/Volumes/etlpipelineincome/default/bronze/Income_Spending_200Rows (1).csv"

# Bronze output
bronze_path = "/Volumes/etlpipelineincome/default/bronze/raw_income"

# Read CSV
df_bronze = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(source_path)

# Check data
df_bronze.show(10)
df_bronze.printSchema()

# Save Bronze as Delta
df_bronze.write \
    .format("delta") \
    .mode("overwrite") \
    .save(bronze_path)

print("Bronze layer created successfully")