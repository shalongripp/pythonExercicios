# Exercício 054 - Ler data de nascimento de 7 pessoas e dizer quantas são de maior idade(21 anos) e
# quantas são menores

from datetime import datetime, date
atual = date.today().year
countMinor = 0
countMajor = 0
for c in range(1, 8):
    dataNascimento = int(input('Em que ano a {}ª pessoa nasceu? ' .format(c)))
    data = atual - dataNascimento
    if data >= 21:
        countMajor += 1
    else:
        countMinor += 1
print('{} pessoas são maiores de idade e {} são menores' .format(countMajor, countMinor))


