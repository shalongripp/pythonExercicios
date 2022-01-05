# Exercício 033 - Ler 3 números e indicar qual é o maior e o menor
n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))
menor = n1
if n1 > n2 < n3:
  menor = n2
if n2 > n3 < n1:
  menor = n3

maior = n1
if n1 < n2 > n3:
  maior = n2
if n2 < n3 > n1:
  maior = n3

print('Maior = {}' .format(maior))
print('Menor = {}' .format(menor))