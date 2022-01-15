'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações sobre ele.'''
algo = input('Digite algo: ')
print(f'Você digitou {algo} o seu tipo primitivo é {type(algo)}')
print(f'Você digitou algo numérico? {algo.isnumeric()}')
