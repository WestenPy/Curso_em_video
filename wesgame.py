from random import randint


def ataque():
    r = randint(1, 20)
    if r >= 18:
        print('DANO CRÍTICO!')
    elif r >= 8 or r < 18:
        print('DANO NORMAL!')
    elif r >= 3 or r < 8:
        print('DANO REDUZIDO!')
    else:
        print('ERRO!')


ataque()
