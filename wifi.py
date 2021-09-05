from wifi_lib import conecta
import urequests

print("Conectando...")
station = conecta("nome_conexao", "senha_de_acesso")
if not station.isconnected():
    print("Não conectado!")
else:
    print("Conectado!")
    print("Acessando a URL desejada...")
    resposta = urequests.get("http://teste.afonsomiguel.com")
    print("Página acessada:")
    print(resposta.text)
    station.disconnect()