'''Faça um programa que leia a largura e a altura de uma parede em metros
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta uma área de 2 metros quadrados.'''

l = float(input('Entre com a largura da parede: '))
h = float(input('Entre com a altura da parede '))
area = l * h
t = area / 2
print('-=' * 30)
print(f'A área da sua parede é {area:.2f}m². \nA quantidade de tinta para pintá-la é de {t:.2f} litros')