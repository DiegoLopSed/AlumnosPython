from clase_abc import *

class med(Producto):
    def __init__(self, nombre, precio, categoria, stock,componente):
        super().__init__(nombre, precio, categoria, stock,componente)

    

paracetamol = med('paracetamol',15,'',15,'paracetamol')
ibuprofeno = med('',50,'',30,'')
terramicina = med('',60,'',78,'')
xl3 = med('',25,'',76,'')
