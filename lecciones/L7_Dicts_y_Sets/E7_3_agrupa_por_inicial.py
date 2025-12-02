palabras = input().strip().split()
p_dict = {}
p_list = []

for p in palabras:
    p_upper = p[0].upper()
    if p_upper in p_dict:
        p_dict[p_upper] += 1
    else:
        p_dict[p_upper] = 1

for k in p_dict.keys():
    p_list.append(k)

p_list.sort()

for p in p_list:
    print(f"{p}: {p_dict[p]}")
