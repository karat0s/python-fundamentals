producto = input("Producto: ").strip()
precio_txt = input("Precio: ").strip()
uds_txt = input("Unidades: ").strip()
try:
    precio = float(precio_txt); uds = int(uds_txt)
    subtotal = precio * uds; prod = producto[:12]
    print(f"|{prod:<12}|{uds:>3}|{precio:>8.2f}|{subtotal:>10.2f}|")
except ValueError:
    print("Datos no válidos.")