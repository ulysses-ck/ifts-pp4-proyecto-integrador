from faker import Faker
from apps.client.models import Client
from apps.barber.models import Barber
from apps.turn.models import Turn
import random
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# seeds client
def seed_client():
    logger.info("Starting to seed clients...")
    fake = Faker()
    count = 0
    for _ in range(10):
        Client.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
        )
        count += 1
    logger.info(f"Successfully seeded {count} clients")

# seeds barber
def seed_barber():
    logger.info("Starting to seed barbers...")
    fake = Faker()
    count = 0
    for _ in range(10):
        Barber.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
        )
        count += 1
    logger.info(f"Successfully seeded {count} barbers")

# seeds turn
def seed_turn():
    logger.info("Starting to seed turns...")
    fake = Faker()
    clients = list(Client.objects.all())
    barbers = list(Barber.objects.all())
    
    if not clients or not barbers:
        logger.error("Cannot seed turns: No clients or barbers found. Please seed clients and barbers first.")
        return
    
    logger.info(f"Found {len(clients)} clients and {len(barbers)} barbers for turn creation")
    count = 0
    
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
            time_slot=random_time,
        )
        count += 1
    
    logger.info(f"Successfully seeded {count} turns")

def run():
    logger.info("Starting database seeding process...")
    seed_client()
    seed_barber()
    seed_turn()
    logger.info("Database seeding completed successfully")

if __name__ == '__main__':
    run()
    