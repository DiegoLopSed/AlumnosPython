
def primos():
    cont = 0
    numero = int(input("Ingresa un numero: "))
    for i in range(numero):
        
        if numero % i == 0 :
            cont += 1
        else:
            print("No es primo")
primos()