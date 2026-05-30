from math import ceil
print('===========ORÇMENTO================')

print('==========BANHEIRO=================')

parede_1 = float(input('Digite a aŕea da parede 1 em m2 :' ))
parede_2 = float(input('Digite a area da parede 2 em m2 :'))
parede_3 = float(input('Digite a area da parede 3 em m2 :'))
parede_4 = float(input('Digite a area da parede 4 em m2 :'))
teto = float(input('Digite a area do teto em m2 :'))
piso = float(input('Digite a area do piso em m2 :'))
revestimento_1 = ceil(parede_1 + parede_2 + parede_3 + parede_4 )
cimento_cola = ceil(1.5 * (revestimento_1 + piso)) 
rejunto = ceil((revestimento_1 + piso ) / 3)
m_o = float(input('Digite o valor da mão de obra por m2 : R$ '))
print(f'Total revestimento da parede {revestimento_1} m2')
print(f'Total cimento cola {cimento_cola} sacos')
print(f" total de rejunto {rejunto} kilos")
print(f' mao de o bra : R$ {m_o * (revestimento_1 + piso):.2f} ')

