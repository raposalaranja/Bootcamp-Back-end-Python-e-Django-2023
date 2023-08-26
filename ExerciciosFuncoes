#1.Faça um programa, com uma função que necessite de três argumentos,
#e que forneça a soma desses três argumentos.#

def soma(x,y,z):
    return (x + y + z)

def opcao():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro numero: '))

    print('Soma: ', soma(x,y,z))

    while True:
      opcao()

#2.Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.
#  Por exemplo: 127->721.

def reverso(n):
    return str(n[::-1])

n = str(input('Digite o número: ')).strip()
print(f'Reverso: {reverso(n)}')

#3. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius
#  para Fahrenheit ou vice- versa. Para cada opção, crie uma função. 
# Crie uma terceira, que é um menu para o usuário escolher a opção desejada, 
# onde esse menu chama a função de conversão correta.#

def C_para_F(C):
    F = (C*9/5) + 32
    return F

def F_para_C(F):
    C = (F-32)*5/9
    return C


def menu():
    while True:
        op = int(input('1. Celsius para Farenheit: \n' +
                       '2. Farenheit para Celsius: '))

        if op==1:
            C=int( input('Celsius: ') )
            print('Conversão de: ', C_para_F(C),' para graus Farenheit\n')
        elif op==2:
            F=int( input('Farenheit: ') )
            print('Conversão de: ', F_para_C(F),' para graus Celsius\n')
        else:
            print('Opção inválida')
menu()