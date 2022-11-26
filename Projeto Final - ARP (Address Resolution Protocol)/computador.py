from dispositivo import Dispositivo
from tabela_hash import TabelaHash

class Computador(Dispositivo):
    def __init__(self, ip: str, mac: str, nome: str):
        super().__init__(ip, mac)
        self.__nome = nome
        self.__tabelaArp = TabelaHash()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    def Validando_IP(self, ip: str):
        return super().Validando_IP(ip)

    def Validando_MAC(self, mac: str):
        return super().Validando_MAC(mac)

    def Tabela_Arp(self, ip: str, mac: str):
        if self.Validando_IP(ip) and self.Validando_MAC(mac):
            self.__tabelaArp[ip] = mac
        else:
            print("Endereço IP ou MAC inválido!")

    def Verificando_Tabela_Arp(self, ip: str):
        if self.Validando_IP(ip):
            if self.__tabelaArp[ip] is not None:
                return self.__tabelaArp[ip]
            else:
                return False

    def Exibindo_Tabela_Arp(self):
        self.__tabelaArp.listTabela()

    def __str__(self):
        return f"Nome: {self.__nome}, {super().__str__()}"
