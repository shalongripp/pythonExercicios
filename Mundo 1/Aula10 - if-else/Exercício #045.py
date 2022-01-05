# Exercício 045 - Faça o computador jogar um Jokenpô com vc (Pedra-Papel-Tesoura)

from random import choice, randint
from time import sleep
print('[1] - Pedra\n[2] - Papel\n[3] - Tesoura')
print('-='* 11)
n = int(input('Qual é sua jogada? '))
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO!!!')

c = randint(1, 3)

if n == 1:
  u = 'Pedra'
elif n == 2:
  u = 'Papel'
elif n == 3:
  u = 'Tesoura'

if c == 1:
  t = 'Pedra'
elif c == 2:
  t = 'Papel'
elif c == 3:
  t = 'Tesoura'
  # Empate
if n == c:
  print('-=' * 11)
  print('EMPATE')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
  # Quando ganho
elif n == 1 and c == 3:
  print('-=' * 11)
  print('GANHOU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
elif n == 2 and c == 1:
  print('-=' * 11)
  print('GANHOU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
elif n == 3 and c == 2:
  print('-=' * 11)
  print('GANHOU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
  # Quando perco
elif n == 1 and c == 2:
  print('-=' * 11)
  print('PERDEU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
elif n == 2 and c == 3:
  print('-=' * 11)
  print('PERDEU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
elif n == 3 and c == 1:
  print('-=' * 11)
  print('PERDEU!')
  print('Você jogou {} e o computador jogou {}' .format(u, t))
