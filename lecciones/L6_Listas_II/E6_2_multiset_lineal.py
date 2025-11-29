linea = input().strip()
tokens = linea.split()

valores = []
conteos = []

try:
    for t in tokens:
        n = int(t)
        if n in valores:
            i = valores.index(n)
            conteos[i] = conteos[i] + 1
        else:
            valores.append(n)
            conteos.append(1)

    for i in range(len(valores)):
        print(f"{valores[i]} -> {conteos[i]}")
except ValueError:
    print("Debes introducir enteros separados por espacios.")
