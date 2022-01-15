todos = open('todos.txt', 'a')
print('Put the trash.', file=todos)
print('Feed the cat.', file=todos)
print('File tax return.', file=todos)
todos.close()


tasks = open('todos.txt')
for c in tasks:
    print(c, end='')
tasks.close()
