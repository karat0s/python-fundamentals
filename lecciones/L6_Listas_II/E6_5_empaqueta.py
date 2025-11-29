palabras = input().split()
resultado = []
prev = None
for p in palabras:
    if prev is None or p != prev:
        resultado.append(p)
    prev = p
print(" ".join(resultado))
