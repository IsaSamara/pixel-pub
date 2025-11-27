# Pixel Pub API

## Sobre o projeto

Bem-vindo ao Pixel Pub, um sistema backend desenvolvido em Python + FastAPI para gerenciar operações internas de um bar temático de jogos de tabuleiro e RPG. Ele concentra a lógica de negócio: desde controle de estoque, cadastro de produtos,
cadastro de funcionários a demais funcionalidades essenciais.

Este repositório contém exclusivamente a API backend, responsável pela lógica de negócio, persistência de dados e exposição de endpoints REST.

## Estrutura do projeto

    pixel-pub/

     ├── crud/          # Funções de acesso e manipulação de dados (CRUD)
     ├── models/        # Modelos do SQLAlchemy
     ├── schemas/       # Classes Pydantic (entrada e saída de dados)
     ├── routers/       # Rotas organizadas por módulo
     ├── database.py    # Conexão e sessão do banco
     └── main.py

## Tecnologias utilizadas

    ◆ Python 3.13
    ◆ FastAPI
    ◆ SQLAlchemy (ORM)
    ◆ Pydantic (validação de dados)
    ◆ Uvicorn (servidor ASGI)
    ◆ Banco de dados (SQLServer)
