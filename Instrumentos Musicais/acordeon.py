from random import *
from instrumento import *


class acordeon(instrumento):
    def __init__(self, Fabricante, Tipo, Cor, Modelo):
        self.fabricante = Fabricante
        self.tipo = Tipo
        self.cor = Cor
        self.modelo = Modelo

    def afinar(self):
        print('Afinando o acordeon...')

    def abre(self):
      print('Abrindo...')

    def puxa(self):
      print('Puxando...')

    def fecha(self):
      print('Fechando...')

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

        print(f'\n{self.abre()}\n{seq1}\n{self.puxa()}\n{seq2}\n{self.abre()}\n{seq3}\n{self.fecha()}\n{seq4}\n')
        

    def limpar(self):
        print('Limpando o acordeon...')
        print('Acordeon limpado com sucesso...')

    
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
            f'\nAcordeon: {super().__fabricante}\nTipo: {super().__tipo}\nCor: {super().__cor}\nModelo: {self.__modelo}\n')
