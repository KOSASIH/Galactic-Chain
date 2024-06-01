import time
from kafka import KafkaProducer

class KafkaDataProducer:
    def __init__(self, topic, bootstrap_servers="localhost:9092"):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode("utf-8"))
        self.topic = topic

    def send_message(self, message):
        self.producer.send(self.topic, message)
        self.producer.flush()

    def close(self):
        self.producer.close()

if __name__ == "__main__":
    producer = KafkaDataProducer(KAFKA_TOPIC)
    while True:
        data = {"sensor_id": 1, "temperature": 25.5, "timestamp": int(time.time())}
        producer.send_message(data)
        time.sleep(1)
