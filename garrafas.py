
'''n = 99
p = 'garrafas'

while n > 0:
    if n == 1:
        p = 'garrafa'
    print(f'{n} {p} de cerveja no muro!')
    print(f'{n} {p} no muro!')
    print('Se uma garrafa cair no chão')
    print('Quantas restarão?')
    n -= 1

print('Fim da canção!')'''

p = 'garrafas'

for c in range(99, 0, -1):
    if c == 1:
        p = 'garrafa'
    print(f'{c} {p} de cerveja no muro!')
    print(f'{c} {p} no muro!')
    print('Se uma garrafa cair no chão')
    print('Quantas restarão?')

print('Fim da canção!')


