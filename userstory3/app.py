from servicios import *
from archivos import *

inventario = []


def menu():
    continuar = True

    while continuar:
        print("\n=== INVENTARIO ===")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                agregar_producto(inventario, nombre, precio, cantidad)

            elif opcion == "2":
                mostrar_inventario(inventario)

            elif opcion == "3":
                nombre = input("Buscar: ")
                p = buscar_producto(inventario, nombre)
                print(p if p else "No encontrado")

            elif opcion == "4":
                nombre = input("Producto a actualizar: ")
                precio = input("Nuevo precio (Enter para omitir): ")
                cantidad = input("Nueva cantidad (Enter para omitir): ")

                actualizar_producto(
                    inventario,
                    nombre,
                    float(precio) if precio else None,
                    int(cantidad) if cantidad else None
                )

            elif opcion == "5":
                nombre = input("Eliminar: ")
                if eliminar_producto(inventario, nombre):
                    print("Eliminado")
                else:
                    print("No encontrado")

            elif opcion == "6":
                stats = calcular_estadisticas(inventario)
                if stats:
                    print(stats)
                else:
                    print("Inventario vacío")

            elif opcion == "7":
                ruta = input("Ruta archivo: ")
                guardar_csv(inventario, ruta)

            elif opcion == "8":
                ruta = input("Ruta archivo: ")
                datos, errores = cargar_csv(ruta)

                if datos:
                    decision = input("¿Sobrescribir inventario? (S/N): ").lower()

                    if decision == "s":
                        inventario.clear()
                        inventario.extend(datos)
                        print("Inventario reemplazado")
                    else:
                        for nuevo in datos:
                            existente = buscar_producto(inventario, nuevo["nombre"])
                            if existente:
                                existente["cantidad"] += nuevo["cantidad"]
                                existente["precio"] = nuevo["precio"]
                            else:
                                inventario.append(nuevo)
                        print("Inventario fusionado")

                    print(f"Filas inválidas omitidas: {errores}")

            elif opcion == "9":
                continuar = False

            else:
                print("Opción inválida")

        except Exception as e:
            print(f"Error: {e}")


menu()