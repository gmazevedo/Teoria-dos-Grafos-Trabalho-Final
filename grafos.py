class Grafo:
    def __init__(self):
        self.destinos = []
        self.raiz = 1
        self.tamanho = 0
        self.matriz = []
        self.pesos = []


    def printaGrafo(self):
        print self.tamanho
        print self.destinos
        print self.pesos
        print self.matriz


def leGrafo(grafo):
    arquivo = open('entrada.txt','r')

    linhas = arquivo.read()
    linhas = linhas.splitlines()
    grafo.tamanho = linhas[0]
    grafo.tamanho = int(grafo.tamanho)
    grafo.destinos = linhas[1].split(' ')
    grafo.pesos = linhas[2].split(' ')

    arquivo.close()

    j = 3

    for i in range(int(grafo.tamanho)):
        linha = linhas[j].split(' ')
        grafo.matriz.append(linha)
        j += 1

    return grafo

def buscaAresta(origem,destino,matriz):
    origem -= 1
    destino -= 1

    return matriz[origem][destino]

def descobreArestas(grafo):
    matrizPred = []
    for i in range(grafo.tamanho):
        linha=[]

    #origem = 1
    #origem -= 1

    for linhas in range(grafo.tamanho):
        print
        print "Descobrindo vizinhos do vertice " + str(linhas + 1)
        print
        for i in range(grafo.tamanho):
            if grafo.matriz[linhas][i] != '-1':
                print "Vertice "+str(i+1)+" descoberto"







