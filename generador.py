# coding=utf-8

import argparse
import random

archivoSalida = ''
listaParametros = []

def crearArchivoSalida(nombreArchivo):
    global archivoSalida
    archivoSalida = nombreArchivo + ".txt"
    archivo = open(archivoSalida, 'w+')
    print("archivo creado")
    archivo.close()

def generador():
    parser = argparse.ArgumentParser(description="Generador de problemas de Mochila 0 Knapsack y de Needleman Wunsch")
    parser.add_argument("problema", type=int,
                        help="Problema que se quiere resolver: 1 para mochila/knapsack y 2 para Needlman Wunsch")
    parser.add_argument("archivo", type=str,
                        help="Nombre del archivo que se va a crear")
    parser.add_argument("peso_largo1", type=int,
                        help="Si es mochila el problema, corresponde al peso que soporta la mochila; Si es needleman wunsch el problema, corresponde al largo de la primera hilera")
    parser.add_argument("elementos_largo2", type=int,
                        help="Si es mochila el programa, corresponde la cantidad de elementos que se quieren agregar a la mochila; Si es needleman wunsch el problema, corresponde al largo de la hilera 2")
    parser.add_argument("minPeso", type=int, nargs="?",
                        default=None, help="Peso minimo de los elementos de la mochila")
    parser.add_argument("maxPeso", type=int, nargs="?",
                        default=None, help="Peso maximo de los elementos de la mochila")
    parser.add_argument("minBeneficio", type=int, nargs="?",
                        default=None, help="Beneficio minimo de cada elemento")
    parser.add_argument("maxBeneficio", type=int, nargs="?",
                        default=None, help="Beneficio maximo de cada elemento")
    parser.add_argument("minCantidad", type=int, nargs="?",
                        default=None, help="Cantidad minima de elementos")
    parser.add_argument("maxCantidad", type=int, nargs="?",
                        default=None, help="Cantidad maximo de elementos")
    args = parser.parse_args()
    nombreArchivo = args.archivo
    crearArchivoSalida(nombreArchivo)
    if(args.problema == 1): #Si es de mochila
        print("Mochila")
        generadorMochila(args.peso_largo1, args.elementos_largo2, args.minPeso, args.maxPeso, args.minBeneficio, args.maxBeneficio,
                         args.minCantidad, args.maxCantidad)
    elif(args.problema == 2): #Si es de needleman wunsch
        print("Needleman Wunsch")
        generadorNeedlemanWunsch(args.peso_largo1, args.elementos_largo2)

#W = peso soportado por la mochila
#N = numero de elementos
def generadorMochila(W,N, minPeso, maxPeso, minBeneficio,maxBeneficio, minCantidad, maxCantidad):
    archivo = open(archivoSalida, "w")
    archivo.write(str(W) + "\n")
    for contadorLineas in range(N):
        peso = random.randint(minPeso, maxPeso)
        beneficio = random.randint(minBeneficio, maxBeneficio)
        cantidad = random.randint(minCantidad, maxCantidad)
        archivo.write(str(peso)+","+str(beneficio)+","+str(cantidad)+"\n")
    archivo.close()
    print("archivo creado")

def generadorNeedlemanWunsch(largo1, largo2):
    letras = "ATCG"
    linea1 = ""
    linea2 = ""
    for contLinea1 in range(largo1):
        linea1 = linea1 + random.choice(letras)
    for contLinea2 in range(largo2):
        linea2 = linea2 + random.choice(letras)
    archivo = open(archivoSalida, "w")
    archivo.write("1,-1,-2" + "\n" + linea1 + "\n" + linea2 + "\n")
    archivo.close()
    print("archivo creado")

def main():
    generador()

if __name__ == "__main__":
    main()