# Cálculo de IMC - Índice de massa Corporal

'''
Qual a sua altura em cm:
Qual seu peso em kg:
Equação IMC = Peso/Altura*Altura

'''

# Menor que 18,5 - Magreza
# Entre 18,5 e 24,9 - Normal
# Entre 25,0 e 29,9 - Sobrepeso
# Entre 30,0 e 39,9 - Obesidade
# Maior que 40,0 - Obesidade Grave

nome = str(input('Qual é o seu nome?: '))
altura = float(input('Qual é a sua aluta em CM: '))
peso = float(input('Qual é o seu peso em KG: '))

imc = float (peso / (altura/100)**2)

if imc < 18.5:
    print(f'{nome}, você está abaixo do seu peso ideal, seu IMC é de {imc:.2f}')

elif imc >= 18.5 and imc < 24.9:
    print(f'{nome}, você está com seu peso ideal, seu IMC é de {imc:.2f}')

elif imc >= 25 and imc < 29.9:
    print(f'{nome}, você está com sobrepeso, tome cuidado, seu IMC é de {imc:.2f} !!! ')

elif imc >= 30 and imc < 39.9:
    print(f'{nome}, você está obeso, tome muito cuidado, seu IMC é de {imc:.2f} !!! ')

elif imc > 40:
    print(f'{nome}, você está com obesidade grave, deve ir ao médico urgente, seu IMC é de {imc:.2f} !!! ')

else:
    print('Internação')