n_txt = input("Entero: ").strip()
try:
    n = int(n_txt)
    print("Par" if n % 2 == 0 else "Impar")
except ValueError:
    print("Debes introducir un entero.")