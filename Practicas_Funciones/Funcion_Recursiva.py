def calcular_salario(horas):
    """
    Calcula el salario de forma recursiva.
    :param horas: Número de horas trabajadas (int).
    :return: Salario total (int).
    """
    # Caso base: si no hay horas de trabajo, el salario es 0.
    if horas == 0:
        return 0
    
    # Caso recursivo: suma el pago por una hora y llama a la función con una hora menos.
    return 1200 + calcular_salario(horas - 1)

# Ejemplo de uso
horas_trabajadas = 5
salario = calcular_salario(horas_trabajadas)
print(f"El salario por trabajar {horas_trabajadas} horas es: ${salario}")
