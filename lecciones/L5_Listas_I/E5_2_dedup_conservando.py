entrada = input("Números separados por espacios: ").strip()
tokens = entrada.split()
sin_dups = []
for t in tokens:
    if t not in sin_dups:
        sin_dups.append(t)
print(" ".join(sin_dups))