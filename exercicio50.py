# 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares. Se o valor digitado for ímpar, desconsidere-o.
import cores

listaNumeros = []
soma = 0

while True:
    numDigite = int(input('Digite um número: '))
    listaNumeros.append(numDigite)
    print(listaNumeros)
    if len(listaNumeros) >= 6:
        for x in range(0, 6):
            if listaNumeros[x] % 2 == 0:
                soma += listaNumeros[x]
        print(f'A soma total dos números pares é: {soma}')
        break
    continue