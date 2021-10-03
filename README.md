Projeto da disciplina de Fundamentos de Internet das Coisas.

ETAPA 1

Esta atividade tem como propósito comparar as características dos computadores de uso geral com os utilizados para internet das coisas. Para isso, siga os passos:
1. Pesquise quatro propagandas atuais de computadores de uso geral (laptops ou desktops) à venda no comércio on-line. Para cada uma delas, localize as principais características anunciadas, destacando:

    - Capacidade de memória RAM (em GB);
    - Capacidade do disco (em GB ou TB);
    - Velocidade de clock do processador (em GHz);
    - Dispositivos de rede integrados Wi-Fi e/ou ethernet (apenas identifique SIM ou NÃO);
    - Potência consumida (em W);
    - Preço (em R$).

    No MS Word, elabore uma tabela com as principais características dos anúncios encontrados.

1. Pesquise na internet as mesmas seis características, agora para os três módulos microprocessadores geralmente usados na prototipação de dispositivos para internet das coisas:

    - Arduino UNO;
    - ESP32 WROOM;
    - Raspberry Pi 3.

    Dica: para esses três módulos, substitua a característica “capacidade de disco” por “capacidade de memória Flash”. Essa substituição é necessária, pois os módulos não possuem um disco integrado, utilizando a memória Flash para esse fim.
    Complemente a tabela gerada no item anterior com as principais características dos módulos microprocessadores obtidas.

3. Adicione ao documento um parágrafo (máximo 3 linhas) com a comparação das seis características, identificando as limitações dos módulos microprocessadores (passo 2) com relação aos computadores de uso geral (passo 1).

4. Localize a implementação de três projetos de internet das coisas usando qualquer um dos três módulos microprocessadores (Arduino Uno, ESP32 WROOM ou Raspberry Pi 3).

5. Adicione ao documento um parágrafo (máximo 5 linhas) comentando os projetos localizados no item anterior (não se esqueça de adicionar o link para o projeto).
Ao final, você deve ter um único documento com os itens pedidos nos passos 1, 2, 3 e 5.

    Ao final desta etapa, você terá uma melhor compreensão das características e limitações dos módulos geralmente usados para internet das coisas, bem como suas possíveis aplicações. Não negligencie esta etapa. Ela será muito útil para as próximas duas.

ETAPA 2

Chegou a hora de começar o trabalho prático!
Nesta etapa, você deve realizar três atividades muito importantes: a configuração inicial do seu sistema para o desenvolvimento da estação meteorológica; testes com um atuador (relé) controlado pelo ESP32; e testes com um sensor de umidade e temperatura atmosféricas (DHT11) acessado pelo ESP32. Siga os passos:

1. Realize a configuração inicial da plataforma ESP32, conectando-a ao computador. Este é o primeiro passo para implementar o projeto de nossa pequena estação meteorológica. Para orientar a realização deste passo, acesse o vídeo que preparamos e siga as instruções: http://iot.microprocessadores.com.br/esp32/1.setupESP32.html.
2. Agora, vamos aprender a controlar um dispositivo elétrico pelo seu módulo ESP32. Para orientar a realização deste passo, acesse o vídeo que preparamos e siga as instruções: http://iot.microprocessadores.com.br/esp32/2.ESP32.RELAY.html.
3. Por fim, vamos aprender a ler a umidade e temperatura ambiente utilizando um sensor e seu ESP32. Para orientar a realização deste passo, acesse o vídeo que preparamos e siga as instruções: http://iot.microprocessadores.com.br/esp32/3.ESP32.DHT11.html.

Ao assistir aos procedimentos, dê uma pausa no vídeo e repita a operação com seu módulo.
Ao final desta etapa, você terá aprendido a configurar um ambiente para iniciar os testes e desenvolvimento de um sistema para internet das coisas.
O material do trabalho prático está na raíz do repositório (FIC-Material.zip).

ETAPA 3

Agora é a sua vez de iniciar a implementação da nossa estação meteorológica.
Utilizando o módulo ESP32, o relé e o sensor de temperatura/umidade DHT11, implemente um sistema que atenda aos requisitos:
   - Monitore a temperatura e a umidade por meio do DHT11, imprimindo as informações na tela do computador.
   - Adicione ao código ações para ligar o relé caso ocorra qualquer das condições a seguir. Observe que basta que uma das condições seja verdadeira para que o relé seja ligado.
        <table border=1>
            <tr>
                <td>Temperatura > 31 °C</td>
            </tr>
            <tr>
                <td>Umidade relativa do ar > 70%</td>
            </tr>
        </table> 
Caso nenhuma das condições esteja presente, o relé deve ser desligado.</br>
<b>Observação:</b> utilize a criatividade para que o sensor alcance as condições de teste apresentadas (faz parte da atividade).

ETAPA 4

Agora, vamos ligar a nossa estação meteorológica à internet.</br>
Sobre a implementação da etapa anterior, adicione a funcionalidade para que a temperatura e umidade lidas do DHT11 sejam enviadas para um servidor de dados IoT na nuvem, chamado Thingspeak. Para realizar esta etapa, assista aos vídeos instrucionais do link:</br>
http://iot.microprocessadores.com.br/esp32/4.ESP32.Thingspeak.html</br>
No primeiro vídeo, é mostrado como configurar o ESP32 para conectá-lo à rede Wi-Fi (do celular ou de casa) e, no segundo, como acessar o Thingspeak, enviando as informações.