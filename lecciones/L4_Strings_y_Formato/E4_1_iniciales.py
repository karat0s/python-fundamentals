nombre_apellidos = input("Nombre y apellidos: ").strip()
siglas = ""
for i in range(len(nombre_apellidos)):
    if i == 0 and nombre_apellidos[i] != " ":
        siglas = nombre_apellidos[i] + "."
    elif nombre_apellidos[i] == " ":
        if i + 1 < len(nombre_apellidos) and nombre_apellidos[i + 1] != " ":
            siglas = siglas + nombre_apellidos[i + 1] + "."
print(siglas.upper())