# 1. O banco Banco Delas é um banco moderno e eficiente,com vantagens exclusivas para clientes mulheres.
#Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
#● Cada conta corrente pode ter um ou mais clientes como
#titular.
#● O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
#● A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#● Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito,
#aumentaremos o saldo.
#● Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas
#podem sacar valores que deixam a sua conta com valor negativo até renda_mensal.
#● Clientes homens por enquanto não têm direito a cheque especial.
#Para modelar seu sistema, utilize obrigatoriamente os conceitos
#"classe", "herança", "propriedades", "encapsulamento" e "classe
#abstrata"

#def exibir_menu():
    #print('''Escolha uma opção:

    #1. Cadastrar um cliente
    #2. Listar clientes cadastrados
    #3. Encontrar informações de um cliente
    #''')

#def cadastrar(clientes):
    #identificador = input('Id: ')
    #nome = input('Nome: ')
    #telefone = int(input('Telefone: '))
    #salario = int(input('Renda mensal:'))
    #clientes.append((identificador, nome, telefone, salario))

#def listar(clientes):
    #for clientes in clientes:
        #identificador, nome, telefone, salario = clientes
        #print(f'Nome: {nome}, telefone: {telefone}, id: {identificador}, salario: {salario}')

#def buscar(clientes):
    #identificador_opcao = input('Id? ')
    #for clientes in clientes:
        #identificador, nome, telefone, salario = clientes
        #if identificador == identificador_opcao:
            #print(f'Nome: {nome}, telefone: {telefone}, id: {identificador}, salario: {salario}')
            #break
    #else:
        #print(f'Cliente com id {identificador_opcao} não encontrada')

#def main():
    #clientes = []

    #while True:
        #exibir_menu()
        #opcao = int(input('Opção? '))
        #if opcao == 1:
            #cadastrar(clientes)
        #elif opcao == 2:
            #listar(clientes)
        #elif opcao == 3:
            #buscar(clientes)
        #else:
            #print('Opção inválida')

#id = input("Digite o id da(o) cliente desejada: ")
#for buscar in listar:
    #if id in buscar:
        #try:
            #print("Nome: %s - Idade: %s - ID: %s - telefone: %s - salario: %s"%(buscar[1],buscar[2],buscar[0]))
        #except:
            #print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID, telefone, salario")

# Solução - Aula da Instrutora Clarisse 

from abc import ABC, abstractmethod


class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self._primeiro_nome = nome.split(" ") [0]
        self._ultimo_nome = nome.split(" ") [-1]
        self._telefone = telefone
        self._renda_mensal = renda_mensal

@property
def nome(self):
    return self._nome

@nome.setter
def nome(self, novo_primeiro_nome, novo_ultimo_nome):
    if type(novo_nome) != str:
        raise TypeError("Tipo da variável deve ser str")
    self._nome = novo_nome

@property
def telefone(self):
    return self.telefone

@telefone.setter
def telefone(self, novo_tel):
    if type(novo_tel) !=str:
        raise TypeError("Tipo da variável deve ser str")
    self._telefone = novo_tel

@property
def renda_mensal(self):
    return self.__renda_mensal

@abstractmethod
def tem_chequeespecial(self):
    return False

class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self.__titulares.append(titular)

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__operacoes.append("Depósito de R$ {valor:.2f}")

    def sacar(self, valor: float):
        titular = self.__titulares[0]
        if titular.tem_cheque_especial() == False:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__operacoes.apped(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
        else:
            if valor <= self.__saldo or (self.saldo - valor) <= titular.renda_mensal:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo Insuficiente")
@property
def saldo(self):
    return self.__saldo  
    
cliente_mulher = Cliente("Vitoria Macedo", "747474", 30000.0)
#cliente_homem = Cliente("Daniel", "9798798789", 1000.0)

conta1 = ContaCorrente(cliente_mulher)
#conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
#print(conta2.saldo)
print()

valor_saque = input("Quanto você quer sacar?")
valor_saque = float(valor_saque)

try:
    conta1.sacar(valor_saque)    
except ValueError as e:
    print(f"Erro durante a execução: {e}")
print(conta1.operacoes)

exit()
conta1.depositar(5000.0)



