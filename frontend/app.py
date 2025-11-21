from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = "data.csv"

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

    return jsonify({"status": "success", "msg": "Saved to CSV"})


if __name__ == "__main__":
    app.run(debug=True)
