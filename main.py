import csv
import os
import sys
from plan_recommender import estimate_monthly_usage, recommend_plan, display_all_plans

def load_people_from_csv(filename):
    people = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            usage_str = row['Data Usage']
            daily_usage_mb = int(usage_str.split()[0])
            people.append((name, daily_usage_mb))
    return people

def recommend_plans_for_people(people):
    recommendations = []
    for name, daily_usage in people:
        estimated_usage = estimate_monthly_usage(daily_usage)
        plan = recommend_plan(estimated_usage)
        recommendations.append((name, estimated_usage, plan))
    return recommendations


def add_person_to_csv (filename, name, daily_usage_mb):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, f"{daily_usage_mb} MB"])


CSV_FILE = 'people_usage.csv'

while True:
    print("Welcome to the Data Plan Recommender!\n-------------------------------")
    select = input("What would you like to do?\n1) Add a new person\n2) Get plan recommendations for existing people\n3) See all plans\nPlease enter 1, 2 or 3: ")
    if select == '1':
        name = input("Enter the person's name: ")
        daily_usage_mb = int(input("Enter their average daily data usage in MB: "))
        add_person_to_csv('people_usage.csv', name, daily_usage_mb)
        recommended_plan = recommend_plan(estimate_monthly_usage(daily_usage_mb))
        print(f"{name} has been added with a daily usage of {daily_usage_mb} MB.\nRecommended Plan: {recommended_plan}")
        
    elif select == '2':
        if not os.path.exists(CSV_FILE):
            print(f"Error: required file '{CSV_FILE}' not found. Please create the file or run the web UI to add entries.")
            sys.exit(1)
        people = load_people_from_csv(CSV_FILE)
        recommendations = recommend_plans_for_people(people)
        number = 1

        print("\nPlan Recommendations:")
        for name, estimated_usage, plan in recommendations:
            print(f"{number}) {name}: Estimated Monthly Usage: {estimated_usage} GB - Recommended Plan: {plan}")
            number += 1
            
    elif select == '3':
        display_all_plans()
    input("Press Enter to continue...")


