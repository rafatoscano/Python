from abc import ABC,abstractmethod
from random import *

class instrumento (ABC):

  def __init__ (self, Fabricante, Tipo, Cor):
    self.fabricante = Fabricante
    self.tipo = Tipo
    self.cor = Cor
    self.notas = ['dó', 'ré', 'mi', 'fá', 'sol', 'lá', 'si']

  @abstractmethod
  def afinar (self):
    pass
  @abstractmethod
  def tocar (self):
    pass
