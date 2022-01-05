# Exercício 049 - Refazer o exercício 009 utilizando laço de repetição (tabuada)

f = int(input('Digite o fator da tabuada: '))
for c in range(0, 11):
   print('{} x {} = {}' .format(f, c, f*c))
