n_txt = input("Introduce un entero: ").strip()
try:
    n = int(n_txt)
    if n < 1:
        print("n debe ser >= 1")
    else:
        salida = ""; primero = True
        for i in range(1, n + 1):
            if i % 2 != 0:
                if primero:
                    salida = str(i); primero = False
                else:
                    salida = salida + " " + str(i)
        print(salida)
except ValueError:
    print("Debes introducir un entero")