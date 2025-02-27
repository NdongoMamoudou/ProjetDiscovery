# kafka_consumer.py
from kafka import KafkaConsumer
import json

# Configuration du consommateur Kafka
KAFKA_BROKER = "kafka:9092"
TOPIC = "planet-discoveries"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest'  # Assurer de lire depuis le début si nécessaire
)

def consume_from_kafka():
    try:
        print("Consommation des messages Kafka...")
        for message in consumer:
            print(f"Message reçu: {message.value}")
    except Exception as e:
        print(f"Erreur de consommation de Kafka: {e}")
    finally:
        consumer.close()
        print("Consommateur Kafka fermé proprement.")

if __name__ == "__main__":
    consume_from_kafka()
