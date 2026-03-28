#10. Academia de baile

clases = int(input("Clases asistidas: "))

if clases < 5:
    print("Asistencia baja")
elif clases <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")
