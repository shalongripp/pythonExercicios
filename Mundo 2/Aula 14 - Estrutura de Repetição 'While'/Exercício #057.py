''' Exercício 057 -  Ler o sexo de uma pessoa, mas só aceite 'M' ou 'F'. Caso esteja errado peça a digitação até o valor
correto. '''

sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0].strip() # [0] pega apenas a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).upper()[0].strip()

if sexo == 'M':
    print('A pessoa é do sexo masculino')
if sexo == 'F':
    print('A pessoa é do sexo feminino')
print('FIM')
