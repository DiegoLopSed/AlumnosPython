from Abstract import Producto

class papas(Producto):
    def info(self):
        print(f"papa: {self.nombre} (${self.precio:.2f})")
        print(f"Categoria: {self.categoria}")
        print(f"Stock: {self.stock}") 
        print(f"Estado: {self._estado}")


#Categoria de productos existentes

categoria = ['Flaming Hot','Bajo Sodio','Frituras de Harina','Sabritas','Barcel','Ruffles','Doritos'] 

chips  = papas(1,'chips sal',20,categoria[4],20)
cheetos = papas(3,'cheetos puff',18,categoria[2],28)
Doritos = papas(9,'doritos incognito',17,categoria[6],69)
Sabritas = papas(10,'sabritas limon',19,categoria[3],99) 
Ruffles = papas(88,'ruffles queso',22,categoria[5],98)
Flaming_hot= papas(74,'cheetos flaming hot',23,categoria[0],34) 

#carrito = [chips,cheetos,Doritos,Sabritas,Ruffles,Flaming_hot]

Doritos.info()

Doritos.vender(6)

Doritos.info()

Sabritas.info()

Sabritas.agregar_stock(8)

Sabritas.info()

Doritos.acitvo_inactivo()