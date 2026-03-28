# servicios.py - Inventory management services for the cash register system.
def add_product(inventory, name, price, quantity): 
    """Adds a product to the inventory."""
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)

# Function to display the inventory
def show_inventory(inventory):
    """Displays all products."""
    if not inventory:
        print("The inventory is empty.")
        return

    for p in inventory:
        print(f"{p['name']} | ${p['price']:.2f} | Quantity: {p['quantity']}")

# Function to search for a product by name
def search_product(inventory, name):
    """Searches for a product by name."""
    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None

# Function to update a product's price and/or quantity
def update_product(inventory, name, new_price=None, new_quantity=None):
    """Updates a product."""
    product = search_product(inventory, name)

    if not product:
        return False

    if new_price is not None:
        product["price"] = new_price

    if new_quantity is not None:
        product["quantity"] = new_quantity

    return True

# Function to delete a product by name
def delete_product(inventory, name):
    """Deletes a product."""
    product = search_product(inventory, name)

    if product:
        inventory.remove(product)
        return True
    return False

# Function to calculate inventory statistics
def calculate_statistics(inventory):
    """Calculates inventory statistics."""
    if not inventory:
        return None

    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(p["price"] * p["quantity"] for p in inventory)

    most_expensive_product = max(inventory, key=lambda p: p["price"])
    highest_stock_product = max(inventory, key=lambda p: p["quantity"])

    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": (most_expensive_product["name"], most_expensive_product["price"]),
        "highest_stock_product": (highest_stock_product["name"], highest_stock_product["quantity"]),
    }