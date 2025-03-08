def recom(Libro):
    Libro = Libro.lower()
    
    if Libro == "aventura" :
        return "El señor de los anillos "
    
    elif Libro == "fantasia":
        return "Wiggeta"
    
    elif Libro == "terror":
        return "Los ojos de plata"
    
    elif Libro == "accion":
        return  "The amazing Spiderman"
    
    elif Libro =="duspenso":
        return "El exorcista"
    
    return "El libro Troll"

peticion = input("Que tipo de libro te gustan?")    
recomendacion = recom(peticion)
print("Te recomendamos:",recomendacion)
    
    
