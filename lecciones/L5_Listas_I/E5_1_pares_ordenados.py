n_txt = input("n (>=1): ").strip()
try:
    n = int(n_txt)
    if n >= 1:
        lista = []
        for i in range(1, n + 1):
            lista.append(i)
        lista.reverse()
        print("Invertida:", " ".join(str(x) for x in lista))
        pares = []
        for x in lista:
            if x % 2 == 0:
                pares.append(x)
        print("Solo pares:", " ".join(str(x) for x in pares))
    else:
        print("El número debe ser >= 1")
except ValueError:
    print("Debes introducir un entero.")