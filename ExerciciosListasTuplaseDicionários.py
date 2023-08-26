# 1."Faça um Programa que peça as quatro notas de 10 alunos, # 
#calcule e armazene numa lista a média de cada aluno, #
#imprima o número de alunos com média maior ou igual a 7.0. #

listaNotas = []
notasAluno = []
print ('Notas dos Alunos')
for i in range(10):
      media = 0
      notasAluno = []

      print ('Aluno: ' + str(i + 1))
      for j in range(4):
          notasAluno.append(float(input('Nota: ' + str(j+1) + '\n')))
          media += notasAluno[j]

      print (media)
      media = media/4
      listaNotas.append(media)

print (listaNotas)

print(f"\n{media} alunos tiveram média maior ou igual a 7.0")

# 2.Programa nome ao contrário em maiúsculas. #
# Faça um programa que permita ao usuário digitar o seu nome #
#e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. #
#Dica:lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.# 

print('Digite seu nome com letras maiúsculas ou minúsculas.')
nome = input('Digite seu nome: ').upper()
invNome = nome[::-1]#
print('{} ---> {}'.format(nome, invNome))

#3.Escreva um programa em Python que onde todos os valores em um dicionário são emitidos.
#Se sim, imprima True. Caso contrário, imprima Falso.  

contatos_lista = [('Mario', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]
for item in contatos_lista:
   print(contatos_lista) 

# "Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
# As perguntas são: ""Telefonou para a vítima?"" ""Esteve no local do crime?"" ""Mora perto da vítima?"" 
# ""Devia para a vítima?"" "Já trabalhou com a vítima?" "O programa deve no final emitir uma classificação 
# sobre a participação da pessoa no crime.Se a pessoa responder positivamente a 2 questões ela deve ser 
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". 
# Caso contrário, ele será classificado como ""Inocente""

contador = 0

print("Responda S para sim ou N para não\n")
resposta = input("Você telefonou para vítima no dia do crime?\n")
if resposta.lower() == 's':
    contador += 1
resposta = input("Esteve no local no dia do crime?\n")
if resposta.lower() == 's':
    contador += 1
resposta = input("Mora perto da vítima?\n")
if resposta.lower() == 's':
    contador += 1
resposta = input("Você devia algum dinheiro ou favor a vítima?\n")
if resposta.lower() == 's':
    contador += 1
resposta = input("Já trabalhou para vítima?\n")
if resposta.lower() == 's':
    contador += 1
del resposta
if contador < 2:
   print("INOCENTE")
elif contador == 2:
   print("SUSPEITO")
elif contador < 5:
   print("CÚMPLICE")
else:
   print("ASSASINO")
