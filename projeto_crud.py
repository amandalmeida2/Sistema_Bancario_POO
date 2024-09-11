# Classe principal
import csv
import random
from datetime import datetime, date
import os

#********************SUPER CLASSE - CLASSE MÃE********************************
class Pessoa:
      def __init__(self, nome:str, dt_nasc:str, cpf:str, endereco:str, telefone:str, escolaridade:int, estado_civil:str, email:str)-> None:

          self._nome = nome
          self._dt_nasc = dt_nasc
          self._cpf = cpf
          self._endereco = endereco
          self._telefone = telefone
          self._escolaridade = escolaridade
          self._estado_civil = estado_civil
          self._email = email
          self._instrucao = None

      @property
      def nome(self):
          return self._nome
      @nome.setter
      def nome(self,nome):
          self._nome = nome

      @property
      def dt_nasc(self):
          return self._dt_nasc
      @dt_nasc.setter
      def dt_nasc(self, dt_nasc):
          self._dt_nasc = date.fromisoformat(dt_nasc)

      @property
      def cpf(self):
          return self._cpf
      @cpf.setter
      def cpf(self,cpf):
          self._cpf = cpf

      @property
      def endereco(self):
          return self._endereco
      @endereco.setter
      def endereco(self, endereco):
          self._endereco = endereco

      @property
      def telefone(self):
          return self._telefone
      @telefone.setter
      def telefone(self, telefone):
          self._telefone = telefone

      @property
      def escolaridade(self):
          return self._escolaridade
      @escolaridade.setter
      def escolaridade(self, escolaridade):
          self._escolaridade = escolaridade

      @property
      def estado_civil(self):
          return self._estado_civil
      @estado_civil.setter
      def estado_civil(self, estado_civil):
          self._estado_civil = estado_civil

      @property
      def email(self):
          return self._email
      @email.setter
      def email(self, email):
          self._email = email

      @property
      def instrucao(self):
          return self._instrucao
      @instrucao.setter
      def instrucao(self, instrucao):
          self._instrucao = instrucao


      def escolaridade_formatada(self):
           if self.escolaridade == 1:
              self.instrucao =  'Analfabeto'
           elif self.escolaridade == 2:
                self.instrucao = 'Fundamental incompleto'
           elif self.escolaridade == 3:
                self.instrucao = 'Fundamental completo'
           elif self.escolaridade == 4:
                self.instrucao = 'Médio incompleto'
           elif self.escolaridade == 5:
                self.instrucao = 'Médio completo'
           elif self.escolaridade == 6:
                self.instrucao = 'Superior incompleto'
           else:
                self.instrucao = 'Superior completo'




#***********************CLASSE CLIENTE FILHA DE PESSOA**************************
class Cliente(Pessoa):

    def __init__(self, nome: str = None, dt_nasc: str = None, cpf: str = None, endereco: str = None ,telefone:str = None, escolaridade: int = None, estado_civil: str = None, email:str = None, conta:str = None, tipo:int = None, saldo:float = 0, idade: int = None) -> None:
        super().__init__(nome, dt_nasc, cpf, endereco, telefone, escolaridade, estado_civil, email)
        self._cadastro = []
        self._linha = None
        #dados para a conta do cliente
        self._conta = None
        self._tipo = tipo
        self._saldo = 0
        self._CABECALHO =  ['cpf', 'nome', 'dt_nasc','idade','endereco', 'telefone','escolaridade', 'estado_civil','email', 'conta', 'tipo', 'saldo', 'cadastro'] # Constante
        self._dt_cadastro = None


    # retorno do str com método mágico
    def __repr__(self):
       return f'{self.linha}'


    @property
    def cabecalho(self):
        return self._CABECALHO

    @property
    def cadastro(self):
        return self._cadastro

    @cadastro.setter
    def cadastro(self,client):

        self._cadastro = client

        #Tenho que fazer que esse método reconheça o CRUD pois esse até corresponde aos usuários do DB

        # match int(client['op']):

        #     case 1: # Seria o adicionar
        #          print()


        #     case 2: # Seria o atualizar
        #          indice = client['index']
        #          client.pop('op', None)
        #          client.pop('index', None)
        #          self.cadastro[indice].update(client)

            # case 3: # Seria o Criar Conta
            #      indice = client['index']
            #      client.pop('op', None)
            #      client.pop('index', None)
            #      self.cadastro[indice].update(client)

            #      #Vamos adicionar os campos faltantes no csv
            #      with open("tab_clientes.csv", "r") as arquivo:
            #           reader = csv.reader(arquivo)
            #           row_update = [row for row in reader if row[0] == self.cadastro[indice]['cpf']]

            #      with open("tab_clientes.csv", "w", newline="") as arquivo:
            #           writer = csv.writer(arquivo)
            #           for row in row_update:
            #               writer.writerow(self.cadastro[indice].update(client))

            # case 4: # Seria o excluir
            #        client.pop('op', None)
            #        self.cadastro.remove(client)




    @property
    def linha(self) -> dict:
        return self._linha

    @linha.setter
    def linha(self,linha) -> None:
        self._linha = linha

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self,conta) -> None:
        self._conta = conta

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,saldo):
        self._saldo = saldo

    @property
    def dt_cadastro(self):
        return self._dt_cadastro
    @dt_cadastro.setter
    def dt_cadastro(self,dt):
        self._dt_cadastro = dt



    def crud_incluir(self):
       hoje = date.today()
       data_nasc = datetime.strptime(self.dt_nasc, "%d/%m/%Y").date()
       self.idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))


       if self.escolaridade == 1:
          self.instrucao =  'Analfabeto'
       elif self.escolaridade == 2:
            self.instrucao = 'Fundamental incompleto'
       elif self.escolaridade == 3:
            self.instrucao = 'Fundamental completo'
       elif self.escolaridade == 4:
            self.instrucao = 'Médio incompleto'
       elif self.escolaridade == 5:
            self.instrucao = 'Médio completo'
       elif self.escolaridade == 6:
            self.instrucao = 'Superior incompleto'
       else:
            self.instrucao = 'Superior completo'


       new_client = {
                   'cpf': self.cpf,
                   'nome': self.nome,
                   'dt_nasc': self.dt_nasc,
                   'idade':self.idade,
                   'endereco': self.endereco,
                   'telefone': self.telefone,
                   'escolaridade': self.instrucao,
                   'estado_civil': self.estado_civil,
                   'email': self.email
       }

       if os.path.isfile('tab_clientes.csv'):
          with open('tab_clientes.csv', 'a') as arquivo:
                writer = csv.DictWriter(arquivo, fieldnames = self._CABECALHO)
                if arquivo.tell() !=0:
                   writer.writerow(new_client)
       else:
            with open('tab_clientes.csv', 'a') as arquivo:
                 writer = csv.DictWriter(arquivo, fieldnames = self._CABECALHO)
                 writer.writeheader()
                 writer.writerow(new_client)

       self.cadastro.append(new_client) # opcionalmente adiciono em uma variável
       ver_client = f'\nCPF: {new_client.get("cpf")} \nNome: {new_client.get("nome")} \nData de Nascimento: {new_client.get("dt_nasc")} \nIdade: {new_client.get("idade")} \nEndereco: {new_client.get("endereco")} \nTelefone: {new_client.get("telefone")} \nEscolaridade: {new_client.get("escolaridade")} \nEstado civil: {new_client.get("estado_civil")} \nE-mail: {new_client.get("email")}\nConta: {new_client.get("conta")} \nTipo: {new_client.get("tipo")} \nSaldo: {new_client.get("saldo")} \nSaldo: {new_client.get("cadastro")} \n'


       print("Cliente adicionado com sucesso!")
       return ver_client



    def crud_excluir(self, cpf):
        new_lista = []
        cliente_excluir = None

        # remoção do CSV
        if os.path.isfile('tab_clientes.csv'):
           with open('tab_clientes.csv', 'r') as arquivo:
                leitura = list(csv.DictReader(arquivo))
                for value in leitura:
                    if value.get('cpf') != cpf:
                       new_lista.append(value)
                    else:
                       cliente_excluir = value

           with open('tab_clientes.csv', 'w') as arquivo:
                escrita = csv.DictWriter(arquivo, fieldnames=self._CABECALHO)
                escrita.writeheader()
                escrita.writerows(new_lista)

           print(f'\nCliente {cpf} excluído com sucesso!')
        else:
          print("\nArquivo CSV não encontrado. Nenhum cliente excluído.")

        if cliente_excluir:
          self.cadastro = [cliente for cliente in self.cadastro if cliente.get('cpf') != cpf]



    def crud_atualizar(self, registro, cpf):

        new_lista = []
        cliente_atualizar = dict()

        if os.path.isfile('tab_clientes.csv'):
           with open('tab_clientes.csv', 'r') as arquivo:
                leitura = csv.DictReader(arquivo)
                for value in leitura:

                    if value.get('cpf') == cpf:
                       cliente_atualizar = value
                       continue
                    new_lista.append(value)


                cliente_atualizar.update(registro) # atualizo o registro do cliente com update do dict
                new_lista.append(cliente_atualizar)

           with open('tab_clientes.csv', 'w') as arquivo:
                escrita = csv.DictWriter(arquivo, fieldnames= self._CABECALHO)
                escrita.writeheader()
                escrita.writerows(new_lista)

           #print(new_lista)
           print(f'\nCliente {registro} atualizado com sucesso!')



    def incluir_conta(self, registro, cpf):

        new_lista = []
        cliente_atualizar = dict()

        if os.path.isfile('tab_clientes.csv'):
           with open('tab_clientes.csv', 'r') as arquivo:
                leitura = csv.DictReader(arquivo)
                for value in leitura:

                    if value.get('cpf') == cpf:
                       cliente_atualizar = value
                       continue
                    new_lista.append(value) # Adiciono todos menos o anterior em uma variável temporária para posterior inserção no CSV


                cliente_atualizar.update(registro) # atualizo o registro do cliente com método [UPDATE] do dict()
                cliente_atualizar['cadastro'] = datetime.now()
                cliente_atualizar['saldo'] = self.saldo # adiciono no dict o saldo
                new_lista.append(cliente_atualizar)  # adiciono o dict atualizado na lista geral

           with open('tab_clientes.csv', 'w') as arquivo:
                escrita = csv.DictWriter(arquivo, fieldnames= self._CABECALHO)
                escrita.writeheader()
                escrita.writerows(new_lista) # adiciona todos novamente no CSV

           #print(new_lista)
           print(f'\nConta: {registro} criada com sucesso!')


    def gerar_conta(self):
         self.conta = f"0892-{random.randint(1000, 3000)}"

    def crud_exibir(self, cpf):

      if os.path.isfile('tab_clientes.csv'):
        with open('tab_clientes.csv', 'r') as arquivo:
            leitura = csv.DictReader(arquivo)
            for cliente in leitura:
                if cliente.get('cpf') == cpf:
                    self.linha = f'\nCPF: {cliente.get("cpf")} \nNome: {cliente.get("nome")} \nData de Nascimento: {cliente.get("dt_nasc")} \nIdade: {cliente.get("idade")} \nEndereco: {cliente.get("endereco")} \nTelefone: {cliente.get("telefone")} \nEscolaridade: {cliente.get("escolaridade")} \nEstado civil: {cliente.get("estado_civil")} \nE-mail: {cliente.get("email")}\nConta: {cliente.get("conta")} \nTipo: {cliente.get("tipo")} \nSaldo: {cliente.get("saldo")} \nSaldo: {cliente.get("cadastro")} \n'

                    return self.linha

        return f'\n Cliente com CPF [{cpf}] não encontrado.'


    def crud_exibir_todos(self):
      lista = []
      if os.path.isfile('tab_clientes.csv'):
        with open('tab_clientes.csv', 'r') as arquivo:
            leitura = csv.DictReader(arquivo)
            for i in leitura:
                lista.append(i)
            self.cadastro = lista



#******************************APLICAÇÃO*************************************



print(f'------------Banco Fantasia------------- \n 🎉 Bem-vindo ao Banco Fantasia! \nOnde seus sonhos financeiros se tornam realidade! \n')

#Instanciar objeto
C = Cliente()


print('--Painel Administrativo--\n')
while True:

   C.crud_exibir_todos()
   dados = C.cadastro # Vou garantir que toda vez que iniciar o loop o sistema traga os usuários do DB atualizados.

   option = int(input('Selecione uma opção:\n1 - Cadastrar Usuário\n2 - Atualizar Usuário\n3 - Criar Conta\n4 - Excluir Usuário\n5 - Exibir Usuário \n6 - Sair\n\n '))

   if option == 6:
      print('Saindo do sistema...')
      print('Foi um prazer tê-lo conosco! Que seu dia seja tão brilhante quanto suas finanças!')
      break

   elif option == 1:

     msg = []


     cpf = input('Digite o CPF, apenas números: ').strip()
     nome = input('Digite o Nome: ').strip().capitalize()
     dt_nasc = input('Data de Nascimento. Ex: 22/08/1980: ').strip()
     email = input('Digite o email: ').strip()
     estado_civil = input('Digite o estado civil: ').strip()
     telefone = input('Digite o seu telefone com DDD: ').strip()
     endereco = input('Endereço:\n [Ex: rua 10\n nr 800\n vila clotilde\n São Paulo-SP\n CEP 10303-560]\n').strip().capitalize()
     escolaridade = int(input('Escolaridade:\n [1] - Analfabeto\n [2] - Fundamental incompleto\n [3] - Fundamento Completo\n [4] - Médio inconleto\n [5] - Médio completo\n [6] - Superior incompleto\n [7] - Superior completo\n\n'))

     checkbox_estado_civil = ['solteiro', 'solteira', 'casado', 'casada']
     nascimento = dt_nasc.split('/')
     res = None
     nome_split = nome.split()
     nome_sem_espaço = None

     # Validação simples dos inputs******************************************
     if len(cpf) != 11 or cpf.isalpha():
        msg.append('CPF deve  possuir 11 caracteres e não conter letras')

     if len(nome_split) > 0:
        for i in nome_split:
            if i.isalpha() == False:
               msg.append('NOME não pode conter número(s)')

     if len(nascimento) !=3:
        msg.append('Insira uma Data de Nascimento Válida')

     if len(nascimento) == 3:
        res = '{}/{}/{}'.format(nascimento[0], nascimento[1], nascimento[2])
     if str(res) != str(dt_nasc):
        msg.append('Data informada está no formato incorreto')
     if email.count('@') > 1 or email.count('@') < 1:
        msg.append('Email está com formato incorreto')
     if estado_civil not in checkbox_estado_civil:
        msg.append('Estado Civil está incorreto. Dever ser casado ou solteiro.')
     if telefone.isalpha():
        msg.append('Telefone só pode conter números')
     if escolaridade not in range(1,8):
        msg.append('Opção de escolha incorreta. Deve ser de 1 até 7')


      # Vamos gerar uma Pessoa
     print(msg)
     if len(msg) < 1:
        C = Cliente(nome, dt_nasc, cpf, endereco, telefone, escolaridade, estado_civil, email)
        print(C.crud_incluir())
     else:
        "/n".join(msg)



   elif option == 2:
      CPF = input('Digite o CPF do usuário que deseja atualizar: ')
      client_atualizar = None

      for i in dados:
          if i.get('cpf') == CPF:
              print('Cliente a ser atualizado é: \n')
              for key,value in i.items():
                  print(f'{key}:{value}')

          break


      print('Digite a chave e o valor a ser alterado \n')
      chave = input('Qual a Chave padrão?')
      valor = input('Qual Valor a ser alterado?')
      #adicionar na classe o novo cliente atualizado
      registro = dict()
      registro[chave] = valor
      C.crud_atualizar(registro, CPF)

   elif option == 3:
      cpf = input('Digite o CPF do usuário que deseja criar uma conta: ')
      tipo = int(input('Qual tipo de conta:\n [1] - Corrente\n [2] - Poupança\n'))
      C.gerar_conta()
      C.tipo = tipo

      registro = dict()
      registro['conta'] = C.conta
      registro['tipo'] = C.tipo

      print(C.incluir_conta(registro, cpf))



   elif option == 4:
      cpf = input('Digite o CPF do usuário que deseja excluir: ')
      C.crud_excluir(cpf)



   elif option == 5:
      cpf = input('Digite o CPF do usuário que deseja exibir: ')
      dado = C.crud_exibir(cpf)
      print(C)

   else:
      print('\nOpção inválida. Digite uma opção de 1 a 6\n')