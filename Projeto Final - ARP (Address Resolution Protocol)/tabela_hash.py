class TabelaHash:
    def __init__(self):
        self.__MAX = 2
        self.__table = [[] for i in range(self.__MAX)]

    def gethash(self, chave):
        hash = 0
        for char in chave:
            hash += ord(char)
        return hash % self.__MAX

    def Listando_Tabela(self):
        print(f"{'IP':^11} | {'MAC':^17}")
        for items in self.__table:
            for elementos in items:
                print(f"{elementos[0]} | {elementos[1]}")

    def __getitem__(self, chave):
        hash = self.gethash(chave)
        for elemento in self.__table[hash]:
            if elemento[0] == chave:
                return elemento[1]

    def __setitem__(self, chave, valor):
        hash = self.gethash(chave)
        encontrado = False
        for id, elemento in enumerate(self.__table[hash]):
            if len(elemento) == 2 and elemento[0] == chave:
                self.__table[hash][id] = (chave, valor)
                encontrado = True
                break
        if not encontrado:
            self.__table[hash].append((chave, valor))

    def __delitem__(self, chave):
        hash = self.gethash(chave)
        for id, elemento in enumerate(self.__table[hash]):
            if elemento[0] == chave:
                del self.__table[hash][id]
