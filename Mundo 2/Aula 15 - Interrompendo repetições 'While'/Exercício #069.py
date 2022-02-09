
print('='*19)
print('CADASTRE UMA PESSOA')
print('='*19)

contMaior18 = contHomem = ContMulher = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo[M/F]: ')).upper().strip()[0]

    continuar =  ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    print('-'*30)

    if idade > 18:
        contMaior18 += 1
    if sexo == 'M':
        contHomem += 1
    if idade < 20 and sexo == 'F':
        ContMulher += 1
    if continuar == 'N':
        break
print('=' * 30)
print('FIM DO PROGRAMA')
print('=' * 30)
print(f'Total de pessoas com +18: {contMaior18}')
print(f'Total de homens: {contHomem}')
print(f'Total de mulheres com -20: {ContMulher}')

