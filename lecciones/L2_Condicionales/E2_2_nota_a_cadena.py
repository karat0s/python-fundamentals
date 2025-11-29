n_txt = input("Nota (0-100): ").strip()
try:
    n = int(n_txt)
    if n < 0 or n > 100:
        print("Nota fuera de rango")
    elif n >= 90:
        print("Sobresaliente")
    elif n >= 80:
        print("Notable")
    elif n >= 50:
        print("Aprobado")
    else:
        print("Suspenso")
except ValueError:
    print("Introduce un entero.")