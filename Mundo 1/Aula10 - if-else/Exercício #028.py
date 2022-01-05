# Exercício 028 - Faça o computador pensar em um número de 0 a 5 para o usuário tentar descobrir.
# O programa vai escrever na tela se o usuário venceu ou perdeu.

from random import randint
n = int(input('Escolha um número de 0 a 5: '))
r = randint(0, 5)
if n == r:
  print('O número sorteado foi {}' .format(r))
  print('Vc acertou!')
else:
  print('O número sorteado foi {}' .format(r))
  print('vc errou!')