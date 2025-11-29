nums_txt = input().strip()
w_txt = input().strip()

try:
    nums = [int(t) for t in nums_txt.split()] if nums_txt else []
    w = int(w_txt)
    if w < 1:
        print("w debe ser >= 1")
    elif len(nums) < w:
        print("Longitud insuficiente")
    else:
        # suma de la primera ventana
        suma = 0
        i = 0
        while i < w:
            suma += nums[i]
            i += 1
        max_suma = suma

        # desliza la ventana
        i = w
        while i < len(nums):
            suma -= nums[i - w]
            suma += nums[i]
            if suma > max_suma:
                max_suma = suma
            i += 1

        print(max_suma)
except ValueError:
    print("Entrada inválida.")
