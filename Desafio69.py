#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o
#usuário quer ou não continuar. No final mostre:
#A)Quantas pessoas tem mais de 18 anos.
#B)Quantos homens foram cadastrados.
#C)Quantas mulheres tem menos de 70 anos.
from time import sleep

h = m = i = 0
while True:
    nome = input('Qual o seu nome? ')
    sexo = input('Qual o seu sexo?[M/F] ').upper().strip()[0]
    if 'M'in sexo:
        h += 1
    elif 'F' in sexo:
        if idade < 20:
            m += 1
    else:
        print('Informação incorreta, tente novamente!')
    idade = int(input('Qual a sua idade? '))
    if idade > 18:
        i += 1
    print('Você deseja cadastrar mais uma pessoa?')
    per = int(input('1- SIM \n2- NÃO '))
    if per == 1:
        print('Cadastrar nova pessoa: ')
    elif per == 2:
        print('Processando dados...')
        break
    else:
        print('Opção inválida, tente novamente!')
sleep(2)
print(f'Foram cadastrados {i} pessoas maiores de 18 anos, \n{h} homens \n{m} mulheres com idades menores de 70 anos.')
