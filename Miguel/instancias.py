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
Xiaomi_15 = tel('Xiaomi 14 Ultra',25000 ,'alta',30,'Snapdragon 8+ Gen1' )


telefonos = [f5,Iphone_16,S25_Ultra,Red_Magic,Xiaomi_15]
i=1
for telefono in telefonos:
    print(i, ':',telefono.nombre)
    i+=1

res = int(input('Ingresa "1" para comprar  Ingresa "2" para añadir stock  Ingresa "3" para cambiar el precio:   '))
if res == 1:
    tel = int(input('Introduce el numero del telefono que desees comprar:   '))
    tel = telefonos[tel-1]
    tel.info()
    intro = int(input('Introduce la cantidad que deses comprar:   '))
    tel.vender_producto(intro)
    tel.info()

if res == 2:
    tel = int(input('Ingresa el numero del telefono que desees agregar stock:   '))
    tel = telefonos [tel-1]
    tel.info()
    añadir = int(input('Ingresa la cantidad que desees añadir:   '))
    tel.añadir_producto(añadir)
    tel.info()

if res == 3:
    tel = int(input('Introduce el numero del producto al cual quieres cambiar el precio:   '))
    tel = telefonos[tel-1]
    tel.info()
    porcentaje = int(input('Introduce el porcentaje de aumento:   '))
    tel.cambiar_precio_porcentaje(porcentaje)
    tel.info()
    