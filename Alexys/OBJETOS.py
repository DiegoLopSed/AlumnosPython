from PRACTICA_ABSTRACCION import Producto


class Helados(Producto):
    def info(self):
        print(f'Nombre: {self.nombre}')    
        print(f'Precio: {self.precio} ')      

Oreo = Helados('Oreo',32)

Oreo.info()
Oreo.cambio_precio()
