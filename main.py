# Importações
import dht
import machine
import time

# Sensor e relé
d = dht.DHT11(machine.Pin(4))         #d = DHT11
r = machine.Pin(2, machine.Pin.OUT)   #r = relé

# Inicialização de variáveis
r.value(0)
temperatura_atual = 0
humidade_atual = 0

# Laço de repetição principal
while True:
    # Mensuração da temperatura e humidade
    d.measure()
    
    # Recebimento dos dados  da mensuração da temperatura e humidade para poder imprimir e fazer as condições
    temperatura_anterior = temperatura_atual
    humidade_anterior = humidade_atual
    temperatura_atual = d.temperature()
    humidade_atual = d.humidity()

    print("Temperatura = {}°C       Umidade = {}%".format(temperatura_atual, humidade_atual))

    # Condições para ligar o relé
    if temperatura_atual > 31 and temperatura_anterior <= 31:
        print("======================================")
        print("Temperatura maior que 31°C!")
        if r.value() == 0 and humidade_atual <= 70:
            print("Ligando o relé...")
            r.value(1)
        print("======================================")
    if humidade_atual > 70 and humidade_anterior <= 70:
        print("======================================")
        print("Humidade relativa do ar maior que 70%!")
        if r.value() == 0 and temperatura_atual <= 31:
            print("Ligando o relé...")
            r.value(1)
        print("======================================")
    
    # Condições para desligar o relé
    if temperatura_atual <= 31 and temperatura_anterior > 31:
        print("======================================")
        print("Temperatura menor que 32°C!")
        if r.value() == 1 and humidade_atual <= 70:
            print("Desligando o relé...")
            r.value(0)
        print("======================================")
    if humidade_atual <= 70 and humidade_anterior > 71:
        print("======================================")
        print("Humidade relativa do ar menor que 71%!")
        if r.value() == 1 and temperatura_atual <= 31:
            print("Desligando o relé")
            r.value(0)
        print("======================================")

    # Tempo de espera entre as medições
    time.sleep(5)
