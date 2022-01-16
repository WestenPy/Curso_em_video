#Faça um programa que leia um ângulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians

ang = float(input('Nos diga um valor ângular: '))
seno = sin(radians(ang))
print(f'O ângulo {ang} tem o seno de {seno:.3f}')
cosseno = cos(radians(ang))
print(f'\nO ângulo {ang} tem o cosseno de {cosseno:.3f}')
tangente = tan(radians(ang))
print(f'\nO ângulo {ang} tem a tangente de {tangente:.3f}')
