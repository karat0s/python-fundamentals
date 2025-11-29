frase_txt = input("Introduce una frase: ").strip().lower()
espacios = 0; vocales = 0
print(f"Longitud: {len(frase_txt)}")
for ch in frase_txt:
    if ch == " ":
        espacios += 1
    elif ch in "aeiou":
        vocales += 1
print(f"Espacios: {espacios}")
print(f"Vocales: {vocales}")