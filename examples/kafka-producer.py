from kafka import KafkaProducer
import json

# Kafka producer configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Define the topic name
topic = 'stock-data-topic'

# Example data to send
data = {
    'symbol': 'AAPL',
    'price': 150.00,
    'timestamp': '2023-10-01T12:00:00Z'
}

# Send data to Kafka topic
producer.send(topic, value=data)

# Ensure all messages are sent before closing the producer
producer.flush()
producer.close()
