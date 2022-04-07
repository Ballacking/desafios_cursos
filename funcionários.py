# Desafios com Sets

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#Lista1
list1 = set(tem_carro)
list2 = set(turno_noite)

print(list1 & list2)

#Lista2
list3 = set(tem_carro)
list4 = set(turno_dia)

print(list3 & list4)

#Lista3
list5 = set(funcionarios)
list6 = set(tem_carro)
print(list5 - list6)
