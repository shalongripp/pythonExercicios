# Exercício 038 - Ler 2 números inteiros e compará-los mostrando: o primeiro é maior;
# o segundo é maior; não existe maior, são iguais.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
if n1 > n2:
  print('O primeiro é maior')
elif n2 > n1:
  print('O segundo é maior')
else:
  print('Não existe maior, são iguais')