#Desafio020 O mesmo professo do desafio anterior quer sortear a ordem de apresentação
#dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e 
#mostre ordem sorteada.

from random import sample

lista = []
for cada in range(4):
	lista.append(input('Digite o seu nome: '))

ordem = sample(lista, 4)

print('A ordem de apresentação será: ')
for c in ordem:
	print(c)
