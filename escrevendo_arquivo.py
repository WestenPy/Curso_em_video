with open('arquivo_teste.txt', 'w', encoding='utf-8')as arq:
    arq.write('Eu to com fome\n')
    arq.write('Número 2\n')
with open('arquivo_teste.txt', 'a', encoding='utf-8')as arq:
    arq.write('não estou nem aí para esta terceira linha!\n')

with open('arquivo_teste.txt', 'r', encoding='utf-8')as arq:
    print(arq.read())
