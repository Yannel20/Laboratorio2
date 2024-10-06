""""
https://www.kaggle.com/datasets/asmonline/spotify-song-performance-dataset

Analisis de los resultados del grafico

Este gráfico proporciona una visión clara de las canciones más populares en Spotify en 2024, 
indicando qué música ha sido más escuchada por los usuarios. Permite identificar artistas que 
dominan las listas de reproducción y tendencias musicales de este año, reflejando los gustos 
predominantes de la audiencia de Spotify.
"""

import matplotlib.pyplot as plt
import pandas as pd

#Llamar el CSV a trabajar y leemos el dataseet
coconut = pd.read_csv("spotify.csv")

# Agrupamos los datos por 'Songs & Artist' y calcular el promedio de 'Streams'
data = coconut.groupby("Songs & Artist")["Streams"].mean().sort_values()

# Define una lista de colores para las barras
colores = ["green", "red", "orange", "purple", "blue", "yellow", "pink", "cyan", "magenta", "brown"]

# Seleccionar las 10 canciones más escuchadas
top10 = data.nlargest(10)

# Crea una figura para el gráfico de barras
plt.figure(figsize=(10, 6))

# Graficar las canciones más escuchadas con diferentes colores para cada barra
plt.bar(top10.index, top10.values, color=colores[:len(top10)])  # se asignan los colores para las barras

# Añadir etiquetas a los ejes y el título del gráfico
plt.ylabel('Total de numeros de streams')
plt.xlabel('Canciones y artistas')
plt.title('Canciones mas escuchadas en Spotify 2024')

# Algunos nombres de las canciones son largos asi que toca rotar
plt.xticks(rotation=90)

# Ajusta el diseño para evitar recortes
plt.tight_layout()

# Muestra el grafico
plt.show()
