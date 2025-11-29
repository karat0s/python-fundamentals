frase_txt = input("Dame una frase: ").strip()
num_vocales = 0
for ch in frase_txt:
    c = ch.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        num_vocales = num_vocales + 1
print(f"Total de vocales: {num_vocales}")