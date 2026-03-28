import csv

# archivos.py - Functions for saving and loading inventory data in CSV format.
def save_csv(inventory, path, include_header=True):
    """Saves inventory to CSV."""
    if not inventory:
        print("No data to save.")
        return

    try:
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if include_header:
                writer.writerow(["name", "price", "quantity"])

            for p in inventory:
                writer.writerow([p["name"], p["price"], p["quantity"]])

        print(f"Inventory saved to: {path}")

    except Exception as e:
        print(f"Error saving file: {e}")

# Function to load inventory from CSV
def load_csv(path):
    """Loads inventory from CSV."""
    inventory = []
    errors = 0
# The function reads a CSV file, validates the data, and populates the inventory list. It counts invalid rows and returns both the inventory and the error count.
    try:
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = next(reader)
            if header != ["name", "price", "quantity"]:
                print("Invalid header.")
                return [], 0

            for row in reader:
                try:
                    if len(row) != 3:
                        raise ValueError

                    name = row[0]
                    price = float(row[1])
                    quantity = int(row[2])

                    if price < 0 or quantity < 0:
                        raise ValueError

                    inventory.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    errors += 1

        return inventory, errors

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error reading file: {e}")

    return [], 0