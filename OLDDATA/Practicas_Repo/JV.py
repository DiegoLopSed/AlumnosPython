def add_user():
    name1 = input('Ingresa el nombre del nuevo usuario: ')
    users.append(name1)

def list_users():
    print('Lista de usuarios actual')
    for user in users:
        print(user)

user_name = input("Ingresa tu usuario: ")  
if user_name == "Dave":   
    print("Get off my computer Dave!")   
elif user_name == "angela_catlady_87":   
    print("I know it is you, Dave! Go away!")   
elif user_name == "Javi":   
    print("Access Granted.")   
else:   
    print("Username not recognized.")


users = []
op=''

while op != 'Salir':

    print('Bienvenido, el menú de opciones es:')
    print('1. Ingresar nombre de nuevo usuario')
    print('2. Ver listado de usuarios')
    print('3. Finalizar sesión')
    
    op = input('Ingrese la opcion elegida: ')

    if op == '1':
        add_user()
    if op == '2':
        list_users()
    if op == '3':
        break

