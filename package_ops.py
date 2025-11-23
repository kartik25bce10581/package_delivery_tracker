

from package_delivery_tracker.data_handler import save_data
from package_delivery_tracker.config import STATUS_MAP
from package_delivery_tracker.utils import now_ts, make_log


def create_package(data, tracking_id, sender, receiver, note=""):
    if tracking_id in data:
        raise ValueError("Tracking ID already exists")
    
    data[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "status": STATUS_MAP.get(1, "Booked"),
        "created_at": now_ts(),
        "notes": note,
        "log": [make_log("Package created", note)]
    }

    save_data(data)
    return True


def update_status(data, tracking_id, status_key, note=""):
    if tracking_id not in data:
        raise KeyError("Tracking ID not found")

    # Convert user input (string) → integer
    try:
        status_key = int(status_key)
    except:
        raise ValueError("Invalid status choice")

    new_status = STATUS_MAP.get(status_key)
    if not new_status:
        raise ValueError("Invalid status choice")

    data[tracking_id]["status"] = new_status
    data[tracking_id]["log"].append(make_log(f"Status updated to {new_status}", note))

    save_data(data)
    return True


def delete_package(data, tracking_id):
    if tracking_id not in data:
        return False
    
    del data[tracking_id]
    save_data(data)
    return True