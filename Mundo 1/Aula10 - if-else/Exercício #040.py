# Exercício 040 - Ler 2 notas de um aluno e calcule sua média mostrando:
# menor que 5 reprovado; entre 5 e 6.9 recuperação; 7 ou superior aprovado.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
if m < 5:
  print('Reprovado')
elif 5 <= m <=6.9:
  print('Recuperação')
elif m >= 7:
  print('Aprovado')