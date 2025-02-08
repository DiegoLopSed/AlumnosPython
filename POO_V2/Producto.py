from abc import ABC, abstractmethod
from datetime import datetime


class Producto(ABC):
    def __init__(self, id_producto, nombre, precio, categoria, stock, tiempo_util):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria
        self._stock = stock
        self._estado = "Activo"
        self._fecha_creacion = datetime.now()
        self._tiempo_util = (
            datetime.strptime(tiempo_util, "%d-%m-%Y %H:%M:%S.%f")
            if isinstance(tiempo_util, str)
            else tiempo_util
        )

    @abstractmethod
    def info(self):
        pass

    def vender(self, cantidad):
        if self._estado != "Activo":
            raise Exception("No se puede vender un producto descontinuado.")
        if cantidad > self._stock:
            raise ValueError("Stock insuficiente.")
        else:
            self._stock -= cantidad
            print("Producto comprado exitosamente")

    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        self._stock += cantidad

    def descontinuar(self):
        self._estado = "Descontinuado"

    def detalles(self):
        return {
            "ID": self._id_producto,
            "Nombre": self._nombre,
            "Precio": self._precio,
            "Categoría": self._categoria,
            "Stock": self._stock,
            "Estado": self._estado,
            "Fecha de Creación": self._fecha_creacion.strftime("%d-%m-%Y"),
            "Tiempo Útil": self._tiempo_util.strftime("%d-%m-%Y"),
        }

    def caducar(self, meses):
        if meses < 0:
            raise ValueError("El tiempo no puede ser negativo.")
        self._tiempo_util += relativedelta(months=meses)

    def subir_precio(self, porcentaje):
        if porcentaje <= 0:
            raise ValueError("El porcentaje debe ser mayor a 0.")
        self._precio += round(self._precio * porcentaje / 100, 2)

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

    @property
    def estado(self):
        return self._estado

