email_txt = input("Introduce un email: ").strip()
if "@" in email_txt and "." in email_txt:
    print("Parece un email")
else:
    print("No es un email")