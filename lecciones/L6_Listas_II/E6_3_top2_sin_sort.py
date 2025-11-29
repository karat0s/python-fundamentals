linea = input().strip()
tokens = linea.split()

mayor1_fij = False
mayor1 = None
mayor2 = None

try:
    for t in tokens:
        x = int(t)
        if not mayor1_fij:
            mayor1 = x
            mayor2 = None
            mayor1_fij = True
        else:
            if x == mayor1 or (mayor2 is not None and x == mayor2):
                continue
            if x > mayor1:
                mayor2 = mayor1
                mayor1 = x
            elif mayor2 is None or (x > mayor2 and x < mayor1):
                mayor2 = x

    if not mayor1_fij:
        print("NA")
    else:
        if mayor2 is None:
            print(mayor1, "NA")
        else:
            print(mayor1, mayor2)
except ValueError:
    print("Debes introducir enteros separados por espacios.")
