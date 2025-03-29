from abc import abstractmethod

class Producto:
   def __init__(self, nombre, precio, categoria, stock):
      self._nombre = nombre
      self._precio = precio
      self._categoria = categoria
      self._status = 'Activo'
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
   def status(self):
      return self._status
   @status.setter
   def status(self, nuevo_status):
      self._status =  nuevo_status
         
   @abstractmethod
   def info(self):
        pass
      
   def vender_producto(self,  stock):

      if stock <= 0:
         print ('Introduce un munero valido')
      else: 
         if stock > self._stock:
            print('Stock insuficiente')
         else:
            print('Compra exitosa')
            self._stock -= stock 
            
   def añadir_producto(self,  stock):

      if stock <= 0:
         print ('Introduce un munero valido')
      else: 
            self._stock += stock 
            print('Añadido Correctamente')
               
   def cambiar_precio_porcentaje(self, porcentaje):

         aumento = 1 + (porcentaje / 100)
         precio_anterior = self._precio
         self._precio = self._precio * aumento
         print('Precio actualizado correctamente')

   def cambiar_status(self, nuevo_status):
      self._status = nuevo_status
      print('Status actualizado correctamente')
