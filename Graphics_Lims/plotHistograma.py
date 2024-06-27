import matplotlib.pyplot as plt
import numpy as np

def plot_grafHist(frecuencias_relativas, marcas_clase, marcas_texto):
    """
    Función para dibujar un histograma que muestra la distribución de frecuencias relativas por marca de clase.
    
    Parámetros:
    - frecuencias_relativas (list): lista de números que representan la frecuencia relativa de cada marca de clase
    - marcas_clase (list): lista de strings que representan las marcas de clase
    - marcas_texto (list): lista de strings que representan los nombres de cada marca de clase
    
    Lo que hace:
    - Dibuja un histograma que muestra la distribución de frecuencias relativas por marca de clase
    - Muestra la frecuencia relativa de cada marca de clase en la gráfica
    - Ajusta el límite superior del eje y para que sea un 10% más alto que el valor máximo de frecuencia relativa
    """
    
    # Crear una figura con un tamaño específico
    plt.figure(figsize=(12, 6))
    
    # Crear un arreglo de indices para las columnas
    x = np.arange(len(marcas_clase))
    
    # Ancho de las columnas
    width = 0.5
    
    # Dibujar las columnas del histograma
    plt.bar(x, frecuencias_relativas, width, 
             # Color del borde de cada columna
             edgecolor="k", 
             # Colores de cada columna
             color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"])
    
    # Etiquetas para el eje x
    plt.xticks(x, marcas_clase, fontsize=15, rotation=45) 
    plt.ylabel("Frecuencia relativa", fontsize=20)
    plt.title("Histograma", fontsize=25)
    
    # Ajustar el límite superior del eje y
    plt.ylim(0, max(frecuencias_relativas) * 1.1)
    
    # Agregar una grilla
    plt.grid()
    
    # Mostrar el gráfico
    plt.show()
    