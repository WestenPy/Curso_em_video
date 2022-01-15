#Faça um programa que mostre a tabuada de vários números, um de cada vez,
#para cada valor digitado pelo usuário. O programa será interrompido quando
#o número solicitado for negativo.
while True:
    print('-='*25)
    n = int(input('Digite um número para saber a sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        t = c * n
        print(f'{c} X {n} = {t}')
print('FIM DO PROGRAMA')
