nombre = input("Nombre: ").strip()
edad_txt = input("Edad (entera): ").strip()
ciudad = input("Ciudad: ").strip()
try:
    edad = int(edad_txt)
    print(f"Hola {nombre}, tienes {edad} y vives en {ciudad}.")
    print(f"El año que viene tendrás {edad + 1}.")
except ValueError:
    print("La edad debe ser un entero.")