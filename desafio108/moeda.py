def aumentar(a=0, b=0):
    return a + (a * b) / 100


def diminuir(a=0, b=0):
    return a - (a * b) / 100


def dobro(a=0):
    return a * 2


def metade(a=0):
    return a / 2

def moeda(a=0, b='R$' ):
    return f'{b}{a}'.replace('.', ',')
