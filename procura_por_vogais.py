def procure_vogais(palavra):
   """
    ->retorna quaisquer vogais encontradas em uma palavra fornecida
    :param palavra: uma string onde será procurada as vogais
    :return: retorna um conjunto set()"""
   vogais = set('aeiou')
   return vogais.intersection(set(palavra))


print(procure_vogais('bumbinha'))

print(help(procure_vogais))
