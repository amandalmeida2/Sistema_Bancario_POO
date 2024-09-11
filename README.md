# Projeto Painel Administrativo Bancário - CRUD

## Descrição do Projeto
Este projeto consiste em um Painel Administrativo Bancário que permite o gerenciamento de dados de clientes, utilizando as operações CRUD (Create, Read, Update, Delete). O sistema simula um banco de dados simples onde os usuários podem adicionar, atualizar, visualizar e excluir clientes, além de criar contas bancárias para esses clientes.

## Funcionalidades
**- Criar (Create):** Permite cadastrar novos clientes, salvando informações como CPF, nome, data de nascimento, endereço, telefone, escolaridade, estado civil e e-mail. <br>
<br>
**- Ler (Read):** Exibe os dados de clientes cadastrados, seja de um cliente específico (por CPF) ou de todos os clientes cadastrados.<br>
<br>
**- Atualizar (Update):** Atualiza as informações de clientes já cadastrados no sistema.<br>
<br>
**- Excluir (Delete):** Exclui um cliente cadastrado, removendo seus dados do sistema.<br>
<br>
**- Criar Conta:** Permite a criação de contas bancárias (corrente ou poupança) para clientes cadastrados.
<br>
## Tecnologias Utilizadas
**- Python:** Linguagem de programação principal. <br>
<br>
**- POO (Programação Orientada a Objetos):** Estruturação do sistema através de classes como Pessoa e Cliente, com métodos para realizar as operações CRUD. <br>
<br>
**- CSV:** Armazenamento dos dados dos clientes em arquivos CSV, simulando um banco de dados.<br>
<br>
## Como Executar o Projeto
1. Certifique-se de ter o Python instalado em sua máquina.<br>
2. Baixe o código-fonte do projeto.<br>
3. Execute o script projeto_crud.py usando o terminal ou uma IDE de sua escolha.<br>
4. Siga as instruções no painel administrativo para interagir com o sistema.<br>

### Instruções de Uso
Após iniciar o sistema, será exibido o seguinte menu:

1 - Cadastrar Usuário<br>
2 - Atualizar Usuário<br>
3 - Criar Conta<br>
4 - Excluir Usuário<br>
5 - Exibir Usuário<br>
6 - Sair<br>
Cada opção permitirá que você execute as funções CRUD conforme necessário.<br>

## Estrutura do Projeto
**- Pessoa:** Classe mãe que armazena os atributos básicos de uma pessoa, como nome, CPF, data de nascimento, entre outros.<br>
<br>
**- Cliente:** Classe filha de Pessoa, onde são adicionados atributos específicos como número de conta, tipo de conta e saldo.<br>
<br>
**- CRUD:** Métodos implementados na classe Cliente para adicionar, atualizar, excluir e visualizar os clientes.
