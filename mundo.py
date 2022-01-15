import main
lista = ['casa', 'arvore', 'comida', ['suco', 'pão', ['agua']]]
'''Este é o módulo "mundo.py", e fornece uma função chamada fun()
que imprime listas que podem ou não incluir listas aninhadas.'''
def fun(a_lista):
    '''Esta função requer um argumento posicional chamado "a_lista", que é qualquer lista PYTHON
    (de possiveis listas aninhadas). Cada item de dados na lista fornecida é (recursivamente)
    impresso na tela em sua própria linha.'''
    for cada_item in a_lista:
        if isinstance(cada_item, list):
            fun(cada_item)
        else:
            print(cada_item)

fun(lista)



