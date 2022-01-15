times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atletico', 'Botafogo', 'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico-GO')
print('-='*30)
print(f'Lista de times do Brasileirão:{times}')
print('-='*30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética:{sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição ')
