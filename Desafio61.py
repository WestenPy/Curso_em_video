#Refaça o desafio 51, lendo o primeiro termo e a razãode uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura
#while.
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
c = 0
while c <= 9:
    print('{}-> '.format(termo), end='')
    termo += razão
    c += 1
print('Fim')
