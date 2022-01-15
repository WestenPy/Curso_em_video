'''Escreva um programa que leia um valor em metros e o exiba convertido
em centimetros e milimetros.'''

m = int(input('Escreva um valor para ser convertido: '))

cm = m * 100
mm = m * 1000

print(f'Você digitou o valor de {m} metros \nque convertito para centimetros equivale a {cm}cm \ne convertido para milimetros é igual a {mm}mm.')