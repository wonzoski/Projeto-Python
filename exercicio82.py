# 081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

import cores

lista_numeros = []

while True:
    lista_numeros.append(int(input('Digite o número desejado: ')))

    pergunta = ' '
    while pergunta not in "SN":
        pergunta = str(input('Deseja continuar? S/N: ')).strip().upper()[0]

    if pergunta == 'N':
        break

lista_pares, lista_impares = [], []

for x in range(len(lista_numeros)):
    if lista_numeros[x] % 2 == 0:
        lista_pares.append(lista_numeros[x])
    else:
        lista_impares.append(lista_numeros[x])

print(f'\nLista original: {lista_numeros}\n')
print(f'Lista de números pares: {lista_pares}\n')
print(f'Lista de números ímpares: {lista_impares}\n')