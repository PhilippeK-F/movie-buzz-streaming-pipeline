import json
import time
import random
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

movies = [
    ("Inception", "Sci-Fi"),
    ("Titanic", "Romance"),
    ("The Dark Knight", "Action"),
    ("Avengers", "Action"),
    ("Interstellar", "Sci-Fi"),
]

regions = ["US", "EU", "ASIA"]
platforms = ["Netflix", "Prime", "Disney+"]
event_types = ["view", "like", "share"]

print("Starting producer... Press Ctrl+C to stop.")

while True:
    movie = random.choice(movies)

    event = {
        "event_time": datetime.utcnow().isoformat(),
        "movie_id": random.randint(1, 100),
        "title": movie[0],
        "genre": movie[1],
        "region": random.choice(regions),
        "platform": random.choice(platforms),
        "event_type": random.choice(event_types),
        "buzz_score": round(random.random() * 100, 2),
    }

    producer.send("movie_events", event)
    producer.flush()
    print(event)

    time.sleep(0.1)