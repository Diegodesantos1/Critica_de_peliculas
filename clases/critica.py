import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
class Grafica:
    global datos
    datos = pd.read_csv("criticapelicula.csv", sep =";")
    def grafica_inicial():
        global lista_votantes
        lista_votantes = list(datos["Cantidad de votantes"])
        eje_x = ["5", "4", "3", "2", "1", "0"]
        eje_y = lista_votantes
        plt.bar(eje_x, eje_y) ; plt.ylabel("Cantidad de votantes") ; plt.xlabel("Nota de las películas") ; plt.title("Opiniones obtenidas para una película")
        plt.show()
    def calculos():
        lista_productos = list(datos["Productos"]) ; suma_producto = 0 ; suma_frecuencia = 0 ; lista_votantes = list(datos["Cantidad de votantes"])
        for i in lista_productos:
            suma_producto  += i
        for j in lista_votantes:
            suma_frecuencia += j
        media = suma_producto/suma_frecuencia


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n\n¿Qué enunciado quieres ejecutar? \n --> 1: Visualizar la gráfica inicial\n --> 2: Cálculo de media,varianza y desviación típica\n --> 3: Finalizar el programa\n") ; print(Style.RESET_ALL, end="")
    enunciado=int(input())
    if enunciado == 1:
        Grafica.grafica_inicial()
    elif enunciado == 2:
        Grafica.calculos()
    elif enunciado == 3:
        exit()
    else:
        elegir_subejercicio()
elegir_subejercicio()