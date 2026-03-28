# Global list that stores inventory products
inventory = []

# Function that prevents the product name from being empty or containing numbers,
# and validates price and quantity to ensure they are positive.
def is_product_name_valid(name):
    """Validates the product name."""
    if not name.strip():
        return False, "The name cannot be empty."
    if name.isdigit():
        return False, "The product name cannot be only numbers."
    if any(char.isdigit() for char in name):
        return False, "The product name cannot contain numbers."
    return True, ""

# Function to request and validate the product name
def request_name():
    """Requests and validates the product name."""
    name = input("Product name: ").strip()
    is_valid, message = is_product_name_valid(name)

    while not is_valid:
        print(message)
        name = input("Product name: ").strip()
        is_valid, message = is_product_name_valid(name)

    return name

# Function to request and validate the product price
def request_price():
    """Requests and validates the product price."""
    valid = False
    while not valid:
        try:
            price = float(input("Unit price: "))
            if price >= 0:
                valid = True
            else:
                print("The price cannot be negative.")
        except ValueError:
            print("The price must be a number.")

    return price

# Function to request and validate the product quantity
def request_quantity():
    """Requests and validates the product quantity."""
    valid = False
    while not valid:
        try:
            quantity = int(input("Inventory quantity: "))
            if quantity >= 0:
                valid = True
            else:
                print("The quantity cannot be negative.")
        except ValueError:
            print("The quantity must be an integer.")

    return quantity

# Function to add a product to the inventory
def add_product():
    """Adds a product to the inventory."""
    print("\n--- Add Product ---")

    name = request_name()
    price = request_price()
    quantity = request_quantity()

    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)

    print("Product added successfully.")

# Function to display the inventory
def show_inventory():
    """Displays all products in the inventory."""
    print("\n--- Inventory ---")

    if not inventory:
        print("The inventory is empty.")
        return

    for product in inventory:
        print(f"Product: {product['name']} | Price: ${product['price']:.2f} | Quantity: {product['quantity']}")

# Function to calculate inventory statistics
def calculate_statistics():
    """Calculates inventory statistics."""
    print("\n--- Statistics ---")

    if not inventory:
        print("There are no products in the inventory.")
        return

    total_value = 0
    total_units = 0

    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_units += product["quantity"]

    print(f"Total inventory value: ${total_value:.2f}")
    print(f"Total number of products: {total_units}")

# --- Main menu ---
def menu():
    """Controls the main program flow."""
    running = True

    while running:
        print("\n=== Inventory System ===")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculate statistics")
        print("4. Exit")

        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            add_product()
        elif option == "2":
            show_inventory()
        elif option == "3":
            calculate_statistics()
        elif option == "4":
            print("Exiting the system. Goodbye!")
            running = False
        else:
            print("Invalid option. Please try again.")

# Run program
menu()

# --- Final comment ---
# This program allows managing a basic inventory using data structures
# such as lists and dictionaries, input validation with conditionals,
# and flow control through loops and functions.