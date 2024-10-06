"""
https://www.kaggle.com/datasets/shivamb/netflix-shows

#Link de archivo de peliculas de nexflix
"""
import pandas as pd
import matplotlib.pyplot as plt

# Llamamos el CSV para trabajar (el archivo proporcionado tiene información de shows y películas)
data = pd.read_csv("netflix.csv")  # Actualiza con el nombre correcto de tu archivo

# Verificamos si los datos se cargaron correctamente
print(data[['title', 'type', 'country']])

# Agrupamos los datos por tipo (películas o series) y contamos cuántos hay de cada tipo
type_counts = data['type'].value_counts()

# Graficamos los datos con un gráfico de líneas
plt.figure(figsize=(8, 6))
plt.plot(type_counts.index, type_counts, marker='o', color='skyblue', linestyle='-')

plt.xlabel('Tipo')
plt.ylabel('Cantidad')
plt.title('Distribución de películas y series')

# Mostramos el gráfico
plt.show()
