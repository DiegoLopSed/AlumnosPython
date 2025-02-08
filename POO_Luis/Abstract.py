from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, id_producto, nombre, precio, categoria, stock,):
        self._id_producto = id_producto
        self._nombre = nombre 
        self._precio = precio 
        self._categoria = categoria 
        self._stock = stock 
        self._estado = "Activo"

    @abstractmethod
    def info(self):
        pass

    def vender(self, cantidad):

        if self._estado != "Activo":
            print("Lo sentimos, producto descontinuado")
        else:
            if cantidad > self._stock:
                raise ValueError("Stock insuficiente.")
            else:
                self._stock -= cantidad
                print("Producto comprado exitosamente, Quedan: ",self._stock)


    def agregar_stock(self, cantidad):
        if self._estado != "Activo":
            print("Se requieren más productos.")
        else:
            if cantidad < 0:
                raise ValueError("Agregar más al stock")
            else:
                self._stock += cantidad
                print("Productos agregados al stock.")
        
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
    def estado(self):
        return self._estado
        
    @property
    def categoria(self):
        return self._categoria
    
    @property
    def stock(self):
        return self._stock
    
    def change_n(self):
        nuevo_nombre = input("Agregue el nuevo nombre:")
        self._nombre = nuevo_nombre

    def descontinuar(self):
        if self._estado == "Activo":
            self._estado = "Descontinuado"
        else:
            self._estado = "Activo"


    def change_p():
        pass
            