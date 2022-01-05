# Exercício 031 - Informar a distância de uma viagem em km.
# Cobrar R$ 0,50/km até 200 km e R$ 0,45/km para viagens mais longas.

d = float(input('Digite a distância em km: '))
if d <= 200.0:
  v = d * 0.5
  print('Valor da passagem: R$ {:.2f}' .format(v))
else:
  v = d * 0.45
  print('Valor da passagem: R$ {:.2f}' .format(v))