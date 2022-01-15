'''pessoas = {'nome': 'wesley', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'José'
del pessoas['sexo']
pessoas['peso'] = 65.9
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
#brasil = []
#estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil)

estado = dict()
brasil = list()
for cada_item in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())# no dicionãrio não podemos usar o formato [:] que se usa na lista, temos que usar o metodo interno copy()
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
