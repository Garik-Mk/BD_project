from faker import Faker
import random

from zoodb import ZooDB
from model import ZooComplex, Accommodations, Species


def generate_random_data(complex_count=10, accommodation_count=100, specie_count=1000):
    fake = Faker()
    ZooDB.connect_to_DB()
    for _ in range(complex_count):
        complex_name = fake.company()
        zoo_complex = ZooComplex(complex_name=complex_name)
        ZooDB.session.add(zoo_complex)
        ZooDB.session.commit()
    for _ in range(accommodation_count):
        accommodation_name = fake.word()
        has_pool = random.choice([True, False])
        area = random.uniform(50.0, 200.0)
        accommodation = Accommodations(
            name=accommodation_name,
            complex_id=random.randint(1, complex_count),
            has_pool=has_pool,
            area=area
        )
        ZooDB.session.add(accommodation)
        ZooDB.session.commit()
    for _ in range(specie_count):
        specie_name = fake.word()
        family = fake.word()
        habitat = fake.word()
        live_duration = random.randint(1, 20)
        species = Species(
            accommodation_id=random.randint(1, 100),
            specie_name=specie_name,
            family=family,
            habitat=habitat,
            live_duration=live_duration
        )
        ZooDB.session.add(species)
        ZooDB.session.commit()


if __name__ == "__main__":
    generate_random_data()
