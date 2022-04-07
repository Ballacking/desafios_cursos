# Desafio com If, Elif e Else

'''
Criar um programa que dependendo da temperatura (em Celsius) do steak
ele retorne o ponto de cozimento em português. O usuário deverá fornecer a temperatura

Temperatura - Cozimento
120°F ou 45°C - Rare (Selada)
130°F ou 54°C - Medium Rare (Ao ponto para mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium Well (Ao ponto para o bem)
160°F ou 71°C - Well Done (Bem passada)
'''

ponto_carne = int(input('Qual é a temperatura da carne?: '))

if ponto_carne < 45:
    print('A carne está selada')

elif ponto_carne in range (48,53):
    print ('A carne está mal passada')

elif ponto_carne in range (54,59):
    print('A canre está ao ponto')

elif ponto_carne in range (60,64):
    print('A carne está ao ponto para bem passada')

elif ponto_carne in range (65,70):
    print('A carne está bem passada')

elif ponto_carne in range (71,74):
    print('Ao ponto')

elif ponto_carne >= 75:
    print('A carne queimou')

else:
    ('Opção inválida')