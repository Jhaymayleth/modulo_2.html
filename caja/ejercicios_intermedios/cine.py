#4. Cine: entrada según edad

edad = int(input("Edad: "))

if edad < 12:
    print("Debe pagar 8000")
elif edad <= 59:
    print("Debe pagar 12000")
else:
    print("Debe pagar 9000")

