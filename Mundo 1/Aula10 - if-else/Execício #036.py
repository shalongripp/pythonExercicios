# Exercício 036 - Calcular empréstimo residencial. Vai perguntar o valor da casa, salário do
# comprador e quantos anos vai pagar. Calcular o valor da prestação não podendo ultrapassar 30% da renda.

v = float(input('Valor do imóvel: R$ '))
s = float(input('Renda Bruta total: R$ '))
a = int(input('Anos: '))
p = v / (a * 12)
print('Valor da Parcela: R$ {:.2f}' .format(p))
if p > (s * 0.30):
  print('Financiamento Reprovado')
else:
  print('Financiamento Aprovado')