#Crie um programa que leia um número real qualquer pelo teclado e mostre sua porção inteira.
#from math import trunc
#n= float(input('Digite um número real :' ))
#print (f'A porção interira do número real {n} é : {trunc(n)}')

#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
#retangulo, calcule e mostre e mostre o comprimento da hipotenusa.
from math import hypot
c_o = int(input(' Digite o cateto oposto :'))
c_a = int(input(' digite o cateto adjacente:'))
#h = (pow(c_o , 2) + (pow( c_a , 2 )))
#print(f'A hitotenusa ao qudrado é :{h}')
#print(f'A raiz quadrada da hipotenusa é :{h ** (1/2):.3f}')
h = hypot(c_o, c_a)
print(f' A hipotenusa  è : {h:.3f}')
