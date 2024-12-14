class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):

        return f"[{self.codigo}] {self.nombre} - Precio: ${self.precio:.2f}, Cantidad: {self.cantidad}"