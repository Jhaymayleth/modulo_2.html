def agregar_producto(inventario, nombre, precio, cantidad):
    """Adds a product to the inventory."""
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


def mostrar_inventario(inventario):
    """Displays all products."""
    if not inventario:
        print("El inventario está vacío.")
        return

    for p in inventario:
        print(f"{p['nombre']} | ${p['precio']:.2f} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """Searches a product by name."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Updates a product."""
    producto = buscar_producto(inventario, nombre)

    if not producto:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    """Deletes a product."""
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """Calculates inventory statistics."""
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"]),
    }