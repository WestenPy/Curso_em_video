from random import randint
def sorteia():
    lista = []
    for i in range(5):
        a =randint(0, 9)
        lista.append(a)
    print(lista)
    return lista
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i

    print(f'A soma de todos os números pares é igual a {soma}')


somaPar(sorteia())
