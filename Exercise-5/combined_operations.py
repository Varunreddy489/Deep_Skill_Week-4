from product_details import product_details

def report_sorted_by_price():
    """
    Generate a report of products sorted by price.
    """
    sorted_products = sorted(product_details.items(), key=lambda item: item[1]['price'])
    for name, details in sorted_products:
        print(f"Product: {name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

def find_products_in_price_range(min_price: float, max_price: float):
    """
    Find products within a certain price range.
    """
    products_in_range = {name for name, details in product_details.items()
                         if min_price <= details['price'] <= max_price}
    print(f"Products in price range ${min_price} - ${max_price}: {products_in_range}")

if __name__ == "__main__":
    report_sorted_by_price()
    find_products_in_price_range(0.50, 1.00)
