#Faça um programa que jogue par ou impar com o computador.
#O jogo só será interrompido quando o jogador PERDER,
#mostrando o total de vitorias consecutivas que ele
#conquistou no final do jogo.
from random import randint
cont = 0
print('Jogo do par ou impar!')

while True:
    print('-='*20)
    jog = int(input('Digite um número entre 1 e 10: '))
    esc = int(input('Digite 1 para "par" e 2 para "Impar": '))
    comp = randint(1, 11)
    print(f'Voce jogou {jog} e o computador jogou {comp}')
    res = (jog + comp) % 2
    cont += 1
    if esc == 1 and res == 0:
        print('Parabéns você venceu!!!')
    elif esc == 2 and res == 1:
        print('Parabéns você venceu!!!')
    else:
        break
print(f'Você foi derrotado depois de {cont} tentativas.')


