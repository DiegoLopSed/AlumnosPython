from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, id_producto, nombre, precio, categoria, stock,):
        self._id_producto = id_producto
        self._nombre = nombre 
        self._precio = precio 
        self._categoria = categoria 
        self._stock = stock 
        self.estado = " Activo"

    @abstractmethod
    def info(self):
        pass

    def vender(self, cantidad):
        if self._estado != "Activo":
            print("Activo")



    @property
    def id_producto(self):
        return self._id_producto
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def precio(self):
        return self._precio
    
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def stock(self):
        return self._stock
    