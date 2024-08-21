from collections import namedtuple

Product = namedtuple('Product', ['name', 'quantity', 'price'])

catalog = [
    Product(name="Apple", quantity=10, price=1.00),
    Product(name="Banana", quantity=20, price=0.50)
]

def add_to_catalog(name: str, quantity: int, price: float):
    """
    Add a product to the catalog.
    """
    global catal
    catalog.append(Product(name, quantity, price))
    print(f"Product '{name}' added to catalog.")

def show_catalog():
    """
    Show the product catalog.
    """
    for product in catalog:
        print(f"Name: {product.name}, Quantity: {product.quantity}, Price: ${product.price:.2f}")

if __name__ == "__main__":
    add_to_catalog("Cherry", 15, 1.25)
    show_catalog()
