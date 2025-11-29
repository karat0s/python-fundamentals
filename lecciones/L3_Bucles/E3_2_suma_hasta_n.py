n_txt = input("n (entero >= 1): ").strip()
try:
    n = int(n_txt)
    if n >= 1:
        i = 1; total = 0
        while i <= n:
            total = total + i
            i = i + 1
        print(f"Suma 1..{n} = {total}")
    else:
        print("n debe ser >= 1")
except ValueError:
    print("Debes introducir un entero.")