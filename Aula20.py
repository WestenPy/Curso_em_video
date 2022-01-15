def dobra(lt):
    pos = 0
    while pos < len(lt):
        lt[pos] *= 2
        pos += 1


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


valores = [6, 9, 3, 2, 5, 10]
dobra(valores)
print(valores)
print()
soma(5, 2)
soma(2, 9, 4)