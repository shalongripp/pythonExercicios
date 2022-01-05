# Exercício 030 - Ler um número e mostrar se ele é par ou ímpar
n = int(input('Digite um número: '))
if n%2==0:
  print('{} é Par' .format(n))
else:
  print('{} é Ímpar' .format(n))