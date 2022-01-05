# Exercício 059 - Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
p = 0

while p!= 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
    p = int(input('>>> Escolha o menu de operações: '))
    if p == 1:
        print('{} + {} = {}' .format(n1, n2, n1 + n2))
    elif p == 2:
        print('{} X {} = {}' .format(n1, n2, n1 * n2))
    elif p == 3:
        if n1 > n2:
            print('{} > {}' .format(n1, n2))
        elif n2 > n1:
            print('{} > {}'. format(n2, n1))
        else:
            print('{} = {} ' .format(n1, n2))
    elif p == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif p == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente')
    print('=-=' *15)
    sleep(2)
print('Fim do Programa')




