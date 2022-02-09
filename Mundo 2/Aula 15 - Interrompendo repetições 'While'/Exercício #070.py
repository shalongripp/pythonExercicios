
soma = contMil = cont = barato = 0
produtoBarato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    cont += 1
    if preco > 1000:
        contMil += 1
    if cont == 1:                   # Esse bloco pode ser simplificado ***
        barato = preco
        produtoBarato = produto
    else:
        if preco < barato:
            barato = preco
            produtoBarato = produto
    soma += preco
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    print('='*25)
    if continua == 'N':
        break
print(f'Valor Total da Compra: {soma:.2f}')
print(f'Qtde Produtos acima de R$ 1.000,00: {contMil}')
print(f'Produto mais barato foi {produtoBarato} e custou R$ {barato:.2f}')


'''  ***  if cont == 1 or preco < barato
          barato = preco
          produtoBarato = produto
'''
