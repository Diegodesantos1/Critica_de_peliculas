<h1 align="center">Serie de notas</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/Serie_de_Notas) queda resuelto el ejercicio de serie de datos. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Ejercicio 1
Para conocer mejor la distribución gaussiana, vamos a dejar a un lado las notas obtenidas en el examen y vamos a concentrarnos en las críticas de películas.

Estas son las opiniones (calificadas de 0 a 5) obtenidas por una película, donde 5 es la mejor nota que puede obtener la película: las famosas 5 estrellas que podemos encontrar en todos los sitios de críticas de cine.

Curva de Gauss

Ante este tipo de gráfico, podemos afirmar que la serie de observaciones sigue una ley matemática llamada ley normal o ley de Gauss (en honor a Karl Friederich Gauss (1777-1855)).

En estadística y en probabilidad, la ley normal permite representar muchos fenómenos aleatorios naturales. Cuando una serie de observaciones obedece a la ley normal, se puede afirmar:

El 50 % de las observaciones están por encima de la media.

El 50 % de las observaciones están por debajo de la media.

El 68 % de las observaciones están comprendidas en el intervalo que va desde la media - la desviación típica hasta la media + la desviación típica.

El 95 % de las observaciones están comprendidas en el intervalo que va desde la media - 2* la desviación típica hasta la media + 2* la desviación típica.

El 99,7 % de las observaciones están comprendidas en el intervalo que va desde la media - 3* la desviación típica hasta la media + 3* la desviación típica.

Ahora vamos a hacer algunos cálculos que al mismo tiempo nos permitirán ver cómo utilizar la idea de frecuencia en los cálculos de media y de desviación típica.

Las opiniones corresponden a nuestros valores observados denominados Xi, y la cantidad de votantes se equipara a la cantidad de veces en que el valor observado ha sido elegido por los espectadores. Entonces hablamos de frecuencia de elección, que se denomina Ni.

A fin de calcular la media de esta serie de observaciones, para cada observación hay que realizar el producto de las opiniones por la cantidad de votantes:

Lo que da un valor de 1,35 para la desviación típica.

Ahora le toca a usted examinar el reparto de las observaciones en función de las desviaciones entre la media y la desviación típica que permite definir los 68 %, 95 % y 97 % de repartos.

Como ejemplo, podemos comprobar que el 68 % de las observaciones están comprendidas en el intervalo [1,3]. Los límites del intervalo se han determinado mediante la resta de la desviación típica a la media para el límite inferior y la suma de la desviación típica a la media para el límite superior. 

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
