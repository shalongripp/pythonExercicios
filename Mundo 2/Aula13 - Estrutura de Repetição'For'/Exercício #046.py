# Exercício 046 - Fazer uma contagem regressiva para os estouros dos fogos de artifício indo de 10 até 0
                # com pausa de 1 s entre eles

from time import sleep
for c in range(10, 0, -1):
  print(c)
  sleep(2)
print('BUM-BUM-BUM-BUM!')