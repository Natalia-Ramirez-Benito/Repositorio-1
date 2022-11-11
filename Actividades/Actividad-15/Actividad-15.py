import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("casasboston.csv")
#Renombramos para mostrar los datos en nuestro idioma
df = datos.rename(columns={
    "TOWN": "CIUDAD",
    "CRIM": "INDICE_CRIMEN",
    "INDUS": "PCT_ZONA_INDUSTRIAL",
    "CHAS": "RIO_CHARLES",
    "RM": "N_HABITACIONES_MEDIO",
    "MEDV": "VALOR_MEDIANO",
    "LSTAT": "PCT_CLASE_BAJA"
})

#Historiograma: para ver la distribución de la cantidad media de habitaciones en el estudio realizado.
df.N_HABITACIONES_MEDIO.plot.hist()
plt.show()

#Gráfico de dispersión: para representar la relación entre dos variables; en este caso, la relación entre índice de crimen y el valor mediano de las casas.
df.plot.scatter(x="INDICE_CRIMEN", y="VALOR_MEDIANO", alpha=0.2)
plt.show()

#Gráfico de barras: para observar el valor medio de cada ciudad.
valor_por_ciudad = df.groupby("CIUDAD")["VALOR_MEDIANO"].mean()
valor_por_ciudad.head(10).plot.barh()
plt.show()

#Diagrama de cajas:  ver los valores atípicos de índice de crimen en los diferentes cuantiles de valor mediano.
df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
df.boxplot(column="INDICE_CRIMEN", by="VALOR_CUANTILES",
	figsize=(8,6))
plt.show()

#Gráfico circular:  para mostrar la relación porcentual entre las partes con relación a su conjunto.
df.RIO_CHARLES.value_counts().plot.pie()
plt.show()