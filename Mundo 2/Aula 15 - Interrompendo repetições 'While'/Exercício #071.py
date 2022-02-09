
contUm = contDez = contVinte = contCinquenta  = resto = 0
valor = float(input('Qual valor requisitado? R$ '))


if valor < 10:
    qtdCedula = valor / 1
    print(f'Total de {qtdCedula} cédulas de R$ 1,00')

elif valor >= 10 and valor < 20:
    qtdCedula = valor // 10
    resto = valor % 10
    print(f'Total de {qtdCedula} notas de R$ 10,00')
    print(f'Total de {resto} notas de R$ 1,00')
elif 20 <= valor < 50:
    qtdCedula = valor // 20
    resto = valor % 20
    print(f'Total de {qtdCedula} notas de R$ 20,00')
    print(f'Total de {resto} notas de R$ 1,00')
else:
    qtdCedula = valor / 50
    if valor % 50 < 10:
        resto = valor % 50
    elif 10 <= (valor % 50) < 20:
        resto = valor % 50
    elif 20 <= (valor % 50) < 50:
        resto = valor % 50
