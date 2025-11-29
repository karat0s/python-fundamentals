# scaffold_full.py — Genera el proyecto con tus soluciones (L0–L6) y L7 en esqueleto
from pathlib import Path

files = {
    # --- raíz ---
    "README.md": """# Python Fundamentals — Dani

Incluye tus soluciones hasta L6 y deja L7 en esqueletos (para que los resuelvas tú).
Regla del curso: no usar imports/funciones hasta que la lección lo introduzca.

## Ejecutar (ejemplo)
python lecciones/L3_Bucles/E3_1_cuenta_atras.py
""",
    ".gitignore": """.venv/
__pycache__/
*.pyc
.vscode/
.idea/
""",

    # --- L0 ---
    "lecciones/L0_Setup_y_Hello/E0_1_eco.py": """texto = input("Escribe una línea: ").strip()
print(f"Texto: {texto}")
print(f"Longitud: {len(texto)}")
print(f"MAYUS: {texto.upper()}")""",
    "lecciones/L0_Setup_y_Hello/E0_2_suma.py": """n1_txt = input("Introduce el primer número: ").strip()
n2_txt = input("Introduce el segundo número: ").strip()
try:
    n1 = int(n1_txt); n2 = int(n2_txt)
    print(f"Suma: {n1 + n2}")
    print(f"Producto: {n1 * n2}")
except ValueError:
    print("Error: introduce números enteros válidos.")""",

    # --- L1 ---
    "lecciones/L1_Variables_y_Tipos/E1_1_perfil_basico.py": """nombre = input("Nombre: ").strip()
edad_txt = input("Edad (entera): ").strip()
ciudad = input("Ciudad: ").strip()
try:
    edad = int(edad_txt)
    print(f"Hola {nombre}, tienes {edad} y vives en {ciudad}.")
    print(f"El año que viene tendrás {edad + 1}.")
except ValueError:
    print("La edad debe ser un entero.")""",
    "lecciones/L1_Variables_y_Tipos/E1_2_operaciones_enteros.py": """a_txt = input("a (entero): ").strip()
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
    print("Debes introducir enteros.")""",
    "lecciones/L1_Variables_y_Tipos/E1_3_precio_con_iva.py": """precio_base_txt = input("Precio base: ").strip()
iva_pct_txt = input("IVA (% entero): ").strip()
try:
    precio_base = float(precio_base_txt); iva_pct = int(iva_pct_txt)
    precio_final = precio_base * (1 + iva_pct / 100)
    print(f"Precio base: {precio_base}€")
    print(f"IVA: {iva_pct}%")
    print(f"Total con IVA: {precio_final}€")
except ValueError:
    print("Introduce un float para precio y un entero para IVA.")""",
    "lecciones/L1_Variables_y_Tipos/E1_4_texto_transform.py": """frase = input("Frase: ").strip()
print(f"Longitud: {len(frase)}")
print(f"MAYUS: {frase.upper()}")
print(f"Con guiones bajos: {frase.replace(' ', '_')}")""",

    # --- L2 (tus practicados) ---
    "lecciones/L2_Condicionales/rango_edad.py": """edad_txt = input("Tu edad: ").strip()
try:
    edad = int(edad_txt)
    if edad < 0:
        print("Edad no válida")
    elif edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
except ValueError:
    print("Debes introducir un número entero.")""",
    "lecciones/L2_Condicionales/valida_correo_basico.py": """email_txt = input("Introduce un email: ").strip()
if "@" in email_txt and "." in email_txt:
    print("Parece un email")
else:
    print("No es un email")""",
    "lecciones/L2_Condicionales/clasifica_cadena.py": """cadena_txt = input("Dame una cadena: ").strip()
if not cadena_txt:
    print("Vacía")
elif len(cadena_txt) < 5:
    print("Corta")
elif 5 <= len(cadena_txt) <= 10:
    print("Media")
else:
    print("Larga")""",

    # --- L2 (oficiales de la lección) ---
    "lecciones/L2_Condicionales/E2_1_par_impar.py": """n_txt = input("Entero: ").strip()
try:
    n = int(n_txt)
    print("Par" if n % 2 == 0 else "Impar")
except ValueError:
    print("Debes introducir un entero.")""",
    "lecciones/L2_Condicionales/E2_2_nota_a_cadena.py": """n_txt = input("Nota (0-100): ").strip()
try:
    n = int(n_txt)
    if n < 0 or n > 100:
        print("Nota fuera de rango")
    elif n >= 90:
        print("Sobresaliente")
    elif n >= 80:
        print("Notable")
    elif n >= 50:
        print("Aprobado")
    else:
        print("Suspenso")
except ValueError:
    print("Introduce un entero.")""",
    "lecciones/L2_Condicionales/E2_3_calculadora_segura.py": """a_txt = input("a (número): ").strip()
op = input("Operador (+ - * / // % **): ").strip()
b_txt = input("b (número): ").strip()
try:
    a = float(a_txt); b = float(b_txt)
    if op == "+": print(a + b)
    elif op == "-": print(a - b)
    elif op == "*": print(a * b)
    elif op == "/": print(a / b) if b != 0 else print("No se puede dividir entre 0")
    elif op == "//": print(int(a) // int(b)) if b != 0 else print("No se puede dividir entre 0")
    elif op == "%": print(int(a) % int(b)) if b != 0 else print("No se puede dividir entre 0")
    elif op == "**": print(a ** b)
    else: print("Operador no soportado")
except ValueError:
    print("Número no válido.")""",
    "lecciones/L2_Condicionales/E2_4_login_minimo.py": """usuario = input("Usuario: ").strip()
password = input("Password: ").strip()
if not usuario or not password:
    print("Faltan credenciales")
elif usuario == "admin" and password == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")""",

    # --- L3 ---
    "lecciones/L3_Bucles/E3_1_cuenta_atras.py": """n_txt = input("n (entero >= 0): ").strip()
try:
    n = int(n_txt)
    if n < 0:
        print("n debe ser >= 0")
    else:
        for i in range(n, -1, -1):
            print(i)
except ValueError:
    print("Debes introducir un entero.")""",
    "lecciones/L3_Bucles/E3_2_suma_hasta_n.py": """n_txt = input("n (entero >= 1): ").strip()
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
    print("Debes introducir un entero.")""",
    "lecciones/L3_Bucles/E3_3_contar_vocales.py": """frase_txt = input("Dame una frase: ").strip()
num_vocales = 0
for ch in frase_txt:
    c = ch.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        num_vocales = num_vocales + 1
print(f"Total de vocales: {num_vocales}")""",
    "lecciones/L3_Bucles/E3_4_solo_impares.py": """n_txt = input("Introduce un entero: ").strip()
try:
    n = int(n_txt)
    if n < 1:
        print("n debe ser >= 1")
    else:
        salida = ""; primero = True
        for i in range(1, n + 1):
            if i % 2 != 0:
                if primero:
                    salida = str(i); primero = False
                else:
                    salida = salida + " " + str(i)
        print(salida)
except ValueError:
    print("Debes introducir un entero")""",
    "lecciones/L3_Bucles/E3_5_intenta_hasta_ok.py": """palabra = ""
while palabra != "OK":
    palabra = input("Introduce una palabra (OK para salir): ").strip()
print("Hecho")""",

    # --- L4 ---
    "lecciones/L4_Strings_y_Formato/E4_1_iniciales.py": """nombre_apellidos = input("Nombre y apellidos: ").strip()
siglas = ""
for i in range(len(nombre_apellidos)):
    if i == 0 and nombre_apellidos[i] != " ":
        siglas = nombre_apellidos[i] + "."
    elif nombre_apellidos[i] == " ":
        if i + 1 < len(nombre_apellidos) and nombre_apellidos[i + 1] != " ":
            siglas = siglas + nombre_apellidos[i + 1] + "."
print(siglas.upper())""",
    "lecciones/L4_Strings_y_Formato/E4_2_invertir.py": """s = input("Cadena: ").strip()
print(s[::-1] if s else "Vacía")""",
    "lecciones/L4_Strings_y_Formato/E4_3_contadores_basicos.py": """frase_txt = input("Introduce una frase: ").strip().lower()
espacios = 0; vocales = 0
print(f"Longitud: {len(frase_txt)}")
for ch in frase_txt:
    if ch == " ":
        espacios += 1
    elif ch in "aeiou":
        vocales += 1
print(f"Espacios: {espacios}")
print(f"Vocales: {vocales}")""",
    "lecciones/L4_Strings_y_Formato/E4_4_recortar_extremos.py": """s = input("Cadena: ").strip()
ini_txt = input("Inicio (entero): ").strip()
fin_txt = input("Fin (entero): ").strip()
try:
    ini = int(ini_txt); fin = int(fin_txt)
    if 0 <= ini < fin <= len(s):
        print(s[ini:fin])
    else:
        print("Rango inválido")
except ValueError:
    print("Debes introducir enteros.")""",
    "lecciones/L4_Strings_y_Formato/E4_5_ticket_simple.py": """producto = input("Producto: ").strip()
precio_txt = input("Precio: ").strip()
uds_txt = input("Unidades: ").strip()
try:
    precio = float(precio_txt); uds = int(uds_txt)
    subtotal = precio * uds; prod = producto[:12]
    print(f"|{prod:<12}|{uds:>3}|{precio:>8.2f}|{subtotal:>10.2f}|")
except ValueError:
    print("Datos no válidos.")""",
    "lecciones/L4_Strings_y_Formato/E4_6_normaliza_email.py": """email = input("Email: ").strip().lower()
print("OK" if "@" in email and "." in email else "Formato incorrecto")""",

    # --- L5 ---
    "lecciones/L5_Listas_I/E5_1_pares_ordenados.py": """n_txt = input("n (>=1): ").strip()
try:
    n = int(n_txt)
    if n >= 1:
        lista = []
        for i in range(1, n + 1):
            lista.append(i)
        lista.reverse()
        print("Invertida:", " ".join(str(x) for x in lista))
        pares = []
        for x in lista:
            if x % 2 == 0:
                pares.append(x)
        print("Solo pares:", " ".join(str(x) for x in pares))
    else:
        print("El número debe ser >= 1")
except ValueError:
    print("Debes introducir un entero.")""",
    "lecciones/L5_Listas_I/E5_2_dedup_conservando.py": """entrada = input("Números separados por espacios: ").strip()
tokens = entrada.split()
sin_dups = []
for t in tokens:
    if t not in sin_dups:
        sin_dups.append(t)
print(" ".join(sin_dups))""",
    "lecciones/L5_Listas_I/E5_3_max_min_media.py": """entrada = input("Números separados por espacios: ").strip()
tokens = entrada.split()
min_fij = False; minimo = 0; maximo = 0; suma = 0; cont = 0
try:
    for t in tokens:
        n = int(t)
        if not min_fij:
            minimo = n; maximo = n; min_fij = True
        if n < minimo: minimo = n
        if n > maximo: maximo = n
        suma = suma + n; cont = cont + 1
    if cont == 0:
        print("No se introdujeron números")
    else:
        media = suma / cont
        print(f"Maximo --> {maximo}")
        print(f"Minimo --> {minimo}")
        print(f"Media --> {media:.2f}")
except ValueError:
    print("Debes introducir enteros.")""",
    "lecciones/L5_Listas_I/E5_4_rotacion_k.py": "\"\"\"ESQUELETO (lo dejaste sin hacer). Rellénalo tú.\"\"\"\n",
    "lecciones/L5_Listas_I/E5_5_palindromo_lista.py": """s = input("Frase: ").strip().lower().replace(" ", "")
print("SI" if s == s[::-1] else "NO")""",

    # --- L6 (stubs, aún no entregados) ---
    "lecciones/L6_Listas_II/E6_1_compacta_espacios.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",
    "lecciones/L6_Listas_II/E6_2_multiset_lineal.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",
    "lecciones/L6_Listas_II/E6_3_top2_sin_sort.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",
    "lecciones/L6_Listas_II/E6_4_window_maxima.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",
    "lecciones/L6_Listas_II/E6_5_empaqueta.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",
    "lecciones/L6_Listas_II/E6_6_inserta_ordenado.py": "\"\"\"Stub — completa tu solución aquí.\"\"\"\n",

    # --- L7 (esqueletos) ---
    "lecciones/L7_Dicts_y_Sets/E7_1_interseccion_ordenada.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
    "lecciones/L7_Dicts_y_Sets/E7_2_freq_palabras_top.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
    "lecciones/L7_Dicts_y_Sets/E7_3_agrupa_por_inicial.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
    "lecciones/L7_Dicts_y_Sets/E7_4_diferencia_simetrica_lista.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
    "lecciones/L7_Dicts_y_Sets/E7_5_invertible_seguro.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
    "lecciones/L7_Dicts_y_Sets/E7_6_merge_preferente.py": "\"\"\"ESQUELETO — resuélvelo tú (sin imports/funciones).\"\"\"\n",
}

# --- escritura ---
for path, content in files.items():
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

print("✔ Estructura creada. Ya puedes hacer git init y subir a GitHub.")
