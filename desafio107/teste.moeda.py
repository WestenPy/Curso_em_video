import moeda

p = float(input('Informe um valor R$ '))
print(f'O dobro do valor R${p:.2f} é igual a R${moeda.dobro(p):.2f}')
print(f'A metade do valor R${p:.2f} é igual a R${moeda.metade(p):.2f}')
t = int(input('Informe a taxa: '))
print(f'O valor R${p:.2f} adicionado com a taxa de {t} % fica igual a R${moeda.aumentar(p, t):.2f}')
print(f'O valor R${p:.2f} diminuido com a taxa de {t} % fica igual a R${moeda.diminuir(p, t):.2f}')
