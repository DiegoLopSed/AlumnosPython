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
   
<<<<<<< HEAD:Miguel/producto.py
   def vender_producto(self,  stock):

      if stock <= 0:
         print ('Introduce un munero valido')
      else: 
         if stock > self._stock:
            print('Stock insuficiente')
         else:
            print('Compra exitosa')
            self._stock -= stock 
         
=======
   



















































   
>>>>>>> 353c8f146181707cb04976f371d07eb32e0db673:Miguel/clase_abc.py
