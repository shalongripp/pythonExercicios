# Exercício 055 - Ler o peso de 5 pessoas e mostrar o maior e o menor peso.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '. format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior peso é {} e menor peso é {}' .format(maior, menor))
