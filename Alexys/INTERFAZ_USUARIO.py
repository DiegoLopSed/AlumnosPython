from CARRITO import *
from INVENTARIO import *
from time import sleep  

def Menu_Usuario():
    print('Bienvenido apreciado cliente \n')
    sleep(2)
    while True:
        try:
             IVN.INVENTARIO_USUARIO()
             sleep(2)
             print('Estos son los productos disponibles. :) \n')
             print('1.Agregar a carrito')        
             print('2.Ver carrito')
             print('3.Remover de carrito')
             print('4.Vaciar carrito')
             print('5.Comprar')
             print('6.Salir')
             sleep(1)
             option = int(input('Opcion:'))
             if option == 1:
                Producto = int(input('Producto a agregar:'))
                Cantidad = int(input('Cantidad:'))
                index = Producto - 1
                Producto_C = IVN.inventario[index]
                carrito1.add_item(Producto_C,Cantidad)
                print(f'{Cantidad}  {Producto_C.nombre} agregado/s al carrito')
                print('==========================')      
                sleep(3)
             if option == 2:
                carrito1.ls_object()
                sleep(3)
             if option == 3:
                Producto = int(input('Producto a eliminar:'))   
                index = Producto - 1
                Producto_C = IVN.inventario[index]
                carrito1.remove_object(Producto_C)
                print(f'{Producto_C.nombre} eliminado del carrito')
                sleep(3)
             if option == 4:
                AVISO = input('Estas seguro de que quieres vaciar todo tu carrito? si/no  1/2: ').lower()
                print('No podras revertirlo')
                if AVISO == 'si' or '1':
                    carrito1.clear_object()
                else:
                    print('nao')
             if option == 5:
                 sleep(3)
             if option == 6:
                 break
                
        except NameError as e:
            print(e)
        except Exception as e:
            print(e)