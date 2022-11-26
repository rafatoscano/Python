from random import *
from violao import *


class cavaquinho(violao):
    __AF1 = 'ré-lá-si-mi'
    __AF2 = 'ré-si-sol-sol'
    __AF3 = 'mi-dó#-lá-lá'
    __AF4 = 'mi-ré-si-sol'

    def __init__(self, Fabricante, Tipo, Cor, Num_Cordas, Tipo_Afinacao):
        self.fabricante = Fabricante
        self.tipo = Tipo
        self.cor = Cor
        self.num_cordas = Num_Cordas
        self.tipoafinacao = Tipo_Afinacao

    def __afinar(self):
        print('Afinando o Cavaquinho...')

    def __tocar(self):
        sequencia = []
        seq1 = []
        seq2 = []
        seq3 = []
        seq4 = []
        for i in range(20):
            sequencia.append(self.notas[randint(0, 6)])
        for j in range(4):
            seq1.append(sequencia[randint(0, 4)])
            seq2.append(sequencia[randint(0, 4)])
            seq3.append(sequencia[randint(0, 4)])
            seq4.append(sequencia[randint(0, 4)])
        print(
            f'\n{super().dedilhar()}\n{seq1}\n{super().dedilhar()}\n{seq2}\n{super().dedilhar()}\n{seq3}\n{super().dedilhar()}\n{seq4}\n')

    @classmethod
    def getTipos(cls):
        return (
            f'\n1 - Tipo de afinação: {cls.__AF1}\n2 - Tipo de afinação: {cls.__AF2}\n3 - Tipo de afinação: {cls.__AF3}\n4 - Tipo de afinação: {cls.__AF4}\n')

    def getFabricante(self):
        return super().__fabricante

    def getTipo(self):
        return super().__tipo

    def getCor(self):
        return super().__cor

    def getNumCordas(self):
        return super().__numcordas

    def getTipoAfinacao(self):
        print('ré-lá-si-mi')

    def __str__(self):
        return (
            f'\nCavaquinho: {super().__fabricante}\nTipo: {super().__tipo}\nCor: {super().__cor}\nNúmero de cordas: {super().__numcordas}\nTipo de afinação: ré-lá-si-mi\n')
