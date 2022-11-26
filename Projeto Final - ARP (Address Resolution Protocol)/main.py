from computador import Computador
from switch import Switch

c1 = Computador('192.168.0.1', '00:E0:4C:55:6D:D0', 'C1')
c2 = Computador('192.168.2.1', '00:E0:6C:5B:6D:D2', 'C2')

c1.Tabela_Arp('192.168.0.2', '00:E0:4C:52:B5:B9')
c1.Tabela_Arp('192.168.0.3', '00:E0:2C:54:B2:B3')

c2.Tabela_Arp('192.168.2.2', '00:E0:4C:18:8B:C1')
c2.Tabela_Arp('192.168.2.3', '00:E0:4C:0E:DF:F6')

sw1 = Switch('10.0.0.1', '00:E0:4C:48:BC:B2')

sw1.Conetando_Computador(1, '00:E0:4C:18:8B:C1')
sw1.Conetando_Computador(2, '00:E0:4C:52:B5:B9')

sw1.Listando_Portas()

mac = c1.Verificando_Tabela_Arp('192.168.0.2')

print(mac)
