# Exercício 056 - Ler nome, idade e sexo de 4 pessoas e mostrar a média de idade, o nome do homem mais velho,
# quantas mulheres tem menos de 20 anos

somaIdade = 0
idade = 0
maiorIdade = 0
nomeVelho = ''
count = 0
for p in range(1, 5):
    print('{}ª pessoa'. format(p))
    nome = str(input('Nome: '.format(p))).strip()
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo [M/F]: '.format(p))).upper()
    somaIdade += idade
    print('-' * 30)

    if p == 1 and sexo == 'M':
        maiorIdade = idade
        nomeVelho = nome
    else:
        if sexo == 'M' and idade > maiorIdade:
            maiorIdade = idade
            nomeVelho = nome

    if sexo == 'F' and idade < 20:
        count += 1


print('O homem mais velho é {}' .format(nomeVelho))
medIdade = somaIdade / p
print(' A idade média entre as pessoas é de {} anos' .format(medIdade))
print('{} mulher(es) tem menos de 20 anos' .format(count))