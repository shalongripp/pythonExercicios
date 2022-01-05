'''
for c in range(0, 5):
    print('oi')

for c in range(0, 5):
    print(c) # se quiser uma contagem de um até 5 -> range(0, 6)

for c in range(5, 0, -1): # -1 faz contar regressivamente de 5 à 1
    print(c)

for c in range(0, 7, 2): # alterando a iteração com o 2
    print(c)
'''
n = int(input('Digite um número: '))
for c in range(1, n):
    print(c)
'''
n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c)

i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input("Digite o passo: "))
for c in range(i, f+1, p):
    print(c)

for c in range(0, 3):
    n = int(input('Digite um número:'))
print('Fim')



s = 0
for c in range(0, 3):
    n = int(input('Digite um número:'))
    s = s + n # no Python pode ser escrito s += n
print('A soma dos números digitados é {}' .format(s))

'''
