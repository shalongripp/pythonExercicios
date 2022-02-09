
from random import randint

resultado = cont = 0
while True:
    num = int(input('Digite um número [0-10]: '))
    computador = randint(0, 10)
    soma = num + computador
    ParImpar = ' '
    while ParImpar not in 'PI':
        ParImpar = str(input('Vc quer par ou ímpar? ')).upper().strip()[0]
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if ParImpar == resultado:
        cont += 1
        print(f'O computador jogou {computador} e vc jogou {num}. Resultado é {soma}')
        print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
        print('='*20)
        print('Você venceu!!!')
        print('Vamos jogar novamente!!!')
        print('='*20)
    else:
        break
print(f'O computador jogou {computador} e vc jogou {num}. Resultado é {soma}')
print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
print('Você perdeu!!!')
print(f'GAME OVER!!! Você conseguiu vencer {cont} vez(es)')


