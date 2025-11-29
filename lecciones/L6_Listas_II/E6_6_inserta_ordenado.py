nums_line = input().strip()
x_txt = input().strip()

try:
    nums = [int(t) for t in nums_line.split()] if nums_line else []
    x = int(x_txt)

    res = []
    insertado = False
    i = 0
    while i < len(nums):
        n = nums[i]
        if not insertado and x <= n:
            res.append(x)
            insertado = True
        res.append(n)
        i += 1
    if not insertado:
        res.append(x)

    # imprime en una sola línea
    salida = ""
    primero = True
    for n in res:
        if primero:
            salida = str(n)
            primero = False
        else:
            salida = salida + " " + str(n)
    print(salida)
except ValueError:
    print("Entrada inválida.")
