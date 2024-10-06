"""
https://www.kaggle.com/datasets/surajjha101/top-youtube-channels-data

Tseries fue el canal que podimos observar en este grafico 

"""
import pandas as pd
import matplotlib.pyplot as plt

# Llamamos el CSV para trabajar
cherrybons = pd.read_csv("yotubers.csv")

# Eliminamos las comas en la columna 'subscribers' y  los convertimos en números
cherrybons['subscribers'] = cherrybons['subscribers'].str.replace(',', '').astype(float)

# Verificamos si  los datos estan procesados
print(cherrybons[['Youtuber', 'subscribers']])

# Ordenamos por números a los  suscriptores
cherrybons_ord = cherrybons.sort_values(by='subscribers', ascending=False).head(10)

# Graficamos los datos con un gráfico circular (de pastel)
plt.figure(figsize=(8, 8))
plt.pie(cherrybons_ord['subscribers'], labels=cherrybons_ord['Youtuber'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

plt.title('Top 10 Youtubers por número de suscriptores')

# Aseguramos que el gráfico sea circular
plt.axis('equal')

plt.show()