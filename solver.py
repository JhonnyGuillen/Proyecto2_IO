# coding=utf-8
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser(
        description = "Soluciona problemas de Mochila 0 Knapsack y de Needleman Wunsch, ya sea de forma de Fuerza Bruta "
                      "o con Programacion Dinamica")
    parser.add_argument("problema", type=int,
                        help="Problema que se quiere resolver: 1 para mochila/knapsack y 2 para Needlman Wunsch")
    parser.add_argument("algoritmo", type=int,
                        help="Algoritmo que se quiere usar: 1 para Fuerza Bruta y 2 para Programacion Dinamica")
    parser.add_argument("archivo", type=str,
                        help="Nombre del archivo a resolver")
    args = parser.parse_args()
    problema = args.problema
    algoritmo = args.algoritmo
    archivo = args.archivo

    if(problema == 1):
        print("Mochila")
        mochila(archivo, algoritmo)
    elif (problema == 2):
        print("Needleman Wunsch Fuerza Bruta")
        alineamiento_secuencia(archivo, algoritmo)
    elif ((problema == 2) & (algoritmo == 2)):
        print("Needleman Wunsch Dinamico")
    else:
        print("Valor erroneo, vuelva a intentar")

class ObjetoMochila:
    def __init__(self, peso, beneficio, cantidad):
        self.peso = peso
        self.beneficio = beneficio
        self.cantidad = cantidad

class ObjetoAlineado:
    def __init__(self, match, fallo, gap):
        self.match = match
        self.fallo = fallo
        self.gap = gap


def mochila(archivoMochila, algoritmo):
    resultado = 0
    archivo = open(archivoMochila, "r")
    linea = archivo.readline()
    pesoMochila = int(linea)
    listaElementos = []
    listaBeneficios = []

    linea = archivo.readline()
    while linea:
        temp = linea.split(",")
        listaElementos.append(ObjetoMochila(int(temp[0]), int(temp[1]), int(temp[2])))
        linea = archivo.readline()

    if(algoritmo == 1):
        print("Mochila Fuerza Bruta")
        resultado = mochilaFuerzaBruta(0, pesoMochila, listaElementos, listaBeneficios)
    elif(algoritmo == 2):
        print("Mochila Dinamica")
        memoria = [[-1 for x in range(pesoMochila+1)] for y in range(len(listaElementos))]
        resultado = mochilaDinamica(0, pesoMochila, memoria, listaElementos,listaBeneficios)

    print("\n" + str(resultado))
    for i in listaBeneficios:
        print(i)

def alineamiento_secuencia(nombreArchivo, algoritmo):
    archivo = open(nombreArchivo, "r")
    linea = archivo.readline()
    print(linea)
    listaPuntajes = linea.split(",")
    hilera1 = archivo.readline()
    hilera2 = archivo.readline()
    print(listaPuntajes[0])
    neddleman_wunsch(hilera1, hilera2, listaPuntajes)

#Complejidad de O(2^n) aproximadamente
def mochilaFuerzaBruta(indice, pesoMochila, listaObjetos, listaBeneficios):
    if(indice >= len(listaObjetos)):
        return 0
    objeto = listaObjetos[indice]
    sumaPesos = objeto.peso * objeto.cantidad
    if(sumaPesos > pesoMochila):
        return mochilaFuerzaBruta(indice + 1, pesoMochila, listaObjetos, listaBeneficios)
    else:
        return max(mochilaFuerzaBruta(indice + 1, pesoMochila, listaObjetos, listaBeneficios),
                   mochilaFuerzaBruta(indice + 1, pesoMochila - sumaPesos, listaObjetos,
                                      listaBeneficios.append(str(indice + 1) + ", " + str(objeto.cantidad))) + (objeto.beneficio * objeto.cantidad))

#Complejidad de O(n^2) aprocimadamente
def mochilaDinamica(indice, pesoMochila, memoria, listaObjetos, listaBeneficios):
    # caso base
    if pesoMochila <= 0 or indice >= len(listaObjetos):
        return 0

    #Si ya se resolvio una mochila similar, devuelve el resultado en memoria
    if memoria[indice][pesoMochila] != -1:
        return memoria[indice][pesoMochila]

    objeto = listaObjetos[indice]
    #Se pregunta si se pueden guardar los objetos en la mochila, si se puede se hace una llamada recursiva para ir guardando los objetos
    ganancia_llevar = 0
    if (objeto.peso * objeto.cantidad) <= pesoMochila:
        ganancia_llevar = (objeto.beneficio * objeto.cantidad) + mochilaDinamica(indice + 1, pesoMochila - (objeto.peso * objeto.cantidad), memoria, listaObjetos, listaBeneficios.append(str(indice + 1) + ", " + str(objeto.cantidad)))

    #Si no se puede guardar el objeto, se deja y procede a guardar el siguiente objeto
    ganancia_no_llevar = mochilaDinamica(indice + 1, pesoMochila, memoria, listaObjetos, listaBeneficios)

    # Se guarda en memoria lo que salga mas benedicioso, llevar el objeto o no
    memoria[indice][pesoMochila] = max(ganancia_llevar, ganancia_no_llevar)

    #Se retorna lo que tenga memoria
    return memoria[indice][pesoMochila]

def neddleman_wunsch(hilera1, hilera2, listaPuntajes):
    matriz_alineamiento = np.zeros((len(hilera1) + 1, len(hilera2) + 1))
    matriz_revision = np.zeros((len(hilera1), len(hilera2)))

    match = listaPuntajes[0]
    fallo = listaPuntajes[1]
    fallo_gap = listaPuntajes[2]

    #Llenar la matriz_revision
    for i in range(len(hilera1)):
        for j in range(len(hilera1)):
            if hilera1[i] == hilera2[j]:
                matriz_revision[i][j] = match
            else:
                matriz_revision[i][j] = fallo

    #Inicializar la matriz
    for i in range(len(hilera1) + 1):
        matriz_alineamiento[i][0] = i * fallo_gap
    for j in range(len(hilera2) + 1):
        matriz_alineamiento[0][j] = j * fallo_gap

    #Llenar la matriz
    for i in range(1, len(hilera1) + 1):
        for j in range(1, len(hilera2) + 1):
            matriz_alineamiento[i][j] = max(matriz_alineamiento[i - 1][j - 1] + matriz_revision[i - 1][j - 1],
                                    matriz_alineamiento[i - 1][j] + fallo_gap,
                                    matriz_alineamiento[i][j - 1] + fallo_gap)


    alineado1 = ""
    alineado2 = ""

    hilera_i = len(hilera1)
    hilera_j = len(hilera2)

    #Revision del puntaje de atras para adelante
    while (hilera_i > 0 and hilera_j > 0):

        if (hilera_i > 0 and hilera_j > 0 and matriz_alineamiento[hilera_i][hilera_j] == matriz_alineamiento[hilera_i - 1][hilera_j - 1] + matriz_revision[hilera_i - 1][hilera_j - 1]):

            alineado1 = hilera1[hilera_i - 1] + alineado1
            alineado2 = hilera2[hilera_j - 1] + alineado2

            hilera_i = hilera_i - 1
            hilera_j = hilera_j - 1

        elif (hilera_i > 0 and matriz_alineamiento[hilera_i][hilera_j] == matriz_alineamiento[hilera_i - 1][hilera_j] + fallo_gap):
            alineado1 = hilera1[hilera_i - 1] + alineado1
            alineado2 = "-" + alineado2

            hilera_i = hilera_i - 1
        else:
            alineado1 = "-" + alineado1
            alineado2 = hilera2[hilera_j - 1] + alineado2

            hilera_j = hilera_j - 1

if __name__ == "__main__":
    main()