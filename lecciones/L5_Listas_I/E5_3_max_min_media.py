entrada = input("Números separados por espacios: ").strip()
tokens = entrada.split()
min_fij = False; minimo = 0; maximo = 0; suma = 0; cont = 0
try:
    for t in tokens:
        n = int(t)
        if not min_fij:
            minimo = n; maximo = n; min_fij = True
        if n < minimo: minimo = n
        if n > maximo: maximo = n
        suma = suma + n; cont = cont + 1
    if cont == 0:
        print("No se introdujeron números")
    else:
        media = suma / cont
        print(f"Maximo --> {maximo}")
        print(f"Minimo --> {minimo}")
        print(f"Media --> {media:.2f}")
except ValueError:
    print("Debes introducir enteros.")