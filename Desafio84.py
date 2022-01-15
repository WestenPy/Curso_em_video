'''Desafio 84- Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
b) uma listagem com as pessoas mais pesadas
C) Uma listagem com as pessoas mais leves'''
pessoas = maior = menor = 0
lista = []
principal = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    principal.append(lista[:])
    lista.clear()
    resp = str(input('Quer continuar? [S/N] '))
    pessoas += 1
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram {principal}.')
print(f'Ao todo você cadastrou {pessoas} pessoas')
print(f'O maior peso foi de {maior} quilos. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor} quilos. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

