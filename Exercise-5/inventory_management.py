product_names = ["Apple", "Banana", "Cherry", "Date"]

def add_product(name: str):
    """
    Add a new product to the list.
    """
    if name not in product_names:
        product_names.append(name)
        print(f"Product '{name}' added.")
    else:
        print(f"Product '{name}' already exists.")

def remove_product(name: str):
    """
    Remove a product from the list.
    """
    if name in product_names:
        product_names.remove(name)
        print(f"Product '{name}' removed.")
    else:
        print(f"Product '{name}' not found.")

def update_product(old_name: str, new_name: str):
    """
    Update the name of a product.
    """
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name
        print(f"Product '{old_name}' updated to '{new_name}'.")
    else:
        print(f"Product '{old_name}' not found.")

# Example usage
if __name__ == "__main__":
    add_product("Elderberry")
    remove_product("Date")
    update_product("Banana", "Blueberry")
    print("Current products:", product_names)
