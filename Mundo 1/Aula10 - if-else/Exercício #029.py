# Exercício 029 - Escreva um programa que leia a velocidade de um carro.
# Se ultrapassar 80 km/h recebe mensagem que foi multado com R$ 7,00 por km/h excedente.

v = float(input('Digite o valor da velocidade: '))
if v > 80.0:
  print('Você excedeu o limite de velocidade!')
  m = (v - 80) * 7
  print('Foi multado em R$ {:.2f}' .format(m))
else:
  print('Dirija com segurança!')