import json
from kafka import KafkaProducer

KAFKA_TOPIC = "data_ingestion"

def ingest_data(data):
    producer = KafkaProducer(bootstrap_servers="localhost:9092",
                             value_serializer=lambda v: json.dumps(v).encode("utf-8"))
    producer.send(KAFKA_TOPIC, data)
    producer.flush()
