from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

spark = SparkSession.builder.appName("KafkaStreaming").getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","sensor-data") \
    .option("startingOffsets","earliest") \
    .load()

schema = StructType([
    StructField("sensor_id", IntegerType()),
    StructField("temperature", FloatType()),
    StructField("humidity", FloatType())
])

json_df = df.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")

avg_df = json_df.groupBy("sensor_id").avg("temperature","humidity")

query = avg_df.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()
