from dispositivo import Dispositivo

class Switch(Dispositivo):
    def __init__(self, ip: str, mac: str):
        super().__init__(ip, mac)
        self.__Num_Portas = 8
        self.__Tabela_Roteamento = [None]*self.__Num_Portas

    @property
    def Num_Portas(self):
        return self.__Num_Portas

    def Validando_IP(self, ip: str):
        return super().Validando_IP(ip)

    def Validando_MAC(self, mac: str):
        return super().Validando_MAC(mac)

    def Conetando_Computador(self, porta: int, mac: str):
        if self.Validando_MAC(mac):
            if self.__Tabela_Roteamento[porta] is None:
                self.__Tabela_Roteamento[porta] = mac
            else:
                print("Porta estar em uso.")
        else:
            print("Endereço MAC inválido!")

    def Verificando_Conexao(self, mac: str):
        if mac in self.__Tabela_Roteamento:
            return True
        else:
            return False

    def Listando_Portas(self):
        print(f"{'PORTA':<5} | {'MAC':^17}")
        for i in range(len(self.__Tabela_Roteamento)):
            mac = self.__Tabela_Roteamento[i]
            if mac is not None:
                print(f"{i:^5} | {mac}")
            else:
                print(f"{i:^5} | {'-----------------':^17}")
