edad_txt = input("Tu edad: ").strip()
try:
    edad = int(edad_txt)
    if edad < 0:
        print("Edad no válida")
    elif edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
except ValueError:
    print("Debes introducir un número entero.")