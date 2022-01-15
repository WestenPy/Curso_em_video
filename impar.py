from datetime import datetime
from random import randint, randrange
from time import sleep
ímpares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
for i in range(5):
    neste_minuto = datetime.today().minute

    if neste_minuto in ímpares:
        print('Este minuto parece um pouco ímpar!')
    else:
        print('não é um minuto ímpar')
    n = randint(0, 60)
    sleep(1)


