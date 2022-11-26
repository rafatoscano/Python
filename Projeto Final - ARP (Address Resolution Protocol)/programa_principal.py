import csv
from computador import Computador
from switch import Switch
from grafo import Graph

def Info_Computadores():
    computadores = []
    with open('data/computadores.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)
        for row in csv_reader:
            computador = dict()
            computador['ip'] = row[0]
            computador['nome'] = row[1]
            computador['mac'] = row[2]
            computador['tabela_ARP'] = row[3].split(',')
            computadores.append(computador)
    return computadores

def Info_Switchs():
    switchs = []
    with open('data/switchs.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)
        for row in csv_reader:
            switch = dict()
            switch['ip'] = row[0]
            switch['mac'] = row[1]
            switch['tabela_roteamento'] = row[2].split(',')
            switchs.append(switch)
    return switchs

def Registro_Computadores(listaComputadores: list):
    cadComputadores = []
    for pc in listaComputadores:
        computador = Computador(pc['ip'], pc['mac'], pc['nome'])
        for ipMac in pc['tabela_ARP']:
            if ipMac != '':
                ip, mac = ipMac.split('|')
                computador.tabelaArp(ip, mac)
        cadComputadores.append(computador)
    return cadComputadores

def Registro_Switchs(listaSwitchs: list):
    cadSwitchs = []
    for sw in listaSwitchs:
        switch = Switch(sw['ip'], sw['mac'])
        for portaMac in sw['tabela_roteamento']:
            if portaMac != '':
                porta, mac = portaMac.split('|')
                switch.conetarComputador(int(porta), mac)
        cadSwitchs.append(switch)
    return cadSwitchs

def Criar_Vertices(switchs: list, computadores: list):
    vertices = []
    for i in range(len(switchs)):
        for j in range(len(computadores)):
            if switchs[i].verificarConexao(computadores[j].mac):
                vertices.append(
                    (f"C{j+1}", computadores[j], f"S{i+1}", switchs[i]))

    return vertices

if __name__ == "__main__":
    computadores = Registro_Computadores(Info_Computadores())
    switchs = Registro_Switchs(Info_Switchs())

    # C1->S1, C2->S1, S1->S2, C3->S2, C4->S2
    g = Graph()
    vertices = Criar_Vertices(switchs, computadores)

    for lista in vertices:
        g.addEdge(lista[1], lista[3])
    g.addEdge(switchs[0], switchs[1])
