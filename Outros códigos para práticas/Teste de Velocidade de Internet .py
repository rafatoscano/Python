#Se não estiver instalado a biblioteca, executar: "pip install speedtest-cli" ou outra biblioteca que queira usar

import speedtest

teste = speedtest.Speedtest()
#Dodnload
print("Verificando a velocidade de Download")
velocidade_download = teste.download()
print (f"Velocidade de Download: {velocidade_download / 10**6:.2f}")

#Upload
print("Verificando a velocidade de Upload")
velocidade_upload = teste.upload()
print (f"Velocidade de Upload: {velocidade_upload / 10**6:.2f}")

#Ping
ping = teste.results.ping
print(f"Ping: {ping:.2f}")