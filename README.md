# 🎬 Real-Time Movie Buzz Streaming Pipeline

A real-time data engineering pipeline that simulates movie buzz events and processes them through a streaming architecture using Kafka, Spark Structured Streaming, PostgreSQL, and Grafana.

The project demonstrates how to build an end-to-end streaming analytics system.

---

# Architecture

Producer → Kafka → Spark Streaming → PostgreSQL → Grafana

          +---------------------+
          |  Python Producer    |
          | generate_events.py  |
          +----------+----------+
                     |
                     v
               +-----------+
               |   Kafka   |
               | movie_events
               +-----+-----+
                     |
                     v
        +--------------------------+
        | Spark Structured Streaming|
        | spark_consumer.py         |
        +-----------+--------------+
                    |
                    v
              +-----------+
              | PostgreSQL|
              | movie_events
              +-----+-----+
                    |
                    v
                +--------+
                | Grafana|
                |Dashboard
                +--------+

## Tech Stack

- Python
- Apache Kafka
- Apache Spark (Structured Streaming)
- PostgreSQL
- Grafana
- Docker

## Data Flow

- Producer
Generates fake movie buzz events using Python.
Sends events to Kafka topic movie_events.

- Kafka
Acts as the streaming message broker.

- Spark Streaming
Consumes Kafka events.
Processes streaming data.

- PostgreSQL
Stores processed events.

- Grafana
Visualizes real-time analytics.

## Example Event
{
  "movie_id": 12,
  "title": "Dune",
  "genre": "Sci-Fi",
  "region": "Europe",
  "platform": "Twitter",
  "event_type": "mention",
  "buzz_score": 72
}

## Dashboard Metrics
Grafana dashboard includes:

- Total Events
- Average Buzz Score
- Events per Minute
- Top Trending Movies
- Events by Region
- Buzz Score by Genre

## Running the Project

## 1 Start services
docker compose up -d

## 2 Start the producer
python producer/generate_events.py

## 3 Run the Spark consumer
docker compose exec spark /opt/spark/bin/spark-submit \
--conf spark.jars.ivy=/tmp/.ivy2 \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
/opt/spark/jobs/spark_consumer.py


## Grafana Dashboard
Open Grafana:

http://localhost:3000

Login:

user: admin
password: admin
Example Dashboard

Real-time movie buzz analytics showing:

trending movies

streaming activity

geographic distribution

## Project Structure
movie-buzz-streaming-pipeline
│
├── producer
│   └── generate_events.py
│
├── streaming
│   └── spark_consumer.py
│
├── sql
│   └── init.sql
│
├── spark
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.md

## Learning Goals

This project demonstrates:

Real-time data pipelines

Streaming architectures

Kafka integration with Spark

Data ingestion into PostgreSQL

Real-time dashboards with Grafana

Containerized infrastructure with Docker

## Author

Philippe Kirstetter-Fender
Data Engineering Portfolio Project