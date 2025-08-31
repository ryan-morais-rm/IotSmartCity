# IoT Smart City - Projeto Prático

## Descrição

Este projeto simula uma rede de **IoT heterogênea** em um ambiente de **Smart City**, utilizando três dispositivos inteligentes:

- **Smart TV**
- **Smart Light**
- **Smart Washing Machine**

O objetivo é **emular o funcionamento dos dispositivos**, gerar métricas de CPU, memória e rede, e disponibilizá-las para monitoramento usando **Prometheus** e **Grafana**.

---

## Estrutura do Projeto

IotSmartCity/
├── devices/
│ ├── app.py # API Flask principal
│ ├── Device.py # Classe base para dispositivos
│ ├── SmartLight.py
│ ├── SmartTv.py
│ ├── SmartWashingMachine.py
│ ├── requirements.txt
│ ├── Dockerfile # Dockerfile da API
├── docker-compose.yaml # Orquestração Docker
├── network/
│ └── configuration.sh # Configuração de rede (opcional)
├── prometheus/
│ └── prometheus.yml # Configuração do Prometheus
├── README.md
└── ...


---

## Tecnologias

- **Python 3** – Lógica dos dispositivos e API.
- **Flask** – Servidor web para expor dados e métricas.
- **Docker** – Contêinerização dos dispositivos.
- **Docker Compose** – Orquestração dos containers.
- **Prometheus** – Coletor de métricas.
- **Grafana** – Visualização dos dashboards.
- **Prometheus Client (Python)** – Exposição de métricas dinâmicas.

---

## Dispositivos

### Smart TV
- Canais, apps conectados/desconectados
- Ligar/desligar
- Fazer chamadas fictícias

### Smart Light
- Ajuste de cor, intensidade de luz e temperatura
- Simulação de uso de CPU, memória e rede

### Smart Washing Machine
- Adicionar/remover roupas
- Ciclo de lavagem
- Monitoramento de CPU, memória e rede

---

## Métricas

- **CPU Usage (%)**
- **Memory Usage (%)**
- **Network Usage (%)**

As métricas são **atualizadas a cada requisição** ao endpoint `/metrics`.

---

## Endpoints da API

| Rota | Descrição |
|------|-----------|
| `/` | Boas-vindas e lista de dispositivos disponíveis |
| `/devices` | Informações gerais de todos os dispositivos |
| `/metrics` | Métricas de CPU, memória e rede (para Prometheus) |
| `/tv` | Informações específicas da Smart TV |
| `/light` | Informações específicas da Smart Light |
| `/washer` | Informações específicas da Smart Washing Machine |

---

## Docker

### Build da API

```bash
cd devices/
docker build -t iot-devices .
