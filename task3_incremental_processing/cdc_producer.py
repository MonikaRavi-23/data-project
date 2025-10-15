from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "record_id": random.randint(1, 100),
        "value": random.random()*100,
        "operation": random.choice(["insert", "update", "delete"])
    }
    producer.send("cdc_topic", value=data)
    print("Sent:", data)
    time.sleep(2)
