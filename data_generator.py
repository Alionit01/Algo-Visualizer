from faker import Faker
import random

fake = Faker()

def generate_records(n=1000):
    records = []
    for _ in range(n):
        record = {
            "id": random.randint(1000, 9999),
            "name": fake.name(),
            "age": random.randint(18, 60)
        }
        records.append(record)
    return records
