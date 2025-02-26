# kafka_producer.py
from kafka import KafkaProducer
import json

# Configuration du producteur Kafka
KAFKA_BROKER = "kafka:9092"
TOPIC = "planet-discoveries"

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
)

def send_to_kafka(data):
    try:
        # Envoi du message dans le topic Kafka
        producer.send(TOPIC, data)
        producer.flush()  
        print("Message envoyé à Kafka avec succès!")
    except Exception as e:
        print(f"Erreur d'envoi à Kafka: {e}")
