# Logistics Data Automation Platform

Uma solução corporativa desenvolvida em Python para automatizar atividades operacionais e analíticas da área de logística, focada em processos de Extração, Transformação e Carga (ETL).

O objetivo deste sistema é eliminar atividades manuais de atualização de planilhas e preparação de bases utilizadas em relatórios gerenciais, processando automaticamente diversos arquivos Excel recebidos diariamente e consolidando informações relacionadas ao fluxo logístico.

## 🚀 Principais Funcionalidades

- **Automação de ETL:** Importação automática e consolidação de múltiplos relatórios (Embarques e Trânsito).
- **Business Rules Engine:** Aplicação de regras de negócio para limpeza de dados (ex: remoção de pedidos cancelados).
- **Data Quality:** Validação de integridade dos dados e tratamento de registros nulos e duplicados.
- **Auditoria:** Geração automática de logs detalhados de processamento e histórico de execuções.
- **Interface Gráfica (GUI):** Interface moderna para usuários finais acompanharem o status do processamento com barra de progresso.
- **Data Preparation:** Criação de bases limpas e estruturadas, prontas para consumo em dashboards (Power BI/Tableau).

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** (Processamento de dados, cruzamentos e agregações)
- **OpenPyXL** (Leitura e escrita nativa de arquivos Excel)
- **CustomTkinter** (Interface gráfica moderna e responsiva)
- **Logging** (Monitoramento e auditoria de execução)

## 📁 Arquitetura do Projeto

```text
logistics-report-automation/
│
├── data/
│   ├── input/       # Arquivos Excel de entrada (gerados via mock)
│   ├── output/      # Base consolidada final gerada pelo sistema
│   └── archive/     # Histórico de arquivos processados
│
├── src/
│   ├── core/
│   │   └── etl_processor.py   # Motor principal de regras de negócio e Pandas
│   └── ui/
│       └── app.py             # Interface gráfica CustomTkinter
│
├── logs/            # Arquivos de log de execução
├── setup_and_mock.py # Script de setup e gerador de dados fictícios
├── requirements.txt  # Dependências do projeto
└── README.md