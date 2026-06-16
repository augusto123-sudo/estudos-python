texto = ''' Um computador é uma máquina composta de um conjunto de partes eletronicas 
e eletromecanicas , com capacidade de coletar, armazenar e manipular dados , além, de 
fornecer diversas informações de forma automática.'''
print(len(texto))
#total_letras = len(texto) - texto.count(' ')
total_letras = len(texto.replace('\n','')) - texto.count (' ')# para não contar as quebras de linha.
print(total_letras)