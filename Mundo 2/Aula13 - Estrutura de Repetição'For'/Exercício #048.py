# Exercício 048 - Somar os valores ímpares múltiplos de 3 no intervalo de 1 a 500
s = 0
count = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += 1
        s += c
print('A soma dos {} valores no intervalo é {}' .format(count, s))