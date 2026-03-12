CREATE TABLE IF NOT EXISTS movie_events (

event_time TIMESTAMP,
movie_id INT,
title TEXT,
genre TEXT,
region TEXT,
platform TEXT,
event_type TEXT,
buzz_score DOUBLE PRECISION

);