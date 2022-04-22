<h1 align="center">Serie de notas</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/Serie_de_Notas) queda resuelto el ejercicio de serie de datos. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Ejercicio 1

Vamos a utilizar un caso práctico que se usa muchas veces en la presentación de las nociones básicas de estadísticas: la descripción y el análisis de una serie de notas que ha obtenido un estudiante. Este caso práctico es sencillo y todo el mundo se siente implicado porque se basa en nuestra experiencia. Además, nos permitirá entender las nociones necesarias para la comprensión de datos que también son aplicables a los casos más complejos que vamos a tratar en los capítulos siguientes.

Este es el contexto: actualmente está en formación para convertirse en experto en inteligencia artificial y acaban de darle sus notas trimestrales, que puede ver a continuación (se trata de una puntuación sobre 20): [3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16]

Como puede comprobar, esta pequeña serie estadística contiene muchas notas distintas. Primero vamos a proceder a la deducción de una tendencia central, es decir, intentar determinar un valor alrededor del que se concentra el conjunto de las notas. Luego estudiaremos su dispersión y al final buscaremos la existencia de datos aberrantes, es decir, no representativos del conjunto de las notas. Todos recordamos un examen donde no habíamos repasado los conceptos principales y obtuvimos una nota no representativa de las notas que habíamos obtenido durante el año.

Debe realizar este tipo de análisis en cualquier serie de observaciones que tendrá que utilizar en el ámbito de los proyectos de Machine Learning. En efecto, hacer mediciones de tendencia y de dispersión de sus datos le permitirá comprender su significado, su papel y su utilidad en la predicción que se ha de efectuar. Identificar los datos aberrantes le permitirá excluir datos no representativos que podrían alterar el aprendizaje.


El código empleado para resolverlo es el siguiente: 

```python
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style
import math
class Grafica:
    global datos,desviacion_tipica, media
    def __init__(self, lista_votantes, lista_opinion, suma_producto, suma_frecuencia, suma_varianza, media, varianza, desviacion_tipica, l_inferior, suma_frecuencia_anterior, frecuencia_intervalo, amplitud):
        self.lista_votantes = lista_votantes ; self.lista_opinion = lista_opinion ;self.suma_producto = suma_producto
        self.suma_frecuencia = suma_frecuencia ; self.suma_varianza = suma_varianza ; self.media = media ; self.varianza = varianza
        self.desviacion_tipica = desviacion_tipica ; self.l_inferior = l_inferior ; self.suma_frecuencia_anterior = suma_frecuencia_anterior
        self.frecuencia_intervalo = frecuencia_intervalo ; self.amplitud = amplitud
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
        global lista_votantes
        lista_opinion = list(datos["Opinión"]) ; lista_votantes = list(datos["Cantidad de votantes"])
        suma_producto = 0 ; suma_frecuencia = 0 ; suma_varianza = 0
        for i in range (len(lista_opinion)):
            suma_producto += lista_opinion[i] * lista_votantes[i]
        for j in lista_votantes:
            suma_frecuencia += j
        media = round((suma_producto/suma_frecuencia), 2)
        for k in range (len(lista_opinion)):
            suma_varianza += lista_votantes[k]*((lista_opinion[k] - media)**2)
        media = round((suma_producto/suma_frecuencia), 2)
        varianza = round((suma_varianza/suma_frecuencia), 2)
        desviacion_tipica = round((math.sqrt(varianza)), 2)
        print(f"\n La media es {media}, la varianza {varianza} y la desviación típica {desviacion_tipica} \n ")
        elegir_subejercicio()
    def percentil_68():
        lista_votantes = list(datos["Cantidad de votantes"]) ; suma_frecuencia = 0
        for j in lista_votantes:
            suma_frecuencia += j
        intervalo = (68 * suma_frecuencia)/100
        print(f"El 68% de los datos son {intervalo}")
        l_inferior = 1 ; suma_frecuencia_anterior = 136 ; frecuencia_intervalo = 133 ; amplitud = 1  #Datos sacados de la tabla
        percentil_68 = round(l_inferior + (((intervalo - suma_frecuencia_anterior)/frecuencia_intervalo)* amplitud), 3)
        print(f"El percentil 68% es {percentil_68}")
    def percentil_95():
        lista_votantes = list(datos["Cantidad de votantes"]) ; suma_frecuencia = 0
        for j in lista_votantes:
            suma_frecuencia += j
        intervalo = (95 * suma_frecuencia)/100
        print(f"\nEl 95% de los datos son {intervalo}")
        l_inferior = 3 ; suma_frecuencia_anterior = 414 ; frecuencia_intervalo = 99 ; amplitud = 1  #Datos sacados de la tabla
        percentil_95 = round(l_inferior + (((intervalo - suma_frecuencia_anterior)/frecuencia_intervalo)* amplitud), 3)
        print(f"El percentil 68% es {percentil_95}")
    def percentil_97():
        lista_votantes = list(datos["Cantidad de votantes"]) ; suma_frecuencia = 0
        for j in lista_votantes:
            suma_frecuencia += j
        intervalo = (97 * suma_frecuencia)/100
        print(f"\nEl 97% de los datos son {intervalo}")
        l_inferior = 4 ; suma_frecuencia_anterior = 513 ; frecuencia_intervalo = 40 ; amplitud = 1  #Datos sacados de la tabla
        percentil_98 = round(l_inferior + (((intervalo - suma_frecuencia_anterior)/frecuencia_intervalo)* amplitud), 3)
        print(f"El percentil 68% es {percentil_98}")
        elegir_subejercicio()


def elegir_subejercicio():
    print (Fore.LIGHTMAGENTA_EX + "\n\n¿Qué enunciado quieres ejecutar? \n --> 1: Visualizar la gráfica inicial\n --> 2: Cálculo de media, varianza y desviación típica\n --> 3: Repartos 68% , 95%, 97%\n --> 4: Finalizar el programa\n") ; print(Style.RESET_ALL, end="")
    enunciado=int(input())
    if enunciado == 1:
        Grafica.grafica_inicial()
    elif enunciado == 2:
        Grafica.calculos()
    elif enunciado == 3:
        Grafica.percentil_68()
        Grafica.percentil_95()
        Grafica.percentil_97()
    elif enunciado == 4:
        exit()
    else:
        elegir_subejercicio()
```

Su UML:

En formato [XML]()
