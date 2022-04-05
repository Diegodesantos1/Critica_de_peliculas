import pandas as pd
import matplotlib.pyplot as plt

class grafica:
    datos = pd.read_csv("criticapelicula.csv", sep =";")
    lista_votantes = list(datos["Cantidad de votantes"])
    eje_x = ["5", "4", "3", "2", "1", "0"]
    eje_y = lista_votantes
    plt.bar(eje_x, eje_y) ; plt.ylabel("Cantidad de votantes") ; plt.xlabel("Nota de las películas") ; plt.title("Opiniones obtenidas para una película")
    plt.show()