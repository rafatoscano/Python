from random import *
from instrumento import *


class violao(instrumento):
    def __init__(self, Fabricante, Tipo, Cor, Num_Cordas):
        self.fabricante = Fabricante
        self.tipo = Tipo
        self.cor = Cor
        self.numcordas = Num_Cordas

    def afinar(self):
        print('Afinando o Violao...')

    def dedilhar(self):
        print('Dedilhando...')

    def tocar(self):
        sequencia = []
        seq1 = []
        seq2 = []
        seq3 = []
        seq4 = []
        for i in range(20):
            sequencia.append([randint(0, 6)])
        for j in range(3):
            seq1.append(sequencia[randint(0, 3)])
            seq2.append(sequencia[randint(0, 3)])
            seq3.append(sequencia[randint(0, 3)])
            seq4.append(sequencia[randint(0, 3)])
        print(f'\n{self.dedilhar()}\n{seq1}\n{self.dedilhar()}\n{seq2}\n{self.dedilhar()}\n{seq3}\n{self.dedilhar()}\n{seq4}\n')

    def trocarCorda(self):
        print('Cordas trocadas!')

    
    def getFabricante(self):
        return self.fabricante

    def getTipo(self):
        return self.tipo

    def getCor(self):
        return self.cor

    def getNumCordas(self):
        return self.numcordas

    def __str__(self):
        return (
            f'\nViolão: {self.fabricante}\nTipo: {self.tipo}\nCor: {self.cor}\nNúmero de cordas: {self.numcordas}\n')
