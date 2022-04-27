import pandas as pnd
import Clases_Rubén.JMPEstadisticas as jmp

from Clases import critica
if __name__ == '__main__':
    eleccion = int(input(("¿Qué versión quieres usar? \n 1: Básicas \n 2: Completa\n")))
    if eleccion == 1:
        critica.elegir_subejercicio()
    elif eleccion ==2:
        datos = pnd.read_csv("imdb_sup.csv", header=0 , sep =",")
        lista_notas = list(datos["Rating"])
        observaciones = pnd.DataFrame({'NOTAS': lista_notas})
        #--- ANALISIS DE UNA CARACTERISTICA ---
        stats = jmp.JMPEstadisticas(observaciones['NOTAS'])
        stats.analisisCaracteristica()
