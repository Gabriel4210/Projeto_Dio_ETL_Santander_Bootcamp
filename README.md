# Santander Bootcamp 2025.2 - Pipeline de ETL com Python

> Desafio de projeto da DIO refatorado para garantir execução offline e independência de APIs instáveis.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📋 Sobre o Projeto

Este projeto implementa um pipeline **ETL (Extract, Transform, Load)** completo. 

O objetivo original do desafio era consumir uma API de usuários e usar a OpenAI para gerar mensagens de marketing. **Nesta versão**, o foco foi criar uma arquitetura resiliente que simula o comportamento da IA através de lógica interna (Mock), permitindo que o projeto seja executado a qualquer momento sem custos de API ou riscos de *downtime* do servidor.

## ⚙️ Funcionalidades

* **Extract:** Leitura de dados de clientes a partir de arquivos CSV (substituindo chamadas API instáveis).
* **Transform:** Lógica de "IA Simulada" usando `random` e templates de texto baseados no perfil do cliente (Investidor, Viajante, etc.). Utiliza `pandas.apply` para processamento eficiente.
* **Load:** Exportação dos dados enriquecidos para um novo arquivo CSV pronto para consumo.
* **Robustez:** Verificação de existência de arquivos e tratamento de exceções.

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x instalado.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [[https://github.com/Gabriel4210/Projeto_Dio_ETL_Santander_Bootcamp.git](Gabriel4210/Projeto_Dio_ETL_Santander_Bootcamp.git)
   cd Projeto_Dio_ETL_Santander_Bootcamp
