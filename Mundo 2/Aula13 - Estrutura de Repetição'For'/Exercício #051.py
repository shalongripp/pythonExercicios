# Exercício 051 - Ler primeiro termo e a razão de uma PA. Mostrar os 10 primeiros termos da progressão.

# an = a1 + (n - 1).r

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('os 10 primeiros termos da PA são: ')
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end =' ')