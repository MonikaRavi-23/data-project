# ----------------------------
# Imports and Spark Session
# ----------------------------
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from pyspark.ml.feature import VectorAssembler, MinMaxScaler  # Import missing classes

spark = SparkSession.builder.appName("DataPreprocessingChallenge").getOrCreate()

# ----------------------------
# Step 1: Read CSV
# ----------------------------
df = spark.read.csv("Mall_Customers.csv", header=True, inferSchema=True)
print("Original Dataset:")
df.show(5)

# ----------------------------
# Step 2: Handle Missing Values
# ----------------------------
df = df.dropna(subset=['CustomerID'])
print("After dropping rows with missing CustomerID:")
df.show(5)

# ----------------------------
# Step 3: Remove Duplicates
# ----------------------------
df = df.dropDuplicates()
print("After removing duplicates:")
df.show(5)

# ----------------------------
# Step 4: Data Type Conversion
# ----------------------------
df = df.withColumn("Age", col("Age").cast("integer")) \
       .withColumn("AnnualIncome", col("Annual Income (k$)").cast("double")) \
       .withColumn("SpendingScore", col("Spending Score (1-100)").cast("double"))
print("After type conversion:")
df.show(5)

# ----------------------------
# Step 5: Feature Engineering
# ----------------------------
df = df.withColumn("Income_Per_Age", col("AnnualIncome") / col("Age"))
print("After feature engineering (Income_Per_Age):")
df.show(5)

# ----------------------------
# Step 6: Normalization / Standardization
# ----------------------------
assembler = VectorAssembler(inputCols=["Age","AnnualIncome","SpendingScore","Income_Per_Age"], outputCol="features")
df_vector = assembler.transform(df)

scaler = MinMaxScaler(inputCol="features", outputCol="scaledFeatures")
scaler_model = scaler.fit(df_vector)
df_scaled = scaler_model.transform(df_vector)

print("After normalization (scaled features):")
df_scaled.select("features","scaledFeatures").show(5)
