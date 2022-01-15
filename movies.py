movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
          ['Graham Chapman', ['Michael Palin', 'John Cleese',
                              'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

def print_lol(lista):
    for cada_item in lista:
        if isinstance(cada_item, list):
            print_lol(cada_item)
        else:
            print(cada_item)

print_lol(movies)


