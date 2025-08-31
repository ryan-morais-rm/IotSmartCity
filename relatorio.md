# INTRODUÇÃO

Neste trabalho desenvolvemos um ecossistema de simulação e monitoramento de dispositivos IoT (Internet of Things), 
integrando diferentes tecnologias para coleta, exposição e análise de métricas. A proposta central foi criar uma smart home simulada, 
composta por dispositivos inteligentes (como TV, lâmpada e máquina de lavar), que geram métricas de uso de CPU, memória e rede em 
tempo real.
Ao longo do processo, estruturamos o ambiente em containers Docker, utilizando Prometheus para coleta de métricas. Além disso, 
implementamos uma API em Flask para expor informações detalhadas de cada dispositivo, 
bem como rotinas de exportação de dados em CSV, que permitem análise posterior em ambientes como o Jupyter Notebook, facilitando a 
construção de gráficos e insights temporais sobre o comportamento dos dispositivos.
O desenvolvimento passou por várias etapas: desde a configuração dos dispositivos simulados e redes de containers, 
até a instrumentação de métricas para Prometheus, integração com Grafana e exportação de dados históricos para análise offline. 
O resultado é um fluxo completo que demonstra, em escala reduzida, como uma infraestrutura IoT inteligente pode ser monitorada, 
analisada e estudada de forma prática e escalável.


# DESENVOLVIMENTO
O projeto foi construído em etapas bem definidas, cada uma agregando uma camada de funcionalidades ao ecossistema IoT simulado.
## 1. Modelagem dos Dispositivos IoT
  Criamos três classes principais que representam os dispositivos inteligentes:
**- SmartTv –** simulando uma TV conectada, com atributos de marca, modelo, aplicativos conectados, níveis de CPU e memória disponíveis, 
  além de rede.
**- SmartLight –** uma lâmpada inteligente com controle de cores, intensidade da luz, temperatura e consumo de recursos computacionais.
**- SmartWashingMachine –** uma máquina de lavar com informações de capacidade, roupas em lavagem e estado atual do ciclo.
## 2. Cada dispositivo possui listas de métricas de CPU, memória e rede que foram preenchidas com valores simulados de forma natural 
   (aumentando e diminuindo gradualmente), para evitar oscilações artificiais. Dessa forma, conseguimos reproduzir um comportamento 
   mais próximo de um dispositivo real em funcionamento.
## 3. API em Flask
A API foi responsável por expor as informações e métricas dos dispositivos:
- /devices – listava todos os dispositivos disponíveis com suas descrições gerais.
- /metrics – retornava as métricas de cada dispositivo (CPU, memória e rede).
- /tv, /light, /washer – endpoints individuais para cada dispositivo, expondo suas informações detalhadas.
## 4. Além disso, criamos o endpoint /export, que permitia salvar as métricas em formato CSV, possibilitando sua análise externa em 
ferramentas como Jupyter Notebook, como realizamos. 
## 5. Prometheus
Para monitoramento contínuo, utilizamos Prometheus como sistema de coleta de métricas como plataforma de visualização:
  No Prometheus, configuramos jobs que consultavam o endpoint de métricas da API em Flask.
  Os serviços foram orquestrados com Docker Compose, organizados em uma rede isolada do Docker.
  Isso permitiu que todos os containers (dispositivos, Prometheus) se comunicassem de forma transparente, 
  simulando uma rede IoT real.
## 6. Exportação de Dados em CSV
Além da coleta via Prometheus, implementamos a exportação dos dados em arquivos CSV. Foram gerados arquivos contendo até 
  1000 linhas de métricas simuladas, representando leituras sucessivas dos dispositivos ao longo do tempo.
  O formato utilizado no CSV foi:
    device,cpu_usage,mem_usage,net_usage
    tv,34,204,89
    light,12,32,15
    washer,28,122,48
## 7. Análise em Jupyter Notebook
- Por fim, estruturamos notebooks no Jupyter para leitura e análise dos arquivos CSV. Neles, aplicamos bibliotecas como pandas 
e matplotlib para ler os dados exportados;
- Filtrar métricas específicas (como as da TV);
- Gerar gráficos temporais mostrando a variação de CPU, memória e rede ao longo das 1000 leituras.
- Isso tornou possível observar padrões de comportamento dos dispositivos simulados, como picos de uso de rede ou ciclos de 
  maior/melhor consumo de CPU.


# ANÁLISE DOS DADOS
- Com base nos dados fornecidos, é possível tirar algumas conclusões sobre o consumo de CPU, memória e rede dos 
  dispositivos monitorados: TV, máquina de lavar (washer) e luzes (light).
## 1.CPU:
- A TV apresenta picos muito altos de CPU, chegando próximo a 100% em vários momentos, mas também momentos de baixo uso 
  (próximo a 5–20%). Isso indica que a TV realiza tarefas intensivas de processamento em certos períodos, possivelmente 
  durante reprodução de vídeos ou processamento de aplicações, mas fica ociosa em outros momentos.
- A máquina de lavar também tem picos de CPU elevados, geralmente entre 60–90%, mas seu uso médio tende a ser mais 
  constante que o da TV, indicando que o processamento está mais ligado à operação contínua do ciclo de lavagem.
- As luzes apresentam altos picos de CPU (até quase 100%), mas também períodos de uso baixo, mostrando que os controles 
  inteligentes consomem processamento variável, possivelmente dependendo de comandos ou ajustes de intensidade.
## 2.Memória:
- A TV tem um consumo de memória moderado a alto, com variações entre ~50 MB até mais de 2 GB. Isso sugere que a TV utiliza 
  bastante memória para buffering de vídeo, apps e processos em execução.
- A máquina de lavar tem consumo de memória geralmente alto (frequentemente acima de 1 GB), mostrando que o sistema embarcado 
  precisa gerenciar sensores, ciclos e talvez comunicação com apps de controle remoto.
- As luzes têm consumo de memória menos intenso que a TV e a máquina de lavar, mas ainda assim variam bastante, 
  indicando que cada ajuste de comando ou automação temporária pode aumentar o uso.
## 3.Rede:
- A TV mostra altos picos de rede, algumas vezes acima de 900 unidades (provavelmente KB/s ou similar), principalmente 
  em momentos de transmissão de vídeo, streaming ou atualizações.
- A máquina de lavar tem uso de rede moderado, normalmente entre 100 e 900, sugerindo que a comunicação remota não é constante, 
  mas relevante para sincronização ou monitoramento remoto.
- As luzes também apresentam picos de rede altos, variando bastante, provavelmente devido a comandos remotos, automações ou 
  sincronização com aplicativos.


# CONCLUSÃO GERAL:
## 1. Podemos observar que a TV é o dispositivo mais variável em consumo de CPU e rede, alternando entre períodos de alto e baixo uso, 
   provavelmente ligados ao streaming e execução de apps. A máquina de lavar mantém um consumo mais constante de CPU e memória, 
   mas com picos de rede moderados. Já as luzes inteligentes apresentam grande variabilidade em CPU e rede, mas memória relativamente 
   menor, mostrando que seu processamento depende de comandos e automações momentâneas.

# Em resumo:
**1. CPU**: TV e luzes têm picos intensos; máquina de lavar é mais constante.
**2. Memória**: Máquina de lavar e TV usam mais, luzes usam menos.
**3. Rede**: TV e luzes têm picos altos; máquina de lavar usa rede de forma moderada.
