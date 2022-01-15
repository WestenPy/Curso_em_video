'''Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos dolares ela pode comprar.'''
n = float(input('Quanto você tem na carteira? R$ '))
d = n / 5.50
print(f'Você tem R${n:.2f} na carteira, o que dá para comprar exatamente US${d:.2f}.')
