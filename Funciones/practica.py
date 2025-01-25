def recomendacion (gusto):

    if gusto == 'accion':
        return 'termineitor'
    
    elif gusto == 'fantasia':
        return 'el principito'
    
    elif gusto == 'terror':
        return 'cuando un extraño llama'
    
    elif gusto == 'aventura':
        return 'viaje al centro de la tierra'

    elif gusto == 'ciencia ficcion':
        return 'harry potter'
    
peticion = input('¿Que categoria de libros te gustan?')
surgeridos = recomendacion(peticion)
print('te surgerimos:',surgeridos)    
