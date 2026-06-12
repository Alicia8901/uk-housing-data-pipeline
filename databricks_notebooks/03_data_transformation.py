from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month, avg, round, count

spark = SparkSession.builder.appName("UKHousingPipeline").getOrCreate()

df = spark.table("housing_cleaned")

# Create Sale Year Column
df = df.withColumn("sale_year", year(df.date))
df.select("date", "sale_year").show(5)

# Create Sale Month Column
df = df.withColumn("sale_month", month(df.date))
df.select("date", "sale_year", "sale_month").show(5)

# Average House Price by District
avg_price_by_district = df.groupBy("district") \
    .agg(round(avg("price"), 2).alias("average_price")) \
    .orderBy("average_price", ascending=False)

avg_price_by_district.show(10)

# Average House Price by Property Type
avg_price_by_property = df.groupBy("property_type") \
    .agg(round(avg("price"), 2).alias("average_price")) \
    .orderBy("average_price", ascending=False)

avg_price_by_property.show()

# New Build vs Existing Property Analysis
new_build_analysis = df.groupBy("new_build") \
    .agg(round(avg("price"), 2).alias("average_price")) \
    .orderBy("average_price", ascending=False)

new_build_analysis.show()

# Freehold vs Leasehold Analysis
freehold_analysis = df.groupBy("freehold") \
    .agg(round(avg("price"), 2).alias("average_price")) \
    .orderBy("average_price", ascending=False)

freehold_analysis.show()

# Average House Price by Year
avg_price_by_year = df.groupBy("sale_year") \
    .agg(round(avg("price"), 2).alias("average_price")) \
    .orderBy("sale_year")

avg_price_by_year.show()

# Housing Transactions by Year
transactions_by_year = df.groupBy("sale_year") \
    .agg(count("*").alias("transactions")) \
    .orderBy("sale_year")

transactions_by_year.show()

df.write.mode("overwrite").format("delta").saveAsTable("housing_transformed")

df.write.mode("overwrite").saveAsTable("housing_transformed")