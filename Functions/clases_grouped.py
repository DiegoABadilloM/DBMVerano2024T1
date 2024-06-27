import math
def clases_grouped(datos):
    """
    Función para agrupar datos en clases y calcular límites inferiores, superiores y marcas de clase.
    
    Parámetros:
    - datos (list): lista de números que representan los datos de entrada
    
    Lo que hace:
    - Calcula el rango de los datos (diferencia entre el máximo y el mínimo)
    - Calcula el número de clases utilizando la fórmula de Sturges (1 + 3.3 * log(n)/2)
    - Redondea el número de clases al entero más cercano y resta 1 para evitar clases vacías
    - Calcula el ancho de cada clase dividiendo el rango entre el número de clases
    - Inicializa listas para los límites inferiores, superiores y marcas de clase
    - Itera sobre el número de clases y calcula los límites inferiores, superiores y marcas de clase para cada clase
    - Agrega el límite superior máximo y la marca de clase correspondiente a la última clase
    - Convierte la lista de clases en una lista de números enteros (1, 2, 3,...)
    
    Devuelve:
    - clases (list): lista de números enteros que representan las clases
    - lim_inf (list): lista de números que representan los límites inferiores de cada clase
    - lim_sup (list): lista de números que representan los límites superiores de cada clase
    - mrks (list): lista de números que representan las marcas de clase (promedio de los límites inferior y superior)
    
    Uso:
    - Se utiliza para agrupar datos en clases y calcular límites inferiores, superiores y marcas de clase
    - Se aplica a la lista de datos de entrada para obtener las clases, límites inferiores, superiores y marcas de clase
    """
    
    # Calcula el rango de los datos
    rango = max(datos) - min(datos)
    
    # Calcula el número de clases utilizando la fórmula de Sturges
    # Antiguo: clases = 1 + 3.3 * (math.log(len(datos))/2)
    clases = 1+math.log(len(datos)*3.3)
    
    # Redondea el número de clases al entero más cercano y resta 1 para evitar clases vacías
    clases_redondear = round(clases)-1
    
    # Calcula el ancho de cada clase
    ancho = rango / clases_redondear
    
    # Inicializa listas para los límites inferiores, superiores y marcas de clase
    lim_inf = [min(datos)]
    lim_sup = []
    mrks = []
    
    for i in range(clases_redondear):
        lim_inf.append(round(lim_inf[i] + ancho, 3))
        lim_sup.append(round(lim_inf[i+1], 3))  
        mrks.append(round((lim_inf[i] + lim_sup[i]) / 2, 3))  
    
    
    lim_inf.pop()

    clases_num = list(range(1, clases_redondear + 1))
    
    # Devolvemos las listas redondeadas a tres decimales
    return clases_num, [round(x, 3) for x in lim_inf], [round(x, 3) for x in lim_sup], [round(x, 3) for x in mrks]