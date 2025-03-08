users = ["Diego", "Alexis", "Miguel","Luis"]
passwords = ["123","456","789","321"]
usuario = input("Usuario: ")
password = input("Contraseña: ")
cont = 0
for user in users:
    
    if users[cont] == usuario and passwords[cont] == password:
        acces = True
        break
    else:
        acces = False
    cont += 1
    
if acces != True:
    print("Acceso denegado")
else: 
    print("Accesos concedido")