def recom(gusto):
    gusto = gusto.lower()
    if gusto == 'aventura':
        return 'gran turismo'
    elif gusto == 'terror':
        return'fainats san fredi'
    elif gusto == 'aventura':
        return'la gran aventura lego'
    elif gusto == 'comedia':
        return'Una pareja de idiotas'
    elif gusto == 'acción':
        return 'avengers era de ulton'


peticion = input('Que gustos literarios tines?')
recomendacion = recom(peticion)
print('Te recomendamos.',recomendacion)

