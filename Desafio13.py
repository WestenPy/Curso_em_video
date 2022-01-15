'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.'''
def lin(n):
    print('-='* n)


n = str(input('Funcionário: '))
s = float(input('Sálario R$'))
p = s * 15/100
novosal = s + p
lin(30)
print(f'O funcionário {n} recebe um salário de R${s:.2f}')
print(f'Recebeu um aumento de 15%, igual a R${p:.2f}')
print(f'O seu novo salário é de R${novosal:.2f}')
lin(30)
