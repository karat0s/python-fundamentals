a_txt = input("a (entero): ").strip()
b_txt = input("b (entero): ").strip()
try:
    a = int(a_txt); b = int(b_txt)
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Producto: {a * b}")
    print(f"División real: {a / b}")
    print(f"División entera: {a // b}")
    print(f"Resto: {a % b}")
    print(f"Potencia: {a ** b}")
except ValueError:
    print("Debes introducir enteros.")