import csv
from faker import Faker
from random import randint
fake = Faker()
def save_people_to_csv(filename, people):
    for i in range (100):
        name = fake.name()
        usage = f"{randint(100, 1500)} MB"
        people.append((name, usage))
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Data Usage'])
        writer.writerows(people)

save_people_to_csv('people_usage.csv', [])