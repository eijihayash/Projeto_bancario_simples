# Projeto Bancário Simple em Python - Versões V1 e V2

Projeto Educacional de um sistema bancário simples em Python que utiliza conceitos de programação orientada a objetos para gerenciar clientes, contas correntes e poupança, saques e autetificação.

# Versão do Python

Este projeto foi desenvolvido e testado com Python 3.13.1

## Funcionalidades
- Cadastro de cclientes.
- Criação de contas correntes e poupança.
- Depósitos e saques com controle de saldo e limite especial.
- Autentificação básico de clientes.

## Visão Geral

- **V1**: Implementação inicial com as classes básicas `Conta` (abstrata), `ContaCorrente`, `ContaPoupanca`, `Pessoa`, `Cliente` e `Banco`.
  - Contas com métodos de depósito, saque, e verificação de saldo.
  - Cliente pode possuir uma ou mais contas.
  - Banco faz cadastro de clientes e contas, e autentica clientes.
  - Limite de cheque especial implementado na conta corrente.
  - Código com uso de propriedades e abstração.

- **V2**: Refatoração para modularização em pacotes, melhoria na autenticação e organização das classes.
  - Separação em módulos: `banco.py`, `contas.py`, `pessoas.py` e `main.py`.
  - Uso de anotações de tipo e melhor tratamento de erros.
  - Controle mais robusto de autenticação garantindo que conta, cliente e agência estão cadastrados.
  - Classes com métodos mais claros e mensagens de feedback mais detalhadas.
  - Melhoria na estrutura das classes Cliente e Banco para melhor gerenciamento de contas e clientes.
  - Testes básicos de operação no `main.py` para exemplificar funcionalidades.

## Autor 
Eiji - Desenvolvedor iniciante estudando Python



