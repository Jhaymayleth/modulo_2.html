# Riwistore Shopping Cart

## Description
This project is a simple command-line shopping cart application written in Python. It is designed to help users calculate the total cost of multiple products by inputting product names, prices, and quantities. The application uses a modular structure with an external inventory module for input validation.

### How it works
1. The script prints a welcome message and imports the `obtener_input_valido` function from the `inventario` module to handle user input validation.
2. It defines the `costo_total` function, which multiplies price by quantity to calculate each product's subtotal.
3. A `while` loop runs as long as the user enters "si" (yes), prompting for product name, price, and quantity; it calculates the subtotal, adds it to `total_general`, and displays product details.
4. After each item, it asks if the user wants to add another article; the loop continues or exits based on the response.
5. Finally, it displays the grand total of all items purchased.

> **Status:** The application is fully functional and currently processing multiple items in a loop until the user chooses to stop.
