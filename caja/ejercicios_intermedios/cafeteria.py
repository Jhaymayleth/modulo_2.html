#3. Cafetería: total de compra

bebida = input("Ingrese bebida (cafe, te, jugo): ").lower()
cantidad = int(input("Cantidad: "))

if bebida == "cafe":
    precio = 4000
elif bebida == "te":
    precio = 3500
elif bebida == "jugo":
    precio = 5000

total = precio * cantidad
print("Total a pagar:", total)
