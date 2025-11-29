email = input("Email: ").strip().lower()
print("OK" if "@" in email and "." in email else "Formato incorrecto")