# 🔁 Incremental Data Processing Challenge 

> ⚡ Real-time model updates and data synchronization using **Change Data Capture (CDC)**, **Apache Kafka**, **Flink**, and **Python**.

---

## 🧠 Overview

This project demonstrates **Incremental Data Processing** using **CDC (Change Data Capture)** techniques — enabling systems to **react instantly to new or changed data**.  

When source data updates (in a database or stream), these changes are captured and processed incrementally using **Apache Kafka Connect**, then applied to update **data processing models or machine learning pipelines** (e.g., regression, clustering, or aggregations).

---

## 🧩 Task 3: Incremental Data Processing (CDC)

### 🎯 Objectives
- 🧩 Implement **Change Data Capture (CDC)** using **Kafka Connect**
- 🗃️ Capture and stream **database changes** in near real-time
- 📈 Process data incrementally and update **aggregations or ML models**
- 🔄 Maintain **consistency** between batch and streaming layers

🧰 **Tools Used:**  
**Apache Kafka** · **Apache Flink** · **Python** · **Kafka Connect** · **CDC Techniques**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

cd data-project
***2️⃣ Create & Activate Virtual Environment****
python3 -m venv streaming_env
source streaming_env/bin/activate   # Mac/Linux
streaming_env\Scripts\activate      # Windows

**3️⃣ Install Dependencies**
pip install -r ../requirements.txt

**4️⃣ Start Kafka & Zookeeper**

Make sure Kafka and Zookeeper are running before you start the CDC components.
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties

🚀 Run the CDC System

**▶️ Start CDC Producer**

Simulate or stream data change events (insert/update/delete) to a Kafka topic:
python3 cdc_producer.py

**▶️ Start CDC Consumer**
Consume the change stream and update downstream models or aggregations:
python3 cdc_consumer.py

**💡 How It Works**

🗄️ Source Database → generates changes (insert/update/delete)
🔗 Kafka Connect CDC Source (e.g., Debezium) captures these changes
🚀 Kafka Topic receives and streams events in real time
⚙️ Flink / Spark Streaming consumes events and applies updates
🧠 Python Model or Aggregation updates incrementally without full retraining
**ouput:**
![terminal ouptut](https://github.com/user-attachments/assets/7cd72598-d8c9-4548-8b0a-8efbaf5fc53a)
![terminal output](https://github.com/user-attachments/assets/94a5d6f5-5b87-49be-9467-9d9ccc1237f9)

