# Exercício 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite o número: '))
c = n
f = 1
print('Calculando {}! = ' .format(n), end='')
while c > 0:
   print('{}' .format(c), end=' ')
   print(' x ' if c > 1 else ' = ', end=' ')
   f *= c
   c -= 1
print('{}' .format(f))