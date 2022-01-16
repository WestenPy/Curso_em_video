#Desafio019 Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

a1 = input('Escreva o seu nome: ')
a2 = input('Escreva o seu nome: ')
a3 = input('Escreva o seu nome: ')
a4 = input('Escreva o seu nome: ')

lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print(f'O nome escolhido para apagar o quadro foi de {sorteio}')
