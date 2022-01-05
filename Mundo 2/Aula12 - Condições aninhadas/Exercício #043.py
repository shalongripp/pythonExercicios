# Exercício 043 - Ler o peso e altura de uma pessoa e calcular o IMC.
                # Mostrar o Status: Abaixo de 18.5 - abaixo do peso; entre 18.5 e 25 - Peso Ideal;
                # 30 até 40 - Obesidade; acima de 40 - Obesidade Mórbida
                
from math import pow
p = float(input('Peso(kg):'))
a = float(input('Altura(m): '))
imc = p / pow(a,2)
print('IMC: {:.2f}' .format(imc))
if imc < 18.5:
  print('Abaixo do Peso')
elif 18.5 <= imc < 25:
  print('Peso Normal')
elif 25 <= imc < 30:
  print('Acima do peso')
elif 30 <= imc < 35:
  print('Obesidade I')
elif 35 <= imc < 40:
  print('Obesidade II (severa)')
elif imc >= 40:
  print('Obesidade Mórbida')