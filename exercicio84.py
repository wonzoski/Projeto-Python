# 084 - Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
import cores

lista_pessoas, dados, lista_peso_maior, lista_peso_menor = [], [], [], []
lista_pessoas = [['Fabricio', 80.0], ['Maria', 77.0], ['Marcelo', 89.0], ['Julia', 60.0], ['João', 89.0]]

#while True:
#    dados.append(str(input('Digite o nome: ')))
#    dados.append(float(input('Digite o peso: ')))
#
#    lista_pessoas.append(dados[:])
#    dados.clear()
#
#    pergunta = ' '
#    while pergunta not in 'SN':
#        pergunta = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
#
#    if pergunta == 'N':
#        break

peso_maior_auxiliar = peso_menor_auxiliar = lista_pessoas[0][1]

for pessoa in lista_pessoas:
    if pessoa[1] >= peso_maior_auxiliar:
        peso_maior_auxiliar = pessoa[1]
    if pessoa[1] <= peso_menor_auxiliar:
        peso_menor_auxiliar = pessoa[1]

for pessoa in lista_pessoas:
    if peso_maior_auxiliar == pessoa[1]:
        lista_peso_maior.append(pessoa[0])
    if peso_menor_auxiliar == pessoa[1]:
        lista_peso_menor.append(pessoa[0])

print(f'Quantas pessoas foram cadastradas → {len(lista_pessoas)}')
print(f'Uma listagem com as pessoas mais pesadas → {lista_peso_maior} com {peso_maior_auxiliar:.2f}KG')
print(f'Uma listagem com as pessoas mais leves → {lista_peso_menor} com {peso_menor_auxiliar:.2f}KG')