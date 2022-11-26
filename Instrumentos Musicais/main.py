from instrumento import *
from musico import *
from sax import *
from violao import *
from cavaquinho import *
from acordeon import *

def main():
  print('\nDigite 1 para adicionar um músico\n')
  op = int(input(': '))
  if op == 1:
    nome = input('Digite o nome do musico: ')
    nacionalidade = input('Digite a nacionalidade: ')
    k = musico(nome, nacionalidade)
    print('\nDigite 1 - Violao\nDigite 2 - Sax\nDigite 3 - Cavaquinho\nDigite 4 - Acordeon\n')
    instrumento = int(input('Digite um instrumento: '))
    if instrumento == 1:
      fabricante = input("Nome do fabricante: ")
      tipo = input ("Tipo do instrumento: ")
      cor = input ("Cor do instrumento: ")
      numcordas = input ("Número de cordas: ")
      a = violao(fabricante, tipo, cor, numcordas)
    if instrumento == 2:
      fabricante = input("Nome do fabricante: ")
      tipo = input ("Tipo do instrumento: ")
      cor = input ("Cor do instrumento: ")
      modelo = input ("Modelo do Sax: ")
      b = sax(fabricante, tipo, cor, modelo)
    if instrumento == 3:
      fabricante = input("Nome do fabricante: ")
      tipo = input ("Tipo do instrumento: ")
      cor = input ("Cor do instrumento: ")
      nun_cordas = input ("Numero de cordas: ")
      tipoafinacao = input ("Tipo de afinação: ")
      c = cavaquinho(fabricante, tipo, cor, nun_cordas, tipoafinacao)
    if instrumento == 4:
      fabricante = input("Nome do fabricante: ")
      tipo = input ("Tipo do instrumento: ")
      cor = input ("Cor do instrumento: ")
      modelo = input ("Modelo do Acordeon: ")
      d = acordeon(fabricante, tipo, cor, modelo)
    print('\nDigite 1 Para iniciar demonstração\nDigite 2 Para adicionar o Instrumento escolhido\nDigite 3 para exibir Instrumento\n')
    usar = int(input(': '))
    if usar == 1 and instrumento == 1:
      k.iniciarDemonstracao()
      a.tocar()
    if usar == 1 and instrumento == 2:
      k.iniciarDemonstracao()
      b.tocar()
    if usar == 1 and instrumento == 3:
      k.iniciarDemonstracao()
      c.tocar()
    #else:
    if usar == 1 and instrumento == 4:
      k.iniciarDemonstracao()
      d.tocar()
if __name__ == '__main__':
  main()
