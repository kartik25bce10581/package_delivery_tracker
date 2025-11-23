

def view_package(data,tracking_id):
    tracking_id=input("Enter Tracking ID:").strip()
    if tracking_id not in data:
        print("Tracking ID not found")
        return 
    pkg=data[tracking_id]
    print("\n--- Package details ---")
    print(f"ID: {tracking_id}")
    print(f"Sender: {pkg['sender']}")
    print(f"Receiver: {pkg['receiver']}")
    print(f"Status: {pkg['status']}")
    print(f"Created At: {pkg['created_at']}")
    print("\n--- Log History ---")
    for entry in pkg['log']:
        print(entry)
    print("--------------------------------")

def view_all_packages(data):
    if not data:
        print("No packages found!")
        return
    print("---All Packages---")
    for tid,pkg in data.items():
        print(f"{tid}: {pkg['sender']} - {pkg['receiver']} | {pkg['status']}")
    print("----------------------------------")
    




