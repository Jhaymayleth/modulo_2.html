#9. Spa: servicio

servicio = input("Servicio (masaje, facial, manicure): ").lower()

if servicio == "masaje" or servicio == "facial" or servicio == "manicure":
    print("Servicio disponible")
else:
    print("Servicio no disponible")

