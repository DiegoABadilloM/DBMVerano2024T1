import math
def clases_grouped_six(datos):

    rango = max(datos) - min(datos)
    
    clases = 1+math.log(6)*3.3
    
    clases_redondear = round(clases)-1
    
    ancho = rango / clases_redondear
    
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
