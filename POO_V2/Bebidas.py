from Producto import Producto
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Clase específica para Bebidas
class Bebidas(Producto):
    def info(self):
        print(f"Bebida: {self.nombre} (${self.precio:.2f})")
        print(f"Categoría: {self.categoria}")
        print(f"Stock: {self.stock}")
        print(f"Estado: {self.estado}")
        print(f"Tiempo útil hasta: {self._tiempo_util.strftime('%d-%m-%Y')}")

class Limpieza(Producto):
    def info(self):
        print(f"Producto: {self.nombre}")


# Ejemplo de uso
fecha_actual = datetime.now()
monster = Bebidas(
    id_producto=1,
    nombre="Monster White",
    precio=55.0,
    categoria="Energética",
    stock=50,
    tiempo_util=fecha_actual,
)

# Mostrar información inicial
monster.info()

# Registrar una venta
monster.vender(5)
print("\nDespués de vender 5 unidades:")
monster.info()

# Agregar más stock
monster.agregar_stock(10)
print("\nDespués de agregar 10 unidades al stock:")
monster.info()

# Cambiar precio
monster.subir_precio(15)
print("\nDespués de aumentar el precio un 15%:")
monster.info()

# Obtener detalles
print("\nDetalles completos del producto:")

print(monster.detalles())
