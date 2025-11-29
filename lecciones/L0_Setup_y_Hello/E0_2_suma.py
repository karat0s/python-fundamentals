n1_txt = input("Introduce el primer número: ").strip()
n2_txt = input("Introduce el segundo número: ").strip()
try:
    n1 = int(n1_txt); n2 = int(n2_txt)
    print(f"Suma: {n1 + n2}")
    print(f"Producto: {n1 * n2}")
except ValueError:
    print("Error: introduce números enteros válidos.")