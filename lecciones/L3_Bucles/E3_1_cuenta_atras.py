n_txt = input("n (entero >= 0): ").strip()
try:
    n = int(n_txt)
    if n < 0:
        print("n debe ser >= 0")
    else:
        for i in range(n, -1, -1):
            print(i)
except ValueError:
    print("Debes introducir un entero.")