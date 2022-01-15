'''Escreva um programa que converta uma temperatura digitada em °C
e converta para °F.'''
t = float(input('Informe a temperatura em °C: '))
f = ((9*t)/5) + 32
print(f'A temperatura de {t}°C corresponde a {f:.2f}°F .')
