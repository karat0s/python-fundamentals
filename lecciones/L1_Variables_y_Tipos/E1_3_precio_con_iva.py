precio_base_txt = input("Precio base: ").strip()
iva_pct_txt = input("IVA (% entero): ").strip()
try:
    precio_base = float(precio_base_txt); iva_pct = int(iva_pct_txt)
    precio_final = precio_base * (1 + iva_pct / 100)
    print(f"Precio base: {precio_base}€")
    print(f"IVA: {iva_pct}%")
    print(f"Total con IVA: {precio_final}€")
except ValueError:
    print("Introduce un float para precio y un entero para IVA.")