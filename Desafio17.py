'''Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa'''
from math import sqrt
ca = float(input('Informe o valor do cateto adjacente: '))
co = float(input('Informe o valor do cateto oposto: '))
hi = sqrt(ca**2 + co**2)
print(f'O valor da hipotenusa desse triângulo é de {hi :.2f}')

