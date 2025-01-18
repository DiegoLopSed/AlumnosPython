from abc import ABC , abstractmethod

class Producto (ABC):
    

    def __init__(self, nombre, precio):
      self._nombre = nombre
      self._precio = precio
      
    @property #get
    def nombre(self):
       return self._nombre
    @nombre.setter # set
    def nombre (self, nuevo_nombre):
       self._nombre = nuevo_nombre

    @property #get
    def precio(self):
        return self._precio
    @precio.setter #set
    def precio (self, nuevo_precio):
       self._precio = nuevo_precio
    
    @abstractmethod
    def info(self):
        pass
    
    def cambio_precio(self):
        nuevo_precio = (self._precio * 10) /  100
        print(f'Cambio de precio: {nuevo_precio}')
       # self._precio raise += nuevo_precio()
        # print(f'Precio nuevo: {precio_final}')

    

