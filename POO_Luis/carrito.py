from clases import *
class carrito:

    def __init__(self, id_carrito, nombre_cliente):
        productos =[]

        self._id_carrito = id_carrito
        self._productos = productos
        self._nombre = nombre_cliente

    def add_item(self,obj):
        self._productos.append(obj)

    def list_product(self):

        if not self._productos:
            print("El carrito está vacío.")
        else:
            for product in self._productos:
                print('nombre: ',product.nombre, '$', product.precio)

    def remove_item(self, producto):

        if producto in self._productos:
            self._productos.remove(producto)
            print(f"Producto '{producto}' eliminado del carrito.")
        else:
            print(f"El producto '{producto}' no se encuentra en el carrito.")

    def clear_cart(self):
        self._productos.clear()
        print("El carrito ha sido vaciado.")


    def add(self, producto, ammount):
        if producto.venta(ammount):

            carrito1 = carrito(1,'Ricardo')

            carrito1.list_product()

            carrito1.add_item(cheetos)

            carrito1.list_product()

