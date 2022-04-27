<h1 align="center">Crítica películas</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/Critica_de_peliculas) queda resuelto el ejercicio de serie de datos. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***
## Ejercicio 1

Estas son las opiniones (calificadas de 0 a 5) obtenidas por una película, donde 5 es la mejor nota que puede obtener la película: las famosas 5 estrellas que podemos encontrar en todos los sitios de críticas de cine.

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

Código Avanzado:
```
from collections import Counter
from math import *
import matplotlib.pyplot as plt


class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica


    def calculoMediaAritmetica(self):

        n = self.caracteristica.count()
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones = sumaValoresObservaciones + valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica

    def calculoMediana(self):
        mediana = 0
        caracteristica = self.caracteristica.sort_values()
        caracteristica = caracteristica.reset_index(drop=True)
        n = self.caracteristica.count()
        par = False
        if (n % 2 == 0):
            print("La cantidad de observaciones es par.")
            par = True

        if par:
            rango = (n / 2)
            print("RANGO = "+str(rango))
            rangoPython = rango-1
            valor1 = caracteristica[rangoPython]
            valor2 = caracteristica[rangoPython+1]
            mediana = valor1 +((valor2-valor1)/2)
        else:
            rango = ((n + 1) / 2)
            rangoPython = rango - 1
            mediana = caracteristica[rangoPython]

        return [mediana, rango]

    def calculoModa(self):
        moda = Counter(self.caracteristica)
        return moda

    def calculoVarianzaDesviacionTipica(self):
        n = self.caracteristica.count()
        mediaAritmetica = self.caracteristica.mean()
        varianza = 0
        c3 = 0
        for valorObservacion in self.caracteristica:
            x = valorObservacion
            moy = mediaAritmetica
            c1 = valorObservacion - mediaAritmetica
            c2 = c1 * c1
            c3 = c3 + c2

        varianza = c3 / (n - 1)

        desviacionTipica = sqrt(varianza)

        return ([varianza, desviacionTipica])

    def calculoDelosCuartiles(self,mediana,rangoMediana):
        n = self.caracteristica.count()
        sort_caracteristica = self.caracteristica.sort_values()
        sort_caracteristica = sort_caracteristica.reset_index(drop=True)
        q1 = 0
        q2 = mediana
        q3 = 0

        #Cálculo Q1
        restoDivision = rangoMediana%2
        if (restoDivision != 0):
            q1 = sort_caracteristica[((rangoMediana/2)+1)-1]
        else:
            valorMin = sort_caracteristica[((rangoMediana/2)-1)]
            valorMax = sort_caracteristica[(rangoMediana/2)]
            q1 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2

        # Cálculo Q3
        nbdatos = len(sort_caracteristica)+1
        nbDatosDesdeMediana = nbdatos - rangoMediana
        restoDivision = nbDatosDesdeMediana % 2
        if (restoDivision != 0):
            q3 = sort_caracteristica[(rangoMediana+ceil(nbDatosDesdeMediana/2))-1]
        else:
            valorMinQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))-1]
            valorMaxQ3 = sort_caracteristica[(rangoMediana+(nbDatosDesdeMediana/2))]
            q3 = (valorMin + ((valorMax - valorMin) / 2) + valorMax) / 2


        return ([q1, q2, q3])


    def criterioDeTukey(self, primerCuartil, tercerCuartil):

        valoresAberrantesInferiores = []
        valoresAberrantesSuperiores = []
        caracteristica = self.caracteristica.sort_values()
        intercuartil = tercerCuartil - primerCuartil
        print("Inter-cuartil = "+str(intercuartil))
        limiteInferior = primerCuartil - (1.5 * intercuartil)
        limiteSuperior = tercerCuartil + (1.5 * intercuartil)

        for valorObservacion in caracteristica:
            if valorObservacion < limiteInferior:
                valoresAberrantesInferiores.append(valorObservacion)

            if valorObservacion > limiteSuperior:
                valoresAberrantesSuperiores.append(valorObservacion)

        valoresAberrantes = valoresAberrantesInferiores + valoresAberrantesSuperiores

        return (valoresAberrantes)



    def visualizacion(self,media,mediana,cuartil_1,cuartil_2,cuartil_3):
        media = round(media,2) ; mediana = round(mediana, 2) ; cuartil_1 = round(cuartil_1) ; cuartil_2 = round(cuartil_2) ; cuartil_3 = round(cuartil_3)
        plt.subplot(2, 2, 1)
        plt.hist(self.caracteristica)
        plt.title("Histograma y media")
        plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 2)
        plt.hist(self.caracteristica)
        plt.title("Histograma y mediana")
        plt.axvline(mediana, color='red', linestyle='dashed', linewidth=1,label = str(mediana))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 3)
        plt.hist(self.caracteristica)
        plt.title("Histograma y cuartiles")
        plt.axvline(cuartil_1, color='red', linestyle='dashed', linewidth=1,label = "Q1: "+str(cuartil_1))
        plt.axvline(cuartil_2, color='red', linestyle='dashed', linewidth=1,label = "Q2: "+str(cuartil_2))
        plt.axvline(cuartil_3, color='red', linestyle='dashed', linewidth=1,label = "Q3: "+str(cuartil_3))
        plt.legend(loc='upper right')

        plt.subplot(2, 2, 4)
        plt.boxplot(self.caracteristica)
        plt.title("Diagrama de caja y bigotes")
        plt.show()


    def analisisCaracteristica(self):

        print("-----------------------------------------")
        print("      MEDIDA DE TENDENCIA CENTRAL        ")
        print("-----------------------------------------\n")

        print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
        n = self.caracteristica.count()
        print("Cantidad de observaciones = " + str(n))

        print ("\n-- MIN --")
        valoresOrdenados = self.caracteristica.sort_values()
        valoresOrdenados = valoresOrdenados.reset_index(drop=True)
        print("Valor mínimo: "+str(valoresOrdenados[0]))

        print ("\n-- MAX --")
        valoresOrdenados = self.caracteristica.sort_values()
        valoresOrdenados = valoresOrdenados.reset_index(drop=True)
        print("Valor máximo: " + str(valoresOrdenados[len(valoresOrdenados)-1]))

        # -Media artimética:
        print("\n-- MEDIA --")
        media = self.calculoMediaAritmetica()
        print("Media aritmética calculada = " + str(media))
        print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))

        # -Media aritmética:
        print("\n-- MEDIANA --")
        mediana = self.calculoMediana()
        print("Mediana calculada = " + str(mediana[0]))
        print("> Observaciones: El valor que se encuentra en el punto medio de las observaciones es:" + str(mediana[0]))
        print("El reparto es: " + str(mediana[1]) + " valores en cada lado de la mediana")

        # -Moda
        print("\n-- MODA --")
        moda = self.calculoModa()
        print(moda)
        print("> Observacions: La moda permite determinar los valores observados con más frecuencia")


        print("\n\n-----------------------------------------")
        print("      MEDIDA DE DISPERSION        ")
        print("-----------------------------------------\n")
        print("-- RANGO --")
        print ("Rango de la serie = "+str(valoresOrdenados[len(valoresOrdenados)-1]-valoresOrdenados[0]))
        varianzaDesviacionTipica = self.calculoVarianzaDesviacionTipica()

        print("\n-- VARIANZA --")
        print("Varianza calculada = " + str(varianzaDesviacionTipica[0]))

        print("\n-- DESVIACION TIPICA --")
        print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))
        desviacionTipica = varianzaDesviacionTipica[1]
        print("68 % de los valores de las observaciones se sitúan entre " + str(media - desviacionTipica) + " y " + str(
            media + desviacionTipica))
        print("95 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 2)) + " y " + str(
            media + (desviacionTipica * 2)))
        print("99 % de los valores de las observaciones se sitúan entre " + str(media - (desviacionTipica * 3)) + " y " + str(
            media + (desviacionTipica * 3)))

        print("\n\n-----------------------------------------")
        print("      CUARTILES        ")
        print("-----------------------------------------\n")
        cuartiles = self.calculoDelosCuartiles(mediana[0],mediana[1])
        print("25 % de las observaciones tienen un valor inferior a " + str(cuartiles[0]))
        print("50 % de las observaciones tienen un valor inferior a " + str(cuartiles[1]))
        print("75 % de las observaciones tienen un valor inferior a " + str(cuartiles[2]))


        print("\n\n-----------------------------------------")
        print("      DETECCION VALORES ABERRANTES        ")
        print("-----------------------------------------\n")
        print("> Criterios de Tukey")
        valoresAberrantes = self.criterioDeTukey(cuartiles[0], cuartiles[2])
        print("Cantidad de valores aberrantes: " + str(len(valoresAberrantes)))
        print("Valores:" + str(valoresAberrantes))


        print("\n\n-----------------------------------------")
        print("      VISUALIZACION        ")
        print("-----------------------------------------\n")
        print("Generación de las gráficas...")
        self.visualizacion(media,mediana[0],cuartiles[0],cuartiles[1],cuartiles[2])
```
Su UML:

![image](https://user-images.githubusercontent.com/91721855/165619806-85ced798-ad2b-490a-9056-6cdbf62d575f.png)

En formato [XML](https://github.com/Diegodesantos1/Critica_de_peliculas/blob/main/UML/notas.drawio)
