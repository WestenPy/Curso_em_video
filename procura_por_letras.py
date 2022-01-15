def procura_por_letras(frase, letra='aeiou'):
    """
    -> faz uma procura por um conjunto de letras especificadas
    :param frase: solicita uma frase (string) a partir do qual será feita a busca
    :param letra: conjunto de letras (string) que serão procuradas na frase
    :return: retorna um conjunto set()
    """
    return set(letra).intersection(set(frase))


print(procura_por_letras('Pão de doce'))
