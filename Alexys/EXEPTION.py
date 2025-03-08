
def compra(nombre,stock):
    if nombre != '':
        if stock != 0:
          raise ValueError('INGRESE UN NUMERO MAYOR A CERO')
        else: 
           print('compra exitosa')
    else:
        raise ValueError('INGRESE UN NOMBRE')
     
while True:
    try:
      nombre = input('Nombre-Producto:')
      stock = int(input('stock a comprar:'))
      compra(nombre,stock)
      break
    except NameError as e:
       print(e)
    except Exception as e:
       print(e)
          






















'''
pida nombre, numero de stock
nombre no vacio
intento infinito
no acepte num negativos
'''

