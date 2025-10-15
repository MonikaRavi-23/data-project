from kafka import KafkaConsumer
import json
from collections import defaultdict

consumer = KafkaConsumer(
    "cdc_topic",
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

data_store = defaultdict(float)

for message in consumer:
    record = message.value
    rid = record["record_id"]
    op = record["operation"]
    val = record["value"]

    if op == "insert":
        data_store[rid] = val
    elif op == "update":
        data_store[rid] = val
    elif op == "delete":
        if rid in data_store:
            del data_store[rid]

    print("Current Data:", dict(data_store))
