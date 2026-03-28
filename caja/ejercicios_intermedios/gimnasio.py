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