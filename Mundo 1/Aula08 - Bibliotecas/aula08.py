''' import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print(' A raiz do número {} é {} '.format(num, raiz))
print(' A raiz do número {} é {:.2f} '.format(num, raiz))
print(' A raiz do número {} é {} '.format(num, math.ceil(raiz))) #arredonda pra cima
print(' A raiz do número {} é {} '.format(num, math.floor(raiz))) #arredonda pra baixo '''

'''from math import ceil, sqrt, floor
num = int(input('digite um numero: '))
raiz = sqrt(num)
print(' A raiz do número {} é {} '.format(num, raiz))
print(' A raiz do número {} é {:.2f} '.format(num, raiz))
print(' A raiz do número {} é {} '.format(num, ceil(raiz))) #arredonda pra cima
print(' A raiz do número {} é {} '.format(num, floor(raiz))) #arredonda pra baixo'''

'''import random
num = random.random() #entre 0 e 1
print(num)'''

import random
num = random.randint(1,10) #inteiro dentro do intervalo dado
print(num)


