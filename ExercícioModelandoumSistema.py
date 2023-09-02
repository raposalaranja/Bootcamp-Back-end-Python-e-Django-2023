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

def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar um cliente
    2. Listar clientes cadastrados
    3. Encontrar informações de um cliente
    ''')

def cadastrar(clientes):
    identificador = input('Id: ')
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    salario = int(input('Renda mensal:'))
    clientes.append((identificador, nome, telefone, salario))

def listar(clientes):
    for clientes in clientes:
        identificador, nome, telefone, salario = clientes
        print(f'Nome: {nome}, telefone: {telefone}, id: {identificador}, salario: {salario}')

def buscar(clientes):
    identificador_opcao = input('Id? ')
    for clientes in clientes:
        identificador, nome, telefone, salario = clientes
        if identificador == identificador_opcao:
            print(f'Nome: {nome}, telefone: {telefone}, id: {identificador}, salario: {salario}')
            break
    else:
        print(f'Cliente com id {identificador_opcao} não encontrada')

def main():
    clientes = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(clientes)
        elif opcao == 2:
            listar(clientes)
        elif opcao == 3:
            buscar(clientes)
        else:
            print('Opção inválida')

id = input("Digite o id da(o) cliente desejada: ")
for buscar in listar:
    if id in buscar:
        try:
            print("Nome: %s - Idade: %s - ID: %s - telefone: %s - salario: %s"%(buscar[1],buscar[2],buscar[0]))
        except:
            print("Essa pessoa não possui algum dos valores a seguir: Nome, Idade, ID, telefone, salario")