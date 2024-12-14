
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


class Productos:
    def __init__(self, codigo, nombre, precio, cantidad,marca):

        self.marca = marca
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):

        return f"[{self.codigo}] {self.nombre} - Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}, Marca {self.marca}"


def main():
    inventario = Inventario()

    # Crear productos
    producto1 = Productos("001", "Laptop", 1500.00, 10,"DELL")
    producto2 = Productos("002", "Mouse", 25.50, 50,"HP")
    producto3 = Productos("003", "Teclado", 45.75, 30,"DELL")

    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)

    # Mostrar inventario
    print("\nInventario actual:")
    inventario.mostrar_inventario()

    # Buscar un producto
    print("\nBuscando el producto con código '002':")
    producto_encontrado = inventario.buscar_producto("002")
    if producto_encontrado:
        print(producto_encontrado)
    else:
        print("Producto no encontrado.")

    # Eliminar un producto
    print("\nEliminando el producto con código '001'.")
    inventario.eliminar_producto("001")

    # Mostrar inventario actualizado
    print("\nInventario actualizado:")
    inventario.mostrar_inventario()

if __name__ == "__main__":
    main()
