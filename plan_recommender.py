from random import randint
def estimate_monthly_usage(daily_usage):
    monthly_usage_mb = daily_usage * 30
    estimated_mb = randint(max(0, monthly_usage_mb - 2000), monthly_usage_mb + 2000)
    rounded_gb = int(round(estimated_mb / 1024))
    return rounded_gb
    

def recommend_plan(usage):
    if usage <= 8:
        return "Flexible Add-On Plan"
    elif usage <= 18:
        return "Dynamic Flexible Plan"
    elif usage <= 30:
        return "Flat 30GB Plan"
    else:
        return "Unlimited Plan"
    
def display_all_plans():
    plans = get_all_plans()
    print("Available Data Plans:")
    print("------------------------")
    for plan in plans:
        print(plan)
        print("------------------------")


def get_all_plans():
    """Return a list of available plan descriptions.

    This is used by other modules (and the web API) to retrieve
    the plans programmatically instead of printing to stdout.
    """
    return [
        "Flexible Add-On Plan: 10GB - €8/month after base plan every 5GB costs €3",
        "Dynamic Flexible Plan: The cost per GB decreases as usage increases:\n0–10GB: €1.2/GB\n10–20GB: €1/GB\n20–30GB: €0.7/GB",
        "Flat 30GB Plan: 30 GB - €30/month",
        "Unlimited Plan: - €50/month"
    ]
    
