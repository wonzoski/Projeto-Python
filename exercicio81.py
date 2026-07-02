# 081 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
import cores

lista_numeros = list()

while True:
    numero = int(input('Digite o número desejado: '))
    lista_numeros.append(numero)
    
    pergunta = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    while pergunta not in 'SN':
        pergunta = str(input('Você precisa digitar! S/N: ')).strip().upper()[0]
    
    if pergunta == 'N':
        break

# A) Quantos números foram digitados.
print(f'\nNumeros digitados: {len(lista_numeros)}\n')

# B) A lista de valores, ordenada de forma decrescente.
lista_numeros.sort(reverse=True)
print(f'Lista de valores em ordem decrescente: {lista_numeros}')

# C) Se o valor 5 foi digitado e está ou não na lista.
if '5' in lista_numeros:
    print('\nO número 5 está na lista')
else:
    print('\nNúmero 5 não está na lista.')