
# BankApp

Projeto desenvolvido durante a disciplina de Projetos à Programação do Departamento de Computação da Universidade Federal Rural de Pernambuco. O projeto consiste na criação de um sistema bancário utilizando a linguagem de programação Python e a biblioteca Kivy.

* A ideia principal da aplicação é poder realizar 3 operações: depósito, saque e visualizar extrato.
* A operação saque só pode ser feita 3 vezes com limite de 500 reais por saque.

## Funcionalidades

* **Tela Inicial**: Apresenta opções para visualizar extrato, realizar saque ou depósito.
* **Tela de Extrato**: Mostra o histórico de transações e o saldo atual.
* **Tela de Saque**: Permite que o usuário realize saques, com validações para saldo e limites.
* **Tela de Depósito**: Permite que o usuário faça depósitos, com validações de valor.
* **Tela de Sucesso**: Exibe uma mensagem de sucesso após uma operação bem-sucedida.
* **Tela de Erro**: Exibe mensagens de erro para operações que falharam.


## Estrutura do código

* Configurações de Estilo: Define o fundo da janela como branco e configura o estilo dos botões.
* Variáveis Globais: Armazena o saldo, o histórico de transações e o número de saques.
* Funções: Contém funções para realizar depósitos, saques e gerar o extrato.
* Classes de Tela: Define o layout e o comportamento das diferentes telas do aplicativo.
* TelaInicial: Tela de boas-vindas com opções de navegação.
* TelaExtrato: Exibe o extrato com um botão para voltar.
* TelaSaque: Campo para inserir o valor do saque e botões para confirmar ou voltar.
* TelaDeposito: Campo para inserir o valor do depósito e botões para confirmar ou voltar.
* TelaSucesso: Mostra uma mensagem de sucesso e botão para voltar.
* TelaErro: Mostra uma mensagem de erro e botão para voltar.
* Gerenciador de Telas: Gerencia as diferentes telas da aplicação.
* Aplicação Principal: Inicializa e executa o aplicativo.
## Requisitos

Para executar este aplicativo, você precisa ter Python e Kivy instalados.

Instale Kivy usando o seguinte comando:
```
pip install Kivy
```

## Executando o aplicativo

Execute o arquivo banco_app.py
