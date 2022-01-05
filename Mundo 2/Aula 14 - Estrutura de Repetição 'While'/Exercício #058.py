''' Exercício 058 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10
Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer '''

from random import randint
print('Sou seu computador e pensei em um número!')
n = int(input('Tente adivinhar: '))
r = randint(0, 10)
count = 0
while n != r:
    if n > r:
        print('Menos...')
    elif n < r:
        print('Mais...')
    n = int(input('Tente outra vez: '))
    count += 1
if n == r:
    print('Parabéns, eu pensei no número {} e você acertou depois de {} tentativa(s)' .format(r, count))

