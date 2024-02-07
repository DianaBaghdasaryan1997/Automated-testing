from faker import Faker
fake = Faker()

credentials = {
    "firstname": fake.first_name(),
    "lastname": fake.last_name(),
    "email": fake.email(),
    "password": fake.password(length=8)
}