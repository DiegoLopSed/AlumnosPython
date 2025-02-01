from abc import ABC , abstractmethod

class Producto (ABC):
    

    def __init__(self, nombre, precio, categoria, stock):
      self._nombre = nombre
      self._precio = precio
      self._categoria = categoria
      self._estado = 'Activo'
      self._stock = stock
      
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

    @property 
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, nueva_cantidad):
         self._cantidad = nueva_cantidad

    @property 
    def categoria (self):
       return self._categoria
    @categoria.setter
    def categoria (self, nueva_categoria):
       self._categoria = nueva_categoria
    
   
    @property
    def estado(self):
       return self._estado
    @estado.setter
    def estado(self, nuevo_estado):
        self._estado =  nuevo_estado

    @abstractmethod

    def info(self):
        pass
    
    def cambio_precio(self):
        nuevo_precio = (self._precio * 10) /  100
        print(f'Cambio de precio: {nuevo_precio}')
       # self._precio raise += nuevo_precio()
        # print(f'Precio nuevo: {precio_final}')

    def venta (self,cantidad):
       if self._estado != 'Activo':
          print('lo sentimos, producto agotado')
       else: 
          if cantidad > self._stock:
             print('stock insuficiente')
          else: 
             print('producto comprado exitosamente')
             self._stock -= cantidad

    def add(self,cantidad):
       if cantidad < 0:
          print('Ingrese un numero valido')
          raise ValueError("No se admiten numeros negativos")
       else:
         self._stock += cantidad
         print(f'Se han agregado {cantidad} {self.nombre}')
    def change_status(self):
        if self._estado == 'Activo':
           nuevo_estado = 'Inactivo'
           self._estado = nuevo_estado
        elif self._estado == 'Inactivo':
           nuevo_estado = 'Activo'
           self._estado = nuevo_estado
    



