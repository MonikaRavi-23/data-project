# 🧠 Task 4: In-Memory Data Processing Challenge 

> ⚡ High-performance data analytics using **in-memory computation** with **Apache Spark** (RDDs & DataFrames).

## 🌐 Overview

This task demonstrates **in-memory data processing** using **Apache Spark** to efficiently handle large datasets.  
By leveraging **Resilient Distributed Datasets (RDDs)** and **DataFrames**, computations are optimized to minimize disk I/O and deliver **real-time analytics** performance.  

💡 The focus is on **speed, scalability, and memory efficiency** — processing massive data volumes directly in memory rather than relying on slow disk operations.

## 🧰 Tools Used

| Tool | Purpose |
|------|----------|
| 🔥 **Apache Spark** | Distributed, in-memory data processing engine |
| 🐍 **Python (PySpark)** | High-level API for Spark operations |
| 💾 **RDDs / DataFrames** | In-memory data structures for transformations & analytics |


## 📁 Files in This Task

| File | Description |
|------|--------------|
| `inmemory_rdd.py` | Demonstrates data processing using **Spark RDDs**, including transformations and actions. |
| `inmemory_dataframe.py` | Demonstrates data analytics using **Spark DataFrames**, with column operations and aggregations. |
| `requirements.txt` | Lists all dependencies required to run this task in a virtual environment. |

## ⚙️ Instructions to Run

### 1️⃣ Activate Python Virtual Environment
source streaming_env/bin/activate

**2️⃣ Run the RDD Example**
python3 inmemory_rdd.py

**3️⃣ Run the DataFrame Example**
python3 inmemory_dataframe.py

**🚀 Key Concepts Demonstrated**
Concept	Description
⚡ In-Memory Computation	Perform analytics directly in memory for high-speed processing.
🔄 RDD Transformations & Actions	Apply map, filter, reduce operations efficiently.
🧱 DataFrame Operations	Use schema-based queries and column manipulations for analytics.
📊 Performance Optimization	Compare execution time improvements with in-memory caching.
🧠 Real-Time Analytics	Demonstrate near-instant query execution and aggregation.
**output:**
![terminal output](https://github.com/user-attachments/assets/7e91f420-acf4-4781-b6fa-493b80e52b5a)
![terminal output](https://github.com/user-attachments/assets/47cef239-e9c3-4667-8766-4f68469c59cc)


