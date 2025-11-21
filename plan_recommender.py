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
    

    
