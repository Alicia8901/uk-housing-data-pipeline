'''This notebook loads the UK housing dataset into a Spark DataFrame and performs initial inspection checks, including table validation, schema inspection, and row count checks.'''

from pyspark.sql import SparkSession

# A Spark session is the entry point for using PySpark. It allows us to read, process, and transform large datasets using Spark.

spark=SparkSession.builder.appName("UKHousingPipeline").getOrCreate()

# The housing data was uploaded into Databricks as a table and loaded into a Spark DataFrame for processing.
spark.sql("SHOW TABLES").show()

# Display the first five rows to understand the structure of the dataset.
df=spark.table("uk_house_prices")
df.show(5)

# Check column names and data types to confirm that fields such as price and date have been imported correctly.
df.printSchema()
df.count()