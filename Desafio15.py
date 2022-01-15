'''Escreva um programa que pergunte a quantidade de Km percorridos por um
carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
R$0,15 por Km rodado.'''
k = int(input("Quantos km's foram percorridos: "))
d = int(input("Quantos dias você ficou com o carro: "))
v_pagar = k * 0.15 + d * 60

print(f"Você percorreu {k}Km's e ficou com o carro por {d} dias e terá de pagar o total de R$.{v_pagar:.2f} .")
