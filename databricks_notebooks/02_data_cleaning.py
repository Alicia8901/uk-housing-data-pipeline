from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

spark = SparkSession.builder.appName("UKHousingPipeline").getOrCreate()

df = spark.table("uk_house_prices")

# Compare the original row count with the row count after removing duplicates to identify duplicate records in the dataset.
df.count()
df.dropDuplicates().count()

# Remove duplicate rows to improve data quality before further transformations.
df=df.dropDuplicates()
df.count()

# Count the number of null values in each column to identify fields that may require cleaning or further investigation.
df.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df.columns
]).show()

# Save Cleaned Dataset
df.write.mode("overwrite").format("delta").saveAsTable("housing_cleaned")