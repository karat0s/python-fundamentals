# Imprimir las palabras comunes a dos líneas, en el orden de la 1ª línea, sin duplicados, en una sola línea separadas por espacios.

palabras_1_txt = input("Introduce palabras separadas por espacios: ").strip().split()
palabras_2_txt = input("Introduce palabras separadas por espacios: ").strip().split()

set_2 = set(palabras_2_txt)
palabras_out = []

for p in palabras_1_txt:
    if p in set_2 and p not in palabras_out:
        palabras_out.append(p)

print(" ".join(palabras_out))
