# Desafios com Funções

'''

Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deve informar as seguintes informações, Rendimento, altura e largura
O programa deve mostrar na tela 'Você necessita de x latas de tinta'

'''
x = int (input ('Digite a quantidade de latas: '))
y = input (('Digite a altura da parede: '))
z = input (('Digite o comprimento da aprede:'))

def calculo_tinta():
    area = int(y)*int(z)
    total_latas = area / x
    print (f'Você precisa de {total_latas} latas de tinta')

calculo_tinta()