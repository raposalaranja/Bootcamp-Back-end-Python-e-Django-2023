# 1.Faça um Programa que peça dois números e imprima o maior deles. #

num1 = int(input('Digite o primeiro numero: '))

num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print(num1)
else:
    print(num2)


#2.Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
#Imprima a mensagem "BomDia!", "BoaTarde!" ou "BoaNoite!" ou "ValorInválido!",
#conforme o caso#

turno = input(
    "Digite seu turno, M - matutino, V - vespertino, N - noturno: ").upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

# 3.Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.#

nota=float(input("Digite um numero entre 0 e 10: "))
while (nota>10) or (nota<0):
	nota=float(input("O numero digitado tem que estar entre 0 e 10.\nTente novamente:"))


