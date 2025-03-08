from clase_abc import Producto 

class tel (Producto):

    def __init__(nombre, precio, categoria, stock,prcesador):
        super().__init__(nombre, precio, categoria, stock,prcesador)

    def info (self):
        print('Modelo',self.nombre)




#categoria = gama

f5 = tel('Xiaomi Poco F5 pro',10000 ,'media alta',30,'Snapdragon 8+ gen1' )
Iphone_16 = tel('Iphone 16 Pro Max',40000 ,'alta',30,'A18 Bionic' )
S25_Ultra = tel('Samsung Galaxy S25 Ultra',30000 ,'alta',30,'Snapdragon 8 elite For Galaxy' )
Red_Magic = tel('ZTE Nubia Red Magic 10s Pro',20000 ,'alta',30,'Snapdragon 8 Elite+' )
Xiaomi_14 = tel('Xiaomi 14 Ultra',25000 ,'alta',30,'Snapdragon 8+ Gen1' )


























