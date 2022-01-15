'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
from math import sqrt
n = int(input('Digite um número:'))
dob = n * 2
tri = n * 3
raiz = sqrt(n)
print(f'O valor {n} tem o valor dobrado de {dob}, o valor triplicado de {tri} e a sua raiz quadrada é de {raiz}.')
