# Aula 010 - Estruturas condicionais
'''
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
  print('Seu carro é novo')
else:
  print('Seu carro é velho')
print('Fim')

# Outra opção
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo<=3 else 'Carro velho')


nome = str(input('Qual é o seu nome? '))
if nome == 'Shalon':
  print('Que nome lindo vc tem!!!')
else:
  print('Seu nome é tão normal!')
print('Muito prazer, {}!'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2  = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média é {:.1f}' .format(m))
if m >= 6.0:
  print('Aprovado')
elif 4.0 <= m < 6.0:
  print('Recuperação')
elif m < 4.0:
  print('Reprovado')

