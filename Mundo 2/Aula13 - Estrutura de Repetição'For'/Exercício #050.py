# Exercício 050 - Ler 6 números inteiros e mostrar a soma dos pares. Se digitar ímpar, desconsiderar.

soma = 0
for c in range(0, 6):
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        soma += n
print('A soma dos pares é {}'.format(soma))
