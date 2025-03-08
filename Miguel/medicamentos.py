from producto import *

class med(Producto):

   def info(self):
      print ('Nombre del medicamento:', self._nombre)
      print ('Precio: $', self._precio)
      print ('Stock:', self._stock)
      print ('Categoria:', self._categoria)


obj = med('Paracetamol',55,'---',5)
obj.info()
intro = int(input('Introduce la cantidad que desees comprar:'))
obj.vender_producto(intro)
obj.info()
