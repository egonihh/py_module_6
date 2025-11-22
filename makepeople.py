import csv
from faker import Faker
from random import randint
fake = Faker()
def save_people_to_csv(filename, people):
    input_people = input("How many fake people would you like to generate? ")
    for i in range (int(input_people)):
        name = fake.name()
        usage = f"{randint(100, 1500)} MB"
        people.append((name, usage))
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Data Usage'])
        writer.writerows(people)
        return input_people

number = save_people_to_csv('people_usage.csv', [])
print(f"CSV file 'people_usage.csv' created with {number} fake people data.")