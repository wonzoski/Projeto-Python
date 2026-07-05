# 085 - Crie um programa onde o usuário possa digitar seta valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

import cores

pares, impares = [], []
lista_numeros = [pares,impares]

for x in range(7):
    numero = int(input(f'Digite o {x+1}° número desejado: '))

    if numero % 2 == 0:
        lista_numeros[0].append(numero)
    else:
        lista_numeros[1].append(numero)

print(f'Números pares: {lista_numeros[0]}')
print(f'Números ímpares: {lista_numeros[1]}')