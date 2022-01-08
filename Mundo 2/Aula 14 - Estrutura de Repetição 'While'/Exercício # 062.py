# Melhore o DESAFIO 61 , perguntando ao usuário se ele quer mais alguns termos. O programa
# encera quando ele disser que quer 0 (zero) termos.

#  an = a1+(n-1) x r

a1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

count = 1
termo = a1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        count += 1
    print('PAUSA')
    mais = int(input('vc quer mais quantos termos: '))
print('Progressão finalizada com {} termos' .format(total))

