# Exercício 042 - Refazer o 035 mostrando o tipo de triângulo: Equilátero, Isósceles e Escaleno.

l1 = float(input('L1: '))
l2 = float(input('L2: '))
l3 = float(input('L3: '))
if abs(l2 - l3) < l1 < (l2 + l3) or abs(l1 - l3) < l2 < (l1 + l3) or abs(l1 - l2) < l3 < (l1 + l2):
  print('L1, L2 e L3 PODEM FORMAR um triângulo')
  if (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
    print('Triângulo Isósceles')
  elif l1 == l2 == l3:
    print('Triângulo Equilátero')
  elif l1 != l2 != l3:
    print('Triângulo Escaleno')
else:
  print('L1, L2 E L3 NÃO PODEM FORMAR um triângulo')