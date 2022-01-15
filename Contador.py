def contador(i=0, f=1, p=1):
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(10,0,-2)
