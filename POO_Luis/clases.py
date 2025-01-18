from Abstract import Producto

class papas(Producto):
    def info(self):
        print(f"papa: {self.nombre} (${self.precio:.2f})")
        print(f"Categoria: {self.categoria}")
        print(f"Stock: {self.stock}") 
        print(f"Estado: {self.estado}")


chips = papas(1,"chips fuego",15,"frituras",15)

chips.info

