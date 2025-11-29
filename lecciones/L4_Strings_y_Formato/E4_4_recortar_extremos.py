s = input("Cadena: ").strip()
ini_txt = input("Inicio (entero): ").strip()
fin_txt = input("Fin (entero): ").strip()
try:
    ini = int(ini_txt); fin = int(fin_txt)
    if 0 <= ini < fin <= len(s):
        print(s[ini:fin])
    else:
        print("Rango inválido")
except ValueError:
    print("Debes introducir enteros.")