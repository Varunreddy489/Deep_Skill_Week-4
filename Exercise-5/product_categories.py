categories = {"Fruits", "Vegetables"}

def add_category(category: str):
    """
    Add a new category to the set.
    """
    categories.add(category)
    print(f"Category '{category}' added.")

def remove_category(category: str):
    """
    Remove a category from the set.
    """
    categories.discard(category)
    print(f"Category '{category}' removed.")

# Example usage
if __name__ == "__main__":
    add_category("Dairy")
    remove_category("Vegetables")
    print("Current categories:", categories)
