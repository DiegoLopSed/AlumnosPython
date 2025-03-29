from INVENTARIO import *



def Menu_Empleado():
    print('Bienvenido')
    
    print('1.Agregar producto')    
    print('2.Listar productos')
    print('3.Eliminar productos')
    print('4.Salir')
    while True:
        try:
             option = int(input('Opcion:'))
             if option == 1:
                print('Producto a agregar:')

             if option == 2:
                IVN.INVENTARIO_EMPLEADO()
             if option == 3:
                print('Producto a eliminar')
             if option == 4:
                break
             else:
                 raise ValueError('NO SE ADMITEN OTROS NUMEROS Y/O LETRAS')
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)