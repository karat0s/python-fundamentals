s = input("Frase: ").strip().lower().replace(" ", "")
print("SI" if s == s[::-1] else "NO")