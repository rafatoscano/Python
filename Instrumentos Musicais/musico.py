class musico:
    def __init__(self, Nome, Nacionalidade):
        self.nome = Nome
        self.nacionalidade = Nacionalidade  

    def getNome(self):
        return self.nome

    def getNacionalidade(self):
        return self.nacionalidade

    def iniciarDemonstracao(self):
        print('Iniciando demonstração...')

    def addInstrumento(self):
        print('Instrumento adicionado!')

    def exibirInstrumentos(self):
        print('Instrumentos: \n')
