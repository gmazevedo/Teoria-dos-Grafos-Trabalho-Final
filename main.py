from grafos import *


def main():
    grafo = Grafo()

    grafo = leGrafo(grafo)

    grafo.printaGrafo()

    print
    descobreArestas(grafo)

   # for destino in grafo.destinos:
    #    print buscaAresta(grafo.raiz,int(destino),grafo.matriz)



main()