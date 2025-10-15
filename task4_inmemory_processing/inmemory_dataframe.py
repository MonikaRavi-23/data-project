from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("InMemoryDF").getOrCreate()

data = [(1, 10), (2, 20), (3, 30), (4, 40)]
columns = ["id", "value"]

df = spark.createDataFrame(data, columns)

# In-memory transformation
df_transformed = df.withColumn("value_double", col("value")*2)
df_transformed.show()

spark.stop()
