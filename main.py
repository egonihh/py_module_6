import csv 
from plan_recommender import estimate_monthly_usage, recommend_plan
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

print ("Recommendations for People from CSV:")
people = load_people_from_csv('people_usage.csv')
recommendations = recommend_plans_for_people(people)
for name, estimated_usage, plan in recommendations:
    print(f"{name}: Estimated Monthly Usage: {estimated_usage} GB, Recommended Plan: {plan}")