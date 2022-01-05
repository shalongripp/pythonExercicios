# Exercício 053 - Ler uma frase e dizer se é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print("Não temos um palíndromo")
