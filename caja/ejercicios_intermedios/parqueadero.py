#6. Parqueadero: cobro

horas = int(input("Horas: "))

if horas == 1:
    total = 5000
else:
    total = 5000 + (horas - 1) * 3000

print("Total a pagar:", total)
