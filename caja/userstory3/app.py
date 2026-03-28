from servicios import *
from archivos import *
# app.py - Main application for the cash register inventory system.
inventory = []
# The main menu function controls the flow of the program, 
# allowing users to manage their inventory and save/load data from CSV files. 
# It includes error handling to ensure a smooth user experience.

def menu():
    running = True

    while running:
        print("\n=== INVENTORY ===")
        print("1. Add")
        print("2. Show")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("Option: ")

        try:
            if option == "1":
                name = input("Name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                add_product(inventory, name, price, quantity)

            elif option == "2":
                show_inventory(inventory)

            elif option == "3":
                name = input("Search: ")
                p = search_product(inventory, name)
                print(p if p else "Not found")

            elif option == "4":
                name = input("Product to update: ")
                price = input("New price (press Enter to skip): ")
                quantity = input("New quantity (press Enter to skip): ")

                update_product(
                    inventory,
                    name,
                    float(price) if price else None,
                    int(quantity) if quantity else None
                )

            elif option == "5":
                name = input("Delete: ")
                if delete_product(inventory, name):
                    print("Deleted")
                else:
                    print("Not found")

            elif option == "6":
                stats = calculate_statistics(inventory)
                if stats:
                    print(stats)
                else:
                    print("Inventory is empty")

            elif option == "7":
                path = input("File path: ")
                save_csv(inventory, path)

            elif option == "8":
                path = input("File path: ")
                data, errors = load_csv(path)

                if data:
                    decision = input("Overwrite current inventory? (Y/N): ").lower()

                    if decision == "y":
                        inventory.clear()
                        inventory.extend(data)
                        print("Inventory replaced")
                    else:
                        for new in data:
                            existing = search_product(inventory, new["name"])
                            if existing:
                                existing["quantity"] += new["quantity"]
                                existing["price"] = new["price"]
                            else:
                                inventory.append(new)
                        print("Inventory merged")

                    print(f"Invalid rows skipped: {errors}")

            elif option == "9":
                running = False

            else:
                print("Invalid option")

        except Exception as e:
            print(f"Error: {e}")


menu()