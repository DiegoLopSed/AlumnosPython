
class Inventario:
    def __init__(self):
        
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            self.productos[producto.codigo].cantidad += producto.cantidad
        else:
            self.productos[producto.codigo] = producto

    def eliminar_producto(self, codigo):

        if codigo in self.productos:
            del self.productos[codigo]
        else:
            print(f"Producto con código {codigo} no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def buscar_producto(self, codigo):

        return self.productos.get(codigo, None)
