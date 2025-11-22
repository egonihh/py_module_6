from flask import Flask, render_template, request, jsonify
import csv
import os
from plan_recommender import estimate_monthly_usage, recommend_plan, display_all_plans, get_all_plans

app = Flask(__name__)

CSV_FILE = "people_usage.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Daily_Usage_MB"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/estimate", methods=["POST"])
def estimate():
    data = request.json
    name = data.get("name")
    daily_usage = data.get("daily_usage")

    # Save into CSV
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, daily_usage])

    # Compute estimated monthly usage (in GB) and recommended plan
    try:
        # daily_usage is expected in MB/day
        estimated_monthly_gb = estimate_monthly_usage(int(daily_usage))
    except Exception:
        estimated_monthly_gb = None

    try:
        recommended = recommend_plan(estimated_monthly_gb) if estimated_monthly_gb is not None else None
    except Exception:
        recommended = None

    return jsonify({
        "status": "success",
        "msg": "Saved to CSV",
        "monthly_gb": estimated_monthly_gb,
        "recommended_plan": recommended
    })


@app.route("/packages", methods=["GET"])
def packages():
    """Return the available plans as JSON."""
    plans = get_all_plans()
    return jsonify({"plans": plans})


if __name__ == "__main__":
    app.run(debug=True)
