cadena_txt = input("Dame una cadena: ").strip()
if not cadena_txt:
    print("Vacía")
elif len(cadena_txt) < 5:
    print("Corta")
elif 5 <= len(cadena_txt) <= 10:
    print("Media")
else:
    print("Larga")