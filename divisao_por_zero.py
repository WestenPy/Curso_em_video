def retorno_erro():
  while True:
    print('\nDigite dois números para obter o valor da razão.')
    print('Digite 999 para sair')
    try:
      primeiro = int(input('\nEntre com o primeiro número: '))
      if primeiro == 999:
        print('Fim do programa')
        break
    except ValueError:
      print('Entre apenas com valores numéricos.')
      retorno_erro()  
    try:
      segundo = int(input('\nEntre com o segundo número: '))
    except ValueError:
      print('Entre apenas com valores numéricos.')
      retorno_erro()
    try:
      razao = primeiro / segundo
    except ZeroDivisionError:
      print('\nNão pode ser dividido por zero')
      print('Tente novamente')      
    else:
      print(f'\n{razao}')