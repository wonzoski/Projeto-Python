# 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
import cores

lista_numeros = list()

while True:
    numero = int(input('Digite o valor para adicionar na lista: '))

    if numero not in lista_numeros:
        lista_numeros.append(numero)
    else:
        print('O valor já exite na lista!')

    confirma = ' '    
    while confirma not in 'SN':
        confirma = str(input('Deseja continuar? S/N')).upper().split()[0]

    if confirma == 'N':
        break

lista_numeros.sort()
print(f'\nValores em ordem → {lista_numeros}\n')
