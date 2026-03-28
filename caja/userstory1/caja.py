# caja.py
# Archivo principal que gestiona la "caja" de la tienda.
# Pide nombre, precio y cantidad de productos, valida los datos,
# calcula el costo total por producto y muestra el resumen de la compra.

from inventario import obtener_input_valido, costo_total

print("Bienvenido a Riwistore")  # Mensaje de bienvenida

total_general = 0
continuar = "si"

while continuar.lower() == "si":
    # Solicitar datos al usuario
    nombre = input("Ingresar nombre de producto: ").strip()
    precio = obtener_input_valido("Ingresar Precio: ", float)
    cantidad = obtener_input_valido("Ingresar cantidad del producto: ", int)

    # Calcular costo total del producto
    subtotal = costo_total(precio, cantidad)
    total_general += subtotal

    # Mostrar resumen del producto en una sola línea
    print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} | Total: ${subtotal:.2f}")

    # Preguntar si desea agregar otro artículo
    continuar = input("¿Deseas agregar otro artículo? (si/no): ").strip()

# Mostrar total general de la compra
print(f"Total general a pagar: ${total_general:.2f}")