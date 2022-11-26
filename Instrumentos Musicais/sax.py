from random import *
from instrumento import *


class sax(instrumento):
    def __init__(self, Fabricante, Tipo, Cor, Modelo):
        self.fabricante = Fabricante
        self.tipo = Tipo
        self.cor = Cor
        self.modelo = Modelo

    def afinar(self):
        print('Afinando o Sax...')

    def soprar(self):
        print('Soprando...')

    def tocar(self):
        sequencia = []
        seq1 = []
        seq2 = []
        seq3 = []
        seq4 = []
        for i in range(20):
            sequencia.append([randint(0, 6)])
        for j in range(3):
            print ("Antes J", j, seq1, seq2, seq3, seq4)
            aux = input("Enter")

            seq1.append(sequencia[randint(0, 3)])
            seq2.append(sequencia[randint(0, 3)])
            seq3.append(sequencia[randint(0, 3)])
            seq4.append(sequencia[randint(0, 3)])
            print ("J", j, seq1, seq2, seq3, seq4)
            aux = input("Enter")

        print(f'\n{self.soprar()}\n{seq1}\n{self.soprar()}\n{seq2}\n{self.soprar()}\n{seq3}\n{self.soprar()}\n{seq4}\n')
        

    def limpar(self):
        print('Limpando o Sax...')
        print('Sax limpado com sucesso...')

    
    def getFabricante(self):
        return super().fabricante

    def getTipo(self):
        return super().tipo

    def getCor(self):
        return super().cor

    def getModelo(self):
        return self.modelo

    def __str__(self):
        return (
            f'\nSax: {super().__fabricante}\nTipo: {super().__tipo}\nCor: {super().__cor}\nModelo: {self.__modelo}\n')
