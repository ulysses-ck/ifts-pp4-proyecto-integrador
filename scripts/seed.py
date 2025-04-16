from faker import Faker
from apps.client.models import Client
from apps.barber.models import Barber
from apps.turn.models import Turn
import random
from datetime import datetime


# seeds client
def seed_client():
    fake = Faker()
    for _ in range(10):
        Client.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
        )

# seeds barber
def seed_barber():
    fake = Faker()
    for _ in range(10):
        Barber.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
        )

# seeds turn
def seed_turn():
    fake = Faker()
    clients = list(Client.objects.all())
    barbers = list(Barber.objects.all())
    
    if not clients or not barbers:
        print("Cannot seed turns: No clients or barbers found. Please seed clients and barbers first.")
        return
    
    for _ in range(10):
        # Generate a random date between 30 days ago and 30 days in the future
        random_date = fake.date_between(start_date='-30d', end_date='+30d')
        
        # Generate a random time between 9 AM and 6 PM
        random_hour = random.randint(9, 17)
        random_minute = random.randint(0, 59)
        random_time = datetime.strptime(f"{random_hour:02d}:{random_minute:02d}", "%H:%M").time()
        
        Turn.objects.create(
            client=random.choice(clients),
            barber=random.choice(barbers),
            date=random_date,
            time=random_time,
        )

def run():
    seed_client()
    seed_barber()
    seed_turn()

if __name__ == '__main__':
    run()
    