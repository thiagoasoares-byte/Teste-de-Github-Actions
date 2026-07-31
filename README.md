# FastAPI + CI/CD com GitHub Actions 

Este repositório contém uma aplicação construída com **FastAPI**, gerenciamento de dependências utilizando **Poetry** e um pipeline básico de Integração Contínua (CI) configurado via **GitHub Actions**.

## Objetivo do Repositório
O objetivo principal deste projeto é demonstrar a configuração de um pipeline CI/CD básico. A cada `push` na branch `main`, o GitHub Actions é acionado automaticamente para:
1. Configurar o ambiente com Python 3.9.
2. Instalar o Poetry.
3. Restaurar o cache de dependências (otimização de tempo).
4. Instalar as dependências do projeto.
5. Executar os testes automatizados garantindo a qualidade do código.

## Tecnologias Utilizadas
* [Python 3.9](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/) - Framework web rápido e moderno.
* [Poetry](https://python-poetry.org/) - Gerenciador de dependências e empacotamento.
* [Pytest](https://docs.pytest.org/) - Framework para testes automatizados.
* [GitHub Actions](https://github.com/features/actions) - Automação de fluxos de trabalho (CI/CD).

## Como executar localmente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.9+ e o Poetry instalados na sua máquina.
Para instalar o Poetry globalmente, você pode usar o `pipx`:
```bash
pipx install poetry
```

### 2. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 3. Instalar as dependências
Com o Poetry instalado, execute o comando abaixo na raiz do projeto:
```bash
poetry install
```

### 4. Rodar a aplicação FastAPI
(Ajuste o caminho `main:app` conforme a estrutura do seu projeto)
```bash
poetry run uvicorn main:app --reload
```

## 🧪 Como rodar os testes localmente
Para garantir que tudo está funcionando antes de fazer o push, rode o pytest:
```bash
poetry run pytest
```

## ⚙️ Estrutura do CI/CD
O arquivo de workflow está localizado em `.github/workflows/python-app.yml`. Ele garante que nenhum código quebrado seja mesclado na branch principal.
