# Real-Time and Incremental Data Processing Project

## Overview
This repository contains projects demonstrating real-time data streaming and incremental data processing using Apache Kafka, Spark, and Python. The project is divided into multiple tasks:

1. **Real-Time Data Streaming** (Task 1)  
   - Producer-Consumer application using Apache Kafka.
   - Real-time processing with Apache Spark Structured Streaming.
   - Basic analytics on incoming data streams, e.g., rolling averages.
   - Tools: Kafka, Spark, Python, Scikit-learn.

2. **Incremental Data Processing with Change Data Capture (CDC)** (Task 3)  
   - CDC system using Apache Kafka Connect to capture database/data stream changes.
   - Incremental updates to machine learning models or aggregations.
   - Tools: Kafka, Python, CDC techniques.



## Repository Structure

data-project/
│
├── producer.py # Kafka producer for Task 1
├── consumer.py # Kafka consumer for Task 1
├── spark_streaming.py # Spark Structured Streaming script for Task 1
├── requirements.txt # Python dependencies for Task 1 & 3
├── .gitignore # Exclude virtual environment and other unnecessary files
├── task3_incremental_processing/
│ ├── cdc_producer.py # Producer for CDC Task 3
│ ├── cdc_consumer.py # Consumer for CDC Task 3
│ └── requirements.txt # Python dependencies for Task 3
└── streaming_env/ # Python virtual environment (excluded via .gitignore)

yaml
Copy code

---

## Setup Instructions

1. **Clone the repository**

git clone https://github.com/MonikaRavi-23/data-project.git
cd data-project
Create & activate Python virtual environment


python3 -m venv streaming_env
source streaming_env/bin/activate
Install dependencies


pip install -r requirements.txt
Start Kafka & Zookeeper


bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
Run Task 1: Real-Time Streaming


python3 producer.py
python3 consumer.py
python3 spark_streaming.py
Run Task 3: Incremental Processing (CDC)


python3 task3_incremental_processing/cdc_producer.py
python3 task3_incremental_processing/cdc_consumer.py
Key Features
Real-time streaming analytics using Kafka & Spark.

Incremental data processing via CDC techniques.

Rolling averages, aggregation, and ML model updates.

Fully containerized Python environment with dependency management.
