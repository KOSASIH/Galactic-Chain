from kafka import KafkaConsumer

KAFKA_TOPIC = "data_ingestion"

class KafkaDataConsumer:
    def __init__(self, topic, bootstrap_servers="localhost:9092"):
        self.consumer = KafkaConsumer(topic,
                                      bootstrap_servers=bootstrap_servers,
                                      value_deserializer=lambda m: json.loads(m.decode("utf-8")))

    def consume(self):
        for message in self.consumer:
            print(message.value)

if __name__ == "__main__":
    consumer = KafkaDataConsumer(KAFKA_TOPIC)
    consumer.consume()
