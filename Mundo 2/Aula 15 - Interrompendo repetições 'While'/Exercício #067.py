while True:
    n = int(input('Tabuada de qual valor: '))
    if n < 0:
        break
    cont = 0
    while cont <= 9:
        cont += 1
        print(f'{n} X {cont} = {n*cont}')

