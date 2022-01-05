# Exercício 052 - Ler um número inteiro e dizer se é ou não primo.

count = 0
num = int(input('Digite um número: '))
print('Números primos destacados em vermelho:')
for c in range(1, num + 1):
    if num % c == 0:
        count += 1
        print('\33[1;31m', end = ' ')
    else:
        print('\33[0;34m', end = ' ')
    print(c, end = ' ')
print('\n\33[0;37mO número {} foi divisível {} vezes'.format(num,count))
if count == 2:
    print('{} é primo'.format(num))
else:
    print('{} não é primo'.format(num))