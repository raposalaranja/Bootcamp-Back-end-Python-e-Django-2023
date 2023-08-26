# 1.Faça um Programa que peça um número e então mostre a mensagem:-> O número informado foi[número].#

numero=input("Digite o número: ")
print("O número informado foi", numero)

# 2.Faça um Programa que peça dois números e imprima a soma. #

def sum(num1, num2):
    return num1 + num2
    
print("\tSoma de dois números\n")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print ("")
print ("O resultado da soma é %d" %sum(num1, num2))

# 3.Faça um Programa que peça a temperatura em graus Celsius,transforme e mostre em graus Fahrenheit.#

def menu():
    print('Conversão de Temperaturas')
    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')

def celsius_fahrenheit():
    C = float(input('Digite a temperatura em Celsius: '))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahrenheit_celsius():
    F = float(input('Digite a temperatura em Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu()
    opcao = input('Digite o tipo de conversão a ser feita:')

    if opcao == '1':
        celsius_fahrenheit()

    if opcao == '2':
        fahrenheit_celsius()

# 4.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. #
    #Calcule e mostre o total do seu salário no referido mês.#

valor = int(input('Valor recebido por hora: '))
horas = int(input('Horas trabalhadas no mes: '))
salario = valor * horas
IRRF = (11/100.0 * salario)
print ('Imposto de renda retido na fonte: ',IRRF)
CPSS = (8/100.0 * salario)
print ('Contribuição Plano Seguridade Social: ',CPSS)
descontos = IRRF + CPSS
salarioLiquido = salario - descontos
print ('O desconto total do salario bruto(',salario,'R$)',
       'foi de',descontos,'\nO salario liquido é: ,',salarioLiquido)



