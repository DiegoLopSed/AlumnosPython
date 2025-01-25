from PRODUCTO import Producto
from CATEGORIAS import *

class Helados(Producto):
    def info(self):
        print(f'Nombre: {self.nombre}')    
        print(f'Precio: {self.precio} ')
        print(f'Categoria: {self.categoria}')      

Oreo = Helados('Oreo',32,categoria[7])
Dracula = Helados ('Dracula', 34,categoria[2])
Chococono = Helados ('Chococono', 30, categoria[1])
Colombina = Helados('Colombina',32, categoria[5])
Casero = Helados ('Casero', 28, categoria[7])
