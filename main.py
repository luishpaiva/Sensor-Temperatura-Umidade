# Importação da biblioteca 'wifi_lib.py'
from wifi_lib import conecta

# Importação de bibliotecas externas
import dht
import machine
import urequests
import time

# Receber nome da rede e senha para realizar a conexão
ssid = input("Informe o nome da rede a qual deseja se conectar: ")
senha = input("Informe a senha da rede: ")

# Imprimir mensagem 'conectando'
print("Conectando...")

# Nova instância de 'conecta' com o nome da rede e a senha como parâmetros
station = conecta(ssid, senha)

# Verifica se está conectado
if not station.isconnected():
    print("Não conectado! Verifique os dados de rede e a conexão e tente novamente.")
else:
    print("Conectado!")
    
    # Número da chave API do Thingspeak
    api_key = input("Informe a chave API (API Key) do Thingspeak: ")

    # Inicialização das variáveis do sensor DHT11 e do relé
    d = dht.DHT11(machine.Pin(4))         #d = DHT11
    r = machine.Pin(2, machine.Pin.OUT)   #r = relé

    # Inicialização do status do relé como desligado
    r.value(0)

    # Receber quantidade de vezes a ser repetida a leitura dos dados
    quantidade = int(input("Informe a quantidade de leituras que deseja fazer (5760 = 1 dia): "))
    
    # Imprimir mensagem de início de leitura dos dados
    print("Começando a leitura dos dados...")
    
    # Cabeçalho
    print("\n===========================================")
    print("        Início da leitura dos dados")
    print("===========================================")

    for i in range(quantidade):
        # Mensuração da temperatura e umidade
        d.measure()
        
        # Condição para ligar o relé
        if (d.temperature() > 31 or d.humidity() > 70) and r.value() == 0:
            print("-------------------------------------------")
            print("Ligando o relé...")
            print("-------------------------------------------")
            r.value(1)

        # Condição para desligar o relé
        if (d.temperature() <= 31 and d.humidity() <= 70) and r.value() == 1:
            print("-------------------------------------------")
            print("Desligando o relé...")
            print("-------------------------------------------")
            r.value(0)

        # Imprimir valores da temperatura e umidade
        print("{}.".format(i + 1), (" " * (len(str(quantidade)) - len(str(i + 1)))), "Temperatura = {}°C    Umidade = {}%".format(d.temperature(), d.humidity()))

        # Upload dos dados de temperatura, umidade e status do relé no servidor Thingspeak
        resposta = urequests.get("https://api.thingspeak.com/update?api_key={}&field1={}&field2={}&field3={}".format(api_key, d.temperature(), d.humidity(), r.value()))

        # Fechamento da variável
        resposta.close()

        # Verificar para não precisar esperar 15 segundos no último laço
        if (i < quantidade - 1):
            # Tempo de espera para poder fazer novo upload no Thingspeak
            time.sleep(15)

    # Fechamento da conexão
    station.disconnect()