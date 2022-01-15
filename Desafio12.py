'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.'''

p = str(input('Nome do produto: '))
v = float(input('Valor do produto R$'))
desconto = v * 5/100
vdesconto = v - desconto
print(f'Você comprou o produto {p} no valor R${v:.2f}')
print(f'Você recebeu um desconto de 5% no valor de R${desconto:.2f}')
print(f'Seu valor atualizado com desconto é de R${vdesconto:.2f}')
