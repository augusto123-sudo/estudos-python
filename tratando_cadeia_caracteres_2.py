# Analise com o operador IN:

frase = (' selmo augusto batista abdo')
print('josé' in (frase))# Mostra se a palavra existe na frase.


frase = ('Deus é o logos, a lógica por detrás da razão')

# Medição e contagem( LEN , COUNT)
print(len(frase))# Mostra o comprimento da string incluindo os espaços.
print(frase.count('d'))# O programa Ignorou a orimeira letra D, por ser maiusculo.
print(frase.lower().count('d'))# O programa contou todos os "d" idenpendente de serem maiusculos ou não.
# deixa a frase inteira em minuscula.

# localização(FIND)
print(frase.find('logos')) # Mostra em que posição da string(indice) a palavra começa.

# transformação (UPPER,LOWER,CAPITALIZE,TITLE)
print( frase.upper())# Coloca a frase inteira em maiuscula.
print(frase.lower())# coloca a frase inteira em minusculo.
print(frase.capitalize())# deixa apenas a primeirissima letra da frase em maiuscula.
print(frase.title())# Coloca a letra inicial de cada palavra em maiusculo.

# Limpesa de espaço(STRIP,RSTRIP,LSTRIP)

frase = ('      Deus é o Logos, a lógica por traz da razão.     ')
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# dividir e juntar (SPLIT,JOIN)

frase = (' Deus é o logos, a lógica por detras da razão')
palavra = (frase.split())# As palavras aparecem divididas por virgulas e aspas, criando uma lista
# onde cada palavra ocupa uma posição ,0,1,2,3,etc..
print(palavra)
print('-'.join(palavra))# As palavras aparecen juntas por traços.
print(' '.join(palavra))# As palavras aparecem juntas com espaços."

# Crie um programa que que leia o nome completo de uma pessoa, e mostre
# O nome com todas as letras maiusculas, O nome com todas as letras mínusculas,
# Quantas letras no total sem considerar os espaços,
# Quantas letras tem o primeiro nome.

nome = input('Digite um nome completo:')
print(nome)
print(nome.upper())
print(nome.lower())
total_letras = len(nome) - nome.count(' ')# A variavél recebeu o total de letras com os espaços
#já subtraidos.
print(f'Quantidade de letras sem espaços :{total_letras}')# Mostra a quantidade de letras sem o espaços
palavra = nome.split()
print(f'O primeiro nome tem {len(palavra[0])} letras ')# conta a quantidade de letras da palavra da
# posição (0).

# faça um programa que leia um número de 0 à 9999 e mostre na tela cada um dos dígitos separados.
# especificando a unidade, dezena ,centena e milhar.

n1= int(input('Digite um numero entre 0 à 9999:'))
print(f'Unidade {n1[3]}') # Com esse metodo , se eu digitar um numero com menos de 4 casas 
print(f'Dezena {n1[2]}') # dara sempre erro.
print(f'centena {n1[1]}')
print(f'Milhar {n1[0]}')

u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f' Unidade:{u}')
print(f' dezena :{d}')
print(f'Centena :{c}')
print(f'Milhar :{m}')

# crie um programa que leie um nome de uma cidade e diga se ela começa com o nome SANTO.

nome = input(' Digite o nome de uma Cidade :')
print(f' O nome SANTO aparece no nome da cidade ? :{('SANTO' in (nome))}')
nome_1 = (nome[0:5].upper())
print(f'O nome SANTO aparece no primeiro nome da cidade ? : {('SANTO' in (nome_1))}')

















