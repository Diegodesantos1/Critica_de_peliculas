import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
import math
class Grafica:
    global datos
    datos = pd.read_csv("criticapelicula.csv", sep =";")
    def grafica_inicial(): # Apartado 1
        global lista_votantes
        lista_votantes = list(datos["Cantidad de votantes"])
        eje_x = ["5", "4", "3", "2", "1", "0"]
        eje_y = lista_votantes
        plt.bar(eje_x, eje_y) ; plt.ylabel("Cantidad de votantes") ; plt.xlabel("Nota de las películas") ; plt.title("Opiniones obtenidas para una película")
        plt.show()
        elegir_subejercicio()
    def calculos(): # Apartado 2
        lista_productos = list(datos["Productos"]) ; lista_votantes = list(datos["Cantidad de votantes"]) ; lista_varianza = list(datos["Varianza"])
        suma_producto = 0 ; suma_frecuencia = 0 ; suma_varianza = 0 ; global desviacion_tipica ; global media
        for i in lista_productos:
            suma_producto  += i
        for j in lista_votantes:
            suma_frecuencia += j
        media = suma_producto/suma_frecuencia ; media = round(media, 2)
        for k in lista_varianza:
            suma_varianza += k
        varianza = suma_varianza/suma_frecuencia ;  varianza = round (varianza, 2)
        desviacion_tipica = math.sqrt(varianza) ; desviacion_tipica = round(desviacion_tipica, 2)
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")
        elegir_subejercicio()
    def repartos():
        lim_inferior = (desviacion_tipica - media)
        lim_superior = (desviacion_tipica + media)
        


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n\n¿Qué enunciado quieres ejecutar? \n --> 1: Visualizar la gráfica inicial\n --> 2: Cálculo de media, varianza y desviación típica\n --> 3: Repartos 68% , 95%, 97% \n--> 3: Finalizar el programa\n") ; print(Style.RESET_ALL, end="")
    enunciado=int(input())
    if enunciado == 1:
        Grafica.grafica_inicial()
    elif enunciado == 2:
        Grafica.calculos()
    elif enunciado == 3:
        Grafica.repartos
    elif enunciado == 4:
        exit()
    else:
        elegir_subejercicio()
elegir_subejercicio()