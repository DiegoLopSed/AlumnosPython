from producto import *

class med(Producto):
<<<<<<< HEAD
=======
    def __init__(nombre, precio, categoria, stock,componente):
        super().__init__(nombre, precio, categoria, stock,componente)
>>>>>>> 353c8f146181707cb04976f371d07eb32e0db673

   def info(self):
      print ('Nombre del medicamento:', self._nombre)
      print ('Precio: $', self._precio)
      print ('Stock:', self._stock)
      print ('Categoria:', self._categoria)

<<<<<<< HEAD

obj = med('Paracetamol',55,'---',5)
obj.info()
intro = int(input('Introduce la cantidad que desees comprar:'))
obj.vender_producto(intro)
obj.info()
=======
paracetamol = med('paracetamol',15,'',15,'paracetamol')
ibuprofeno = med('',50,'',30,'')
terramicina = med('',60,'',78,'')
xl3 = med('',25,'',76,'')


>>>>>>> 353c8f146181707cb04976f371d07eb32e0db673
