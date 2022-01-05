# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

#  an = a1+(n-1) x r

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
print('Os 10 primeiros termos de uma PA são: ')
count = 1
termo = a1
while count <= 10:
    print('{} -> ' .format(termo), end='')
    termo += r
    count += 1
print('FIM')