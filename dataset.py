from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)

actions = ["watch", "pause", "like", "search"]
genres = ["Action", "Drama", "Comedy", "Romance", "Sci-Fi", "Horror", "Documentary", "Animation"]

def generate_user_events(n_users=1000, n_events=10000):
    users = [f"user_{i}" for i in range(n_users)]
    movies = [{"movie_id": f"movie_{i}", "genre": random.choice(genres)} for i in range(100)]

    data = []
    for _ in range(n_events):
        user = random.choice(users)
        movie = random.choice(movies)
        action = random.choice(actions)
        duration = random.randint(1, 200)
        timestamp = fake.date_time_between(start_date='-30d', end_date='now')

        data.append((timestamp, user, movie["movie_id"], movie["genre"], action, duration))

    df = pd.DataFrame(data, columns=["timestamp", "user_id", "movie_id", "genre", "action", "duration"])
    df.to_csv("/Users/dennismain/Documents/Netflix_algorithm/data.csv", index=False)

generate_user_events()