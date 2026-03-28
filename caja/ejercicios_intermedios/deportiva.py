#8. Tienda deportiva

contador = 0

for i in range(6):
    precio = int(input("Precio del producto: "))
    if precio > 100000:
        contador += 1

print("Productos caros:", contador)
