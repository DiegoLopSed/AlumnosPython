from OBJETOS import *

class CARRITO:

    def __init__(self,nombre_usaurio):
        productos = []
        cantidad = []
        self._nombre_usuario = nombre_usaurio
        self.productos = productos
        self.cantidad = cantidad

    def add_item(self,producto,ammount):
        if producto.venta(ammount):
            self.productos.append(producto)
            self.cantidad.append(ammount)

    def ls_object(self):
        
        if len(self.productos) <= 0:
            print('Carrito: \n')
            print('El carrito esta vacio')
        else:
            print('==========================')
            print('Carrito: \n')
            i = 0
            for producto in self.productos:
                print(f'Cantidad',self.cantidad[i],'Producto:',producto.nombre,'$',producto.precio)
                i+= 1
            print('==========================')

    def remove_object(self,producto):
        
        
        if  producto in self.productos:
            index = self.productos.index(producto)
            self.productos.remove(producto)
            self.cantidad.remove(self.cantidad[index])
            print(f'Producto:',producto.nombre, 'ha sido eliminado')
            
        else:
            print(f'El producto:',producto.nombre, 'no se encuentra en el carrito')
    
    def clear_object(self):
        self.productos.clear()
        print('El carrito se ha vaciado.')

carrito1 = CARRITO('Alexys')

Oreo.info()
Dracula.info()
carrito1.ls_object()
carrito1.add_item(Oreo,3)
carrito1.add_item(Dracula,5)
carrito1.ls_object()
carrito1.remove_object(Oreo)
carrito1.ls_object()
carrito1.clear_object()
Oreo.info()
Dracula.info()

