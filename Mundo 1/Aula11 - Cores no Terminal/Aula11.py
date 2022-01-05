'''

    style            text            background
    0(none)         30(branco)      40(idem)
    1(bold)         31(vermelho)    41('')
    4(underline)    32(verde)       42('')
    7(negative)     33(amarelo)     43('')
                    34(azul)        44('')
                    35(violeta)     45('')
                    36(ciano)       46('')
                    37(cinza)       47('')
'''

print('\033[0;31mOlá, mundo!') # em vermelho

print('\033[0;31;43mOlá, mundo!') # fundo amarelo

print('\033[1;31;43mOlá, mundo!') # fundo amarelo e texto em negrito

print('\033[1;31;43mOlá, mundo!\033[m') # fundo amarelo e texto em negrito limitando o fundo amarelo no final do texto

print('\033[4;30;45mOlá, mundo!\033[m') # sublinhado e fundo violeta

print('\033[7;30;44mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[35m{}\033[m'.format(a, b))

print('Os valores são {}{}{} e {}{}{}'.format('\033[32m',a,'\033[m', '\033[35m', b,'\033[m')) #fazendo a mesma coisa usando máscaras