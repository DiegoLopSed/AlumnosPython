from Bebidas import *
from Categorias import *


predator = Bebidas(1,'Predator Energy',20,bebidas[1],50,fecha_actual)
monster_white = Bebidas(2,'Monster White',55,bebidas[1],50,fecha_actual)
amper = Bebidas(3,'Amper Energy',20,bebidas[1],50,fecha_actual)
bonafont = Bebidas(4,'Bonafont',18,bebidas[4],50,fecha_actual)
whisky = Bebidas(5,'Johnnie Walker',2500,bebidas[0],15,fecha_actual)
mezcal = Bebidas(6,'400 Conejos',980,bebidas[0],20,fecha_actual)


carrito = [predator,monster_white,amper,bonafont,whisky,mezcal]

for productos in carrito:
    productos.info()
    print('==========')
    
carrito.clear(mezcal)

for productos in carrito:
    productos.info()
    print('==========')
