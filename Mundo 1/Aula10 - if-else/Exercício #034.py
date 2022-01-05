 # Exercício 034 - Perguntar o salário e calcular o aumento de 10% quando acima de R$ 1.250,00
 # e 15% para salários inferiores
 
s = float(input('Digite o salário: R$ '))
if s > 1250:
  print('Seu salário com aumento de 10% será de R$ {:.2f}' .format(s * 1.10))
else:
  print('Seu salário com aumento de 15% será de R$ {:.2f}' .format(s * 1.15))