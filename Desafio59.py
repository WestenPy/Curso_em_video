#Desafio 59
#Crie um programa que leia dois valores e mostre um menu.
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

opcao = 0
while opcao != 5:
    print('Escolha uma opção: ')
    print('''
    [1] soma
    [2] produto
    [3] maior
    [4] novos números
    [5] sair''')
    opcao = int(input('Opção escolhida: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é igual a {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} x {} é igual a {}.'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é o número {}.'.format(n1, n2, maior))
        elif n1 == n2:
            print('Os números são iguais.')
        else:
            maior = n2
            print('O maior número entre {} e {} é o número {}.'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Escolha outra opção.')
    print('-=' * 20)
    sleep(3)
print('Fim do programa!')
