import csv
from package_delivery_tracker.config import DATA_FILE

COLUMNS = ["tracking_id", "sender", "receiver", "status", "created_at", "notes", "log"]

def load_data():
    data = {}
    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["log"] = row["log"].split(";;") if row.get("log") else []
                data[row["tracking_id"]] = row
    except FileNotFoundError:
        return {}
    return data


def save_data(data):
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=COLUMNS)
            writer.writeheader()

            for tid, pkg in data.items():
                row = pkg.copy()
                row["tracking_id"] = tid
                row["log"] = ";;".join(row.get("log", []))
                writer.writerow(row)

    except Exception as e:
        print("Error saving:", e)