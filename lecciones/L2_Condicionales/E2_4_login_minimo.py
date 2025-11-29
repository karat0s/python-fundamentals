usuario = input("Usuario: ").strip()
password = input("Password: ").strip()
if not usuario or not password:
    print("Faltan credenciales")
elif usuario == "admin" and password == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")