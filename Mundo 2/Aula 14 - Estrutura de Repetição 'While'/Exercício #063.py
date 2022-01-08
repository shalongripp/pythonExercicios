# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci

# Fn = Fn – 1 + Fn – 2

n = int(input('quantos termos vc quer? '))
t0 = 0
t1 = 1
print('{} → {}' .format(t0, t1), end='')
cont = 3
while cont <= n:
    t2 = t0 + t1
    print(' → {}' .format(t2), end='')
    t0 = t1
    t1 = t2
    cont += 1
print(' → FIM')
