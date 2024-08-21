product_details = {
    "Apple": {"quantity": 10, "price": 1.00},
    "Banana": {"quantity": 20, "price": 0.50}
}

def add_product_details(name: str, quantity: int, price: float):
    """
    Add or update product details.
    """
    product_details[name] = {"quantity": quantity, "price": price}
    print(f"Details for '{name}' added/updated.")

def update_product_details(name: str, quantity: int = None, price: float = None):
    """
    Update product details.
    """
    if name in product_details:
        if quantity is not None:
            product_details[name]["quantity"] = quantity
        if price is not None:
            product_details[name]["price"] = price
        print(f"Details for '{name}' updated.")
    else:
        print(f"Product '{name}' not found.")

def delete_product_details(name: str):
    """
    Delete product details.
    """
    if name in product_details:
        del product_details[name]
        print(f"Details for '{name}' removed.")
    else:
        print(f"Product '{name}' not found.")

# Example usage
if __name__ == "__main__":
    add_product_details("Cherry", 15, 1.25)
    update_product_details("Apple", price=1.10)
    delete_product_details("Banana")
    print("Current product details:", product_details)
