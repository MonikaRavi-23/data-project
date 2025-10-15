# Real-Time Data Streaming using Kafka and Apache Spark

This project demonstrates a real-time data streaming pipeline using **Apache Kafka** as a message broker and **Apache Spark Structured Streaming** for real-time analytics.  
It was developed and tested inside **WSL (Ubuntu)** environment.

## 🚀 Project Overview

The system consists of three main components:

1. **Producer (`producer.py`)** – Sends streaming data (messages) to a Kafka topic.
2. **Consumer (`consumer.py`)** – Reads and verifies messages from the Kafka topic.
3. **Spark Streaming (`spark_streaming.py`)** – Processes data in real-time using Spark Structured Streaming and displays live analytics.

## 🏗️ Project Structure

data-project/
│
├── producer.py # Kafka producer script
├── consumer.py # Kafka consumer script
├── spark_streaming.py # Spark Structured Streaming script
├── requirements.txt # Python dependencies
├── .gitignore # Excludes virtual environment folder
└── streaming_env/ # Local virtual environment (ignored in git)

## ⚙️ Setup Instructions

### 1️⃣ Create and Activate Virtual Environment

python3 -m venv streaming_env
source streaming_env/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Start Zookeeper and Kafka

# In separate terminals
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties

4️⃣ Create Kafka Topic
kafka-topics.sh --create --topic realtime-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

5️⃣ Run Producer & Consumer
python3 producer.py
python3 consumer.py

6️⃣ Run Spark Streaming Script
python3 spark_streaming.py

🧩 Output Example
Spark reads the stream and prints processed results in real-time:

Batch: 1
-------------------------------------------
+---------+---------------+
| keyword | message_count |
+---------+---------------+
| kafka   | 5             |
| spark   | 8             |
+---------+---------------+

🧠 Technologies Used
1.Apache Kafka – Real-time message streaming
2.Apache Spark – Structured Streaming engine
3.Python (PySpark) – Scripting and analysis
4.WSL (Ubuntu) – Linux environment on Windows
