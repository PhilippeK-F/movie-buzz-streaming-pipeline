from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import psycopg2

spark = SparkSession.builder \
    .appName("MovieBuzzStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "movie_events") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)")

schema = """
event_time STRING,
movie_id INT,
title STRING,
genre STRING,
region STRING,
platform STRING,
event_type STRING,
buzz_score DOUBLE
"""

events = json_df.select(from_json(col("value"), schema).alias("data")).select("data.*")

events = events.withColumn(
    "event_time",
    to_timestamp("event_time")
)

def write_to_postgres(batch_df, batch_id):

    rows = batch_df.collect()

    conn = psycopg2.connect(
        host="postgres",
        database="movies",
        user="movies",
        password="movies"
    )

    cursor = conn.cursor()

    for r in rows:
        cursor.execute(
            """
            INSERT INTO movie_events
            (event_time, movie_id, title, genre, region, platform, event_type, buzz_score)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                r.event_time,
                r.movie_id,
                r.title,
                r.genre,
                r.region,
                r.platform,
                r.event_type,
                r.buzz_score
            )
        )

    conn.commit()
    cursor.close()
    conn.close()

query = events.writeStream \
    .foreachBatch(write_to_postgres) \
    .start()

query.awaitTermination()