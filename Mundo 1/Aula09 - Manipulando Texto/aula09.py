# Aula 09 - Manipulando Texto
frase = 'curso em vídeo'
print(frase)

    # Fatiamento:
#print(frase[9]) # vai identificar o caracter 9 - 'V'
#print(frase[9:13]) # seleciona do caracter 9 até o 12 - 'Víde'
#print(frase[9:22]) # vai fatiar do 9 ao último caracter nesse intervalo
#print(frase[9:21:2]) # do 9 ao 21 de 2 em 2
#print(frase[:5]) # começa do caracter 0 até o 5
print(frase[15:]) # do 15 até o final
print(frase[9::3]) # começa no 9 até o final pulando de 3 em 3

'''
    # Análise:
print(len(frase)) # mostra a quantidade de caracteres
print(frase.count('o')) # quantidade de ocorrências da letra o minúscula
print(frase.count('o', 0, 13)) # contando a letra 'o' do 0 ao 13
print(frase.find('deo')) # 'deo' encontrado na posição 11
print(frase.find('android')) # vai retornar '-1' indicando que não existe 'android' na sentença.
'curso'in frase # vai retornar 'True' pois existe a palavra 'curso'na sentença.

    # Transformação:
frase = frase.replace('Python', 'Android')
print(frase.replace('Python', 'Android')) # Substitui "Python' por 'Android'
print(frase.upper()) # transforma as minúsculas em maiúsculas
print(frase.lower()) # transforma maiúsculas em minúsculas
print(frase.capitalize()) # transforma primeira letra de uma frase em maiúscula
print(frase.title()) # transforma a primeira letra de cada palavra de ima frase em maiúscula
print(frase.strip()) # Remove espaços excedentes no início e no final da cadeia de caracteres
print(frase.rstrip()) # Remove espaços excedentes no lado direito ('r') da cadeia de caracteres
print(frase.lstrip()) # Remove espaços excedentes no lado esquerdo ('l') da cadeia de caracteres

    # Divisão:
print(frase.split()) # Por padrão, divide cada palavra da cadeia gerando uma lista com todas as palavras
                    # da cadeia e com indexação própria.
              # Existem outras funcionlidades para o método 'split'.

    # Junção:
'-'.join(frase) # Faz a junção de todos os elementos de 'frase'. No caso, serão unidos com o separador '-'.
                #Ex.: 'curso-em-vídeo' 

'''