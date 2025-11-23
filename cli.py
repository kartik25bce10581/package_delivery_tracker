
from package_delivery_tracker.data_handler import load_data
from package_delivery_tracker.package_ops import create_package, update_status, delete_package
from package_delivery_tracker.view_ops import view_package, view_all_packages


def main():
    print("\n=== Package Delivery Status Tracker ===\n")
    data = load_data()

    while True:
        print("\nChoose an option:")
        print("1) Add package")
        print("2) Update status")
        print("3) View a package")
        print("4) View all packages")
        print("5) Delete")
        print("6) Exit\n")

        choice = input("Enter choice: ").strip()

        # ---- Add ----
        if choice == "1":
            tid = input("Tracking ID: ").strip()
            sender = input("Sender: ").strip()
            receiver = input("Receiver: ").strip()
            note = input("Notes (optional): ").strip()
            try:
                create_package(data, tid, sender, receiver, note)
                print("Added successfully.")
            except Exception as err:
                print("Could not add package:", err)

        # ---- Update ----
        elif choice == "2":
            tid = input("Tracking ID: ").strip()
            print("Status options: 1) Booked  2) In Transit  3) Out for Delivery  4) Delivered")
            status_key = input("Choose status number: ").strip()
            note = input("Note (optional): ").strip()

            try:
                update_status(data, tid, status_key, note)
                print("Status updated.")
            except Exception as err:
                print("Update failed:", err)

        # ---- View one ----
        elif choice == "3":
            tid = input("Enter tracking ID to view: ").strip()
            view_package(load_data(),tid)

        # ---- View all ----
        elif choice == "4":
            view_all_packages(load_data())

        # ---- Delete ----
        elif choice == "5":
            tid = input("Tracking ID to delete: ").strip()
            if delete_package(data, tid):
                print("Deleted.")
            else:
                print("ID not found.")

        # ---- Exit ----
        elif choice == "6":
            print("Exiting…")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()