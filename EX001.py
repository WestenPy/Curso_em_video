#desafio 1
#Construa um algoritmo que leia um número inteiro e exiba a informação se este número é ou não
#divisivel por 5. ( dica: utilize o operador resto de divisão)
print('-=' * 23)
print('Descubra se o número é ou não divisível por 5 !')
print('-=' * 23)
n1 = int(input('Digite um número: '))
r = n1 % 5
if r == 0:
    print('O número {} é divisível por 5!'.format(n1))
else:
    print('O número {} não é divisível por 5!'.format(n1))

