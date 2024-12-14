from Clases import Inventario, Producto

def main():
    inventario = Inventario()

    # Crear productos
    producto1 = Producto("001", "Laptop", 1500.00, 10)
    producto2 = Producto("002", "Mouse", 25.50, 50)
    producto3 = Producto("003", "Teclado", 45.75, 30)

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
