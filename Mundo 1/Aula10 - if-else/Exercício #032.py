# Exercício 032 - Digitar um ano e mostrar se ele é bissexto

ano = int(input('Digite o ano: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
  print('{} é bissexto' .format(ano))
else:
  print('{} não é bissexto' .format(ano))