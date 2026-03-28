 #1. Heladería: sabor más pedido

vainilla = 0
chocolate = 0
fresa = 0

for i in range(5):
    sabor = input("Ingrese sabor (vainilla, chocolate, fresa): ").lower()

    if sabor == "vainilla":
        vainilla += 1
    elif sabor == "chocolate":
        chocolate += 1
    elif sabor == "fresa":
        fresa += 1

print("Vainilla:", vainilla)
print("Chocolate:", chocolate)
print("Fresa:", fresa)

#2. Gimnasio: acceso por edad

edad = int(input("Ingrese su edad: "))

if edad < 13:
    print("No puede ingresar")
elif edad <= 17:
    print("Clase juvenil")
elif edad <= 59:
    print("Clase general")
else:
    print("Clase senior")
