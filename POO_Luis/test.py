def menu():
    print("Bienvenido")
    
    print("0. Iniciar sesión como usuario")
    print("1. Crear cuenta ")
    print("2. Ver productos")
    print("3. Crear carrito")
    print("4. Buscar producto por nombre o Id")
    print("5. Añadir productos al carrito")
    print("6. Eliminar productos del carrito")
    print("7. Eliminar carrito")
    print("8. Salir")



while True:

    menu()
    option = int(input("Ingrese una opción: "))
    if option == 0: 
        print("Iniciando sesión como usuario...")
    if option == 1:
        print("Añadir correo electrónico")
    if option == 2:
        print("Mostrando productos...")
    if option == 3:
        print("Creando carrito ...")
    if option == 4:
        print("Buscando producto ...")
    if option == 5:
        print("Añadiendo productos al carrito...")
    if option == 6:
        print("Eliminando productos del carrito...")
    if option == 7:
        print("Eliminando carrito...")
    if option == 8:
        print("Gracias por su visita")
        break
    else:
        print("Opción no válida. Por favor intente de nuevo.")    


    