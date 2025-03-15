
def compra(nombre,stock):
            if nombre != '':
                if stock <= 0:
                        raise  ValueError('INGRESE UN NÚMERO VÁLIDO')
                else:
                        print("Compra exitosa")
            else:
                raise ValueError('INGRESE UN NOMBRE')
            
while True:
    try:
        nombre = input('Nombre-producto')
        stock = int(input('Stock a comprar:'))
        compra(nombre,stock)
        break
    except NameError as e:
        print(e)
    except Exception as e:
        print (e) 