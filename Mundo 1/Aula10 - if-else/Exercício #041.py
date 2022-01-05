# Exercício 041 - Ler ano de nascimento de um atleta e classificar sua categoria.
# Até 9 anos - Mirim; até 14 - Infantil; até 19 anos - Júnior; até 20 anos - Sênior; acima - Master.

from datetime import date
a = int(input('Ano de Nascimento: '))
atual = date.today().year
c = atual - a
print('O atleta tem {} anos' .format(c))
if c <= 9:
  print('Categoria: Mirim')
elif 9 < c <=14:
  print('Categoria: Infantil')
elif 14 < c <= 19:
  print('Categoria: Júnior')
elif 19 < c <= 20:
  print('Categoria: Sênior')
elif c > 20:
  print('Categoria: Master')