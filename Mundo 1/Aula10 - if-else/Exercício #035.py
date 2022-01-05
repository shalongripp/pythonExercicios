# Exercício 035 - Ler comprimento de 3 retas e dizer se ela podem ou não formar um triângulo

l1 = float(input('L1: '))
l2 = float(input('L2: '))
l3 = float(input('L3: '))
'''
if abs(l2 - l3) < l1 < (l2 + l3) or abs(l1 - l3) < l2 < (l1 + l3) or abs(l1 - l2) < l3 < (l1 + l2):
  print('L1, L2 e L3 podem formar um triângulo')
else:
  print('L1, L2 E L3 não podem formar um triângulo')
'''
if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
    print('L1, L2 e L3 podem formar um triângulo')
else:
    print('L1, L2 E L3 não podem formar um triângulo')
