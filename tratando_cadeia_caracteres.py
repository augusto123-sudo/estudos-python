#manipulando texto:
#Nessa aula, vamos aprender operações com String no Python.
#  As principais operações que vamos aprender são o Fatiamento de String, 
# Análise com len(), count(), find(), transformações com replace(), 
# upper(), lower(), capitalize(), title(), strip(), junção com join().

#Fatiamento:

frase =('Curso em video python')#Aqui eu tenho uma cadeis de caracteres que são micro espaços 
#criados na memoria do computador , incluindo od espaços.
print(frase[9:15])# A partir do caractere "3" eu determinei que o programa impromisse "7" caracteres 
#da string.
frase = ('selmo AugustO Batista Abdo')
print(frase[0:24:4])# Nesse caso o programa seleciona 24 caraccteres a partir do '0' , e escolhe 
# de 4 em 4.
print(frase[:6])# Nesse caso o programa seleciona os caracteres do '0" ao '5'.
print(frase[5:])# nesse caso o programa seleciona os caracterses do '5' ate o fim da string.
print(frase[6::4])# nesse caso o programa seleciona os caracteres do "6" ate'o fim da string
# e escolhe de 4 em 4 e printa.

# Analise de uma string: 

print(len(frase))# Conta quantos caracteres etm a string, incluindo espaços.
print(frase.count('o'))# Conta quantos caracters iguais tem na string, (diferencia maiusculo de 
#minusculo))
print(frase.lower().count('o'))# Nao diferencia maiusculo de minusculo.
print(frase.lower().count('o',0,13)) #O programa seleciona os caracteres do indice"0" ao "13"
# contas quantos caracteres igual tem i printa.
print(frase.find('mo'))# O programa em que indice,inicia os caracters selecionados.
print(frase.find('python')) # O programa retorna '-1' porque a string nao faz parte da lista.
#print(frase.lower().count('a'))

import random

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n = [n1,n2,n3,n4]
random.shuffle(n)
print(n)
print(len(n))
print(n[0:2])
c = random.choice(n[0:2])
print(c)

#selecionando cartas de taro:

import random

p = input('Faça uma pergunta :')

n1 = ('O mago')
n2 = ('A Sacerdotiza')
n3 = ('A imperatriz')
n4 = ('O Imperador')
n5= (' O Sacerdote')
n6 = ('Os Enamorados')
n7 = ('O Carro')
n8 = (' A Justiça')
n9 = (' O eremita')
n10 = (' A roda da fortuna')
n11 = (' A força')
n12 = (' O Pendurado')
n13 = (" A Morte")
n14 = ('A temperança')
n15 = (' O Diabo')
n16 = (' A torre')
n17 = (' A estrela')
n18 = ('A Lua')
n19 = ('O sol')
n20 = ('O julgamneto')
n21 = (' O Mundo')
n22 = (' O louco')

taro = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22]
random.shuffle (taro)
escolha = random.choice(taro)
print(f'Sua pergunta foi, {p}, e a resposta do taro é: {escolha}')