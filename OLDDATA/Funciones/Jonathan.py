"""
Crea una función que reciba como parametro una temperatura en C° y que asigne 
la sensasión termica
Helada = (-3,6)
Fria = (7-11)
Templada = (12-20)
Calida = (21-28)
Sofocante = (29-32)
"""


def  temperatura_r(temperatura):
    
    if temperatura <=6:
        print('Helado')

    elif  temperatura >=7 and temperatura <= 11:
        print('Frio')

    elif temperatura >=12 and temperatura <= 20:
        print('Templado')

    elif temperatura >= 21 and temperatura <=28:
        print('Calido')

    elif temperatura >=29:
        print('Sofocante')

temperatura_r(2)
temperatura_r(10)
temperatura_r(16)
temperatura_r(21)
temperatura_r(35)
