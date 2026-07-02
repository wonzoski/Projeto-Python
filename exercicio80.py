# 080 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

import cores

lista_numeros = list()

for x in range(5):
    numero = int(input('Digite o número desejado: '))
    lista_numeros.append(numero)

    for y in range(len(lista_numeros)):
        if lista_numeros[x] < lista_numeros[y]:
            lista_numeros.insert(y, lista_numeros[x])
            lista_numeros.pop()
print(lista_numeros)

