def es_nombre_valido(nombre):
    if not nombre.strip():
        return False, "El nombre no puede estar vacío."
    if nombre.isdigit():  # si todo es un número (ej. "2000", "123")
        return False, "El nombre del producto no puede ser solo números."
    if any(char.isdigit() for char in nombre):  # si lleva algún número mezclado
        return False, "El nombre del producto no puede contener números."
    return True, ""

ventas = []  # Lista que guarda cada venta (diccionario)
continuar = True
print("=== Registro de ventas diarias ===\n")
while continuar:
    print("\n--- Nueva venta ---")
    nombre = input("Nombre del producto (o escriba 'salir' para terminar el día): ").strip()

    # Verificar si el usuario quiere salir
    if nombre.lower() == "salir":
        continuar = False
        continue

    # Validar nombre con la función
    valido, mensaje = es_nombre_valido(nombre)
    if not valido:
        print(mensaje)
        continue

    # Leer precio y validarlo
    try:
        precio = float(input("Precio unitario: "))
        if precio < 0:
            print("El precio no puede ser negativo. Intente de nuevo.")
            continue
    except ValueError:
        print("Precio inválido. Debe ingresar un número. Intente de nuevo.")
        continue

    # Leer cantidad y validarlo
    try:
        cantidad = int(input("Cantidad vendida: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0. Intente de nuevo.")
            continue
    except ValueError:
        print("Cantidad inválida. Debe ingresar un número entero. Intente de nuevo.")
        continue

    # Calcular total de la venta
    total_venta = precio * cantidad

    # Registrar la venta
    ventas.append({
        "producto": nombre,
        "precio_unitario": precio,
        "cantidad": cantidad,
        "total_venta": total_venta
    })
    print(f"Venta registrada: {nombre} - {cantidad} unidades - Total: {total_venta:.2f}")

# Resumen al finalizar el día
print("\n" + "=" * 50)
print("RESUMEN DE VENTAS DEL DÍA")
print("=" * 50)

if not ventas:
    print("No se registraron ventas hoy.")
else:
    # Diccionario para acumular cantidades por producto
    productos_totales = {}
    total_dia = 0.0

    for venta in ventas:
        prod = venta["producto"]
        cant = venta["cantidad"]
        tot = venta["total_venta"]

        if prod in productos_totales:
            productos_totales[prod]["cantidad"] += cant
            productos_totales[prod]["total_acumulado"] += tot
        else:
            productos_totales[prod] = {
                "cantidad": cant,
                "total_acumulado": tot
            }

        total_dia += tot

    # Mostrar listado de productos
    print("\nProductos vendidos:")
    print("-" * 40)
    for prod, datos in productos_totales.items():
        print(f"{prod:20} - Unidades: {datos['cantidad']:3} - Total: {datos['total_acumulado']:8.2f}")

    # Totales generales
    print("\n" + "-" * 40)
    print(f"Cantidad total vendida: {sum(v['cantidad'] for v in ventas)} unidades")
    print(f"Ingreso total del día: {total_dia:.2f}")
    print("-" * 40)

print("\n¡Fin del registro de ventas!")