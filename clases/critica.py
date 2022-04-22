import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
import math
class Grafica:
    global datos ; global desviacion_tipica ; global media
    datos = pd.read_csv("criticapelicula.csv", sep =";")
    def grafica_inicial(): # Apartado 1
        global lista_votantes
        lista_votantes = list(datos["Cantidad de votantes"])
        eje_x = ["5", "4", "3", "2", "1", "0"]
        eje_y = lista_votantes
        plt.bar(eje_x, eje_y, color = ["r", "g", "b", "b", "g", "r"]) ; plt.ylabel("Cantidad de votantes") ; plt.xlabel("Nota de las películas") ; plt.title("Opiniones obtenidas para una película")
        plt.show()
        elegir_subejercicio()
    def calculos(): # Apartado 2
        lista_opinion = list(datos["Opinión"]) ; lista_votantes = list(datos["Cantidad de votantes"])
        suma_producto = 0 ; suma_frecuencia = 0 ; suma_varianza = 0
        for i in range (len(lista_opinion)):
            suma_producto += lista_opinion[i] * lista_votantes[i]
        for j in lista_votantes:
            suma_frecuencia += j
        media = round((suma_producto/suma_frecuencia), 2)
        for k in range (len(lista_opinion)):
            suma_varianza = lista_votantes[k]*((lista_opinion[k] - media)**2)
        media = round((suma_producto/suma_frecuencia), 2)
        varianza = round((suma_varianza/suma_frecuencia), 2)
        desviacion_tipica = round((math.sqrt(varianza)), 2)
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")
        elegir_subejercicio()
    def repartos(media, desviacion_tipica):
        lim_inferior = round((desviacion_tipica - media), 2)
        lim_superior = round((desviacion_tipica + media), 2)
        print (f"los limites son {lim_inferior} y {lim_superior}")


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n\n¿Qué enunciado quieres ejecutar? \n --> 1: Visualizar la gráfica inicial\n --> 2: Cálculo de media, varianza y desviación típica\n --> 3: Repartos 68% , 95%, 97%\n --> 4: Finalizar el programa\n") ; print(Style.RESET_ALL, end="")
    enunciado=int(input())
    if enunciado == 1:
        Grafica.grafica_inicial()
    elif enunciado == 2:
        Grafica.calculos()
    elif enunciado == 3:
        Grafica.repartos(2.46,2.57)
    elif enunciado == 4:
        exit()
    else:
        elegir_subejercicio()
elegir_subejercicio()