
# Exercício 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = cont = soma = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    media = soma/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor  = n
    resposta = str(input('Deseja continuar [S/N}? ')).upper().strip()[0]

print(f'A média é {media:.2f}, {maior} é o maior e {menor} é o menor') # FStrings - sintaxe mais recente