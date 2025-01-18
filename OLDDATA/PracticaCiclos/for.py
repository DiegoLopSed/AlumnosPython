"""
En las prácticas de hoy exploraremos el ciclo o bucle 'for'.
A continuación, se explica su funcionamiento y sintaxis con ejemplos.
"""

#* La variable `i` es el iterador.
#* Es decir, es la que lleva el control del incremento del ciclo.
for i in range(10):  #! El valor 10 en range() indica el número de repeticiones del ciclo.
    print(i)
    
#* En resumen, el ciclo `for` permite repetir una instrucción un número específico de veces.

#? El ciclo `for` puede declararse con diferentes sintaxis según los parámetros usados en range():

# Ejemplo con un rango inicial y final
for i in range(5, 10):  #! Empieza desde 5 y termina en 9 (el límite superior no se incluye).
    print(i)

# Ejemplo con un rango inicial, final y un paso específico
for i in range(2, 20, 2):  #! Empieza desde 2, incrementa de 2 en 2 y termina antes de 20.
    print(i)

#? Ejecuta los ejemplos y comenta tus conclusiones sobre cómo funciona cada caso.
