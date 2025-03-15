from producto import Producto 

class tel (Producto):

    def __init__(self, nombre, precio, categoria, stock,procesador):
       super().__init__(nombre, precio, categoria, stock)
       self.procesador = procesador

    def info(self):
      print ('Nombre del Telefono:', self._nombre)
      print ('Precio: $', self._precio)
      print ('Stock:', self._stock)
      print ('Categoria:', self._categoria)



f5 = tel('Xiaomi Poco F5 pro',10000 ,'media alta',30,'Snapdragon 8+ gen1' )
Iphone_16 = tel('Iphone 16 Pro Max',40000 ,'alta',30,'A18 Bionic' )
S25_Ultra = tel('Samsung Galaxy S25 Ultra',30000 ,'alta',30,'Snapdragon 8 elite For Galaxy' )
Red_Magic = tel('ZTE Nubia Red Magic 10s Pro',20000 ,'alta',30,'Snapdragon 8 Elite+' )
Xiaomi_14 = tel('Xiaomi 14 Ultra',25000 ,'alta',30,'Snapdragon 8+ Gen1' )

res = int(input('Ingresa "1" para comprar  Ingresa "2" para añadir stock'))
if res == 1:
    Iphone_16.info()
    intro = int(input('Introduce la cantidad que deses comprar:'))
    Iphone_16.vender_producto(intro)
    Iphone_16.info()
else:
    Iphone_16.info()
    añadir = int(input('Ingresa la cantidad que desees añadir'))
    Iphone_16.añadir_producto(añadir)
    Iphone_16.info()






