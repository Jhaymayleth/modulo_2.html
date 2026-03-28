# inventario.py
# Módulo con funciones de validación y cálculo para un sistema simple de inventario/caja.

def obtener_input_valido(mensaje, tipo):
    """Pide al usuario un valor hasta que sea válido para el tipo dado (int o float).
       Si el valor es inválido, muestra un mensaje de error y vuelve a pedir."""
    valor_correcto = False
    while not valor_correcto:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            valor_correcto = True
            return valor
        except ValueError:
            print("Error: Ingresa un valor válido.")  # Evita que el programa se cierre por error de tipo.


def costo_total(precio, cantidad):
    """Calcula el costo total de un producto (precio unitario * cantidad)."""
    return precio * cantidad