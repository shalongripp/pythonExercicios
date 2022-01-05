# Exercício 044 - Calcular o valor a ser pago por um produto considerando o preço normal e as condições
                # de pagamento:
                # à vista dinheiro/cheque - 10% de desconto; à vista cartão de crédito - 5% de desconto
                # em até 2 X no cartão - preço normal; 3 X ou mais no cartão - 20% de juros

v = float(input('Preço do Produto: '))
print('''Forma de Pagamento:
[1] à vista Dinheiro/Cheque
[2] à vista cartão de crédito
[3] Parcelado em 2 X
[4] Parcelado em 3 X ou mais''')
f = int(input())
if f == 1:
  print('R$ {:.2f}' .format(v * 0.90))
elif f == 2:
  print('R$ {:.2f}' .format(v * 0.95))
elif f == 3:
  print('R$ {:.2f}' .format(v))
  print('2 parcelas de R$ {:.2f}' .format(v/2))
elif f == 4:
  p = int(input('Quantidade de parcelas: '))
  if p >= 3:
    print('R$ {:.2f}' .format(v * 1.20))
    print('{} parcelas de R$ {:.2f}' .format(p,((v * 1.20)/p)))
  else:
    print('Esta opção permite apenas o mínimo de 3 parcelas')