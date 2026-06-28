# 065 - Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores.

import cores

numeros = []

while True:
    valor = int(input('Digite um valor: '))
    numeros.append(valor)

    continuar = input('Quer continuar? [S/N]: ').strip().upper()

    if continuar == 'N':
        break

media = sum(numeros) / len(numeros)

print(f'\nA média dos valores é: {media:.2f}')
print(f'O maior valor é: {max(numeros)}')
print(f'O menor valor é: {min(numeros)}')