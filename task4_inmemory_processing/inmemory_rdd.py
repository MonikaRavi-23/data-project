from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("InMemoryRDD").getOrCreate()
sc = spark.sparkContext

# Sample dataset
data = [(1, 10), (2, 20), (3, 30), (4, 40)]
rdd = sc.parallelize(data)

# Perform in-memory transformations
result = rdd.map(lambda x: (x[0], x[1]*2)).collect()
print("Transformed RDD:", result)

spark.stop()
