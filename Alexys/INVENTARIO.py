from OBJETOS import *

class INVENTARY():

    def __init__(self):
        inventario = [Oreo,Dracula,Chococono,Colombina,Casero]
        self.inventario  =  inventario
    def INVENTARIO_USUARIO(self):
            print('Productos:')
            i = 0
            for producto in self.inventario:
                i += 1
                print(f'{i}.',producto.nombre,'$',producto.precio)
            print('==========================')
    def INVENTARIO_EMPLEADO(self):
            for producto in self.inventario:
                print(f'INVENTARIO',producto.info)
            print('===========================')
IVN = INVENTARY()
        