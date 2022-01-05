# Exercício 039 - Ler ano de nascimento de um jovem e informar: se ainda vai se alistar;
                # se é hora de se alistar; se já passou do tempo de alistamento. Mostrar o tempo que falta ou que passou.

from datetime import date
a = int(input('Digite o ano de seu nascimento: '))
print('[1] Masculino\n[2] Feminino')
sexo = int(input('Qual é o seu sexo? '))
if sexo == 1:
  atual = date.today().year
  l = atual - a
  print(' Você completa {} anos em {}' .format(l, atual))
  if l < 18:
    ano = (a + 18)
    print('Você ainda vai se alistar. Faltam {} anos para seu alistamento.' . format(abs(l-18)))
    print('Seu alistamento será em {}' .format(ano))
  elif l == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
  elif l > 18:
    ano = a + 18
    print('Já deveria ter se alistado há {} anos.' .format(abs(l-18)))
    print('Seu alistamento foi em {}' .format(ano))
else:
  print('Seu alistamento não é obrigatório')