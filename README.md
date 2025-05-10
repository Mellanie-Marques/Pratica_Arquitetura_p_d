# Resposta da Atividade Arquitetura de SD e Threads

Este repositório contém a resposta da atividade da disciplina **Programação Distribuída**, referente ao tema **Arquitetura de Software e Threads**.

## Descrição

A atividade foi respondida utilizando a linguagem **Python**. O código implementa a comunicação entre um **servidor** e **cliente**, onde o servidor gerencia um dicionário compartilhado entre as partes, permitindo operações como adicionar, remover e consultar elementos. A comunicação entre servidor e cliente foi realizada através da biblioteca **hprose**.

## Estrutura do Repositório

- **servidor.py**: Contém a implementação do servidor que fornece o serviço de manipulação do dicionário.
- **cliente.py**: Contém a implementação do cliente que consome os métodos remotos do servidor.
- **README.md**: Este arquivo com a descrição do projeto.

## Tecnologias Utilizadas

- **Python 3.x**
- **hprose**: Biblioteca para comunicação remota entre o servidor e o cliente.
- **Threads**: Utilização de threads para gerenciamento simultâneo de operações no servidor.

## Como Executar

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/usuario/repositorio.git
2. Instale as dependências necessárias:
   ```bash
   pip install hprose
3. Primeiro, execute o servidor:
   ```bash
   python servidor.py
4. Depois, execute o cliente em uma outra instância do terminal:
   ```bash
   python cliente.py

## Objetivo

 Implementar a arquitetura de comunicação entre servidor e cliente, utilizando threads para gerenciar operações concorrentes no servidor e métodos remotos para a interação entre as partes.
