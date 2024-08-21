
import threading
import time
import json

class Inventory:
    def __init__(self, filename='inventory.json'):
        self.items = {}
        self.filename = filename
        self.load_from_file()
        self.check_thread = threading.Thread(target=self.periodic_check, daemon=True)
        self.check_thread.start()

    def add_item(self, item_name: str, quantity: int):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} of {item_name}. Current stock: {self.items[item_name]}")
        self.save_to_file()

    def remove_item(self, item_name: str, quantity: int):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
                print(f"Removed {quantity} of {item_name}. Current stock: {self.items[item_name]}")
                if self.items[item_name] == 0:
                    del self.items[item_name]
            else:
                print(f"Not enough stock of {item_name} to remove.")
        else:
            print(f"Item {item_name} does not exist in inventory.")
        self.save_to_file()

    def check_stock(self, item_name: str):
        return self.items.get(item_name, 0)

    def save_to_file(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.items, file)
            print("Inventory saved to file.")
        except IOError as e:
            print(f"Failed to save inventory to file: {e}")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                self.items = json.load(file)
            print("Inventory loaded from file.")
        except FileNotFoundError:
            print("Inventory file not found. Starting with empty inventory.")
        except IOError as e:
            print(f"Failed to load inventory from file: {e}")

    def check_restocking_alerts(self):
        for item_name, quantity in self.items.items():
            if quantity <= 5:  # Assuming a restocking threshold of 5 items
                print(f"Alert: Low stock on {item_name}. Current quantity: {quantity}")

    def periodic_check(self):
        while True:
            self.check_restocking_alerts()
            time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    inventory = Inventory()

    # Perform some operations
    inventory.add_item('Apples', 10)
    inventory.add_item('Bananas', 4)
    inventory.remove_item('Apples', 6)
    inventory.remove_item('Bananas', 1)

    time.sleep(120)  # Sleep for 2 minutes to allow the periodic check to run

    print("Current Inventory:")
    for item, quantity in inventory.items.items():
        print(f"{item}: {quantity}")
