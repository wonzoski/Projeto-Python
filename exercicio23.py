# 023 - Faça um programa que leia um número de - a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4, dezena:3, centena: 8, milhar:1

#numero = input('Digite um número de 0 até 9999: ')
#if (len(numero) < 5 and numero.isnumeric()):
#    if len(numero) == 1:
#        print(f'Unidade: {numero[0]}')
#    elif len(numero) == 2:
#        print(f'Unidade: {numero[0]}')
#        print(f'Dezena: {numero[1]}')
#    elif len(numero) == 3:
#        print(f'Unidade: {numero[0]}')
#        print(f'Dezena: {numero[1]}')
#        print(f'Centena: {numero[2]}')
#    elif len(numero) == 4:
#        print(f'Unidade: {numero[0]}')
#        print(f'Dezena: {numero[1]}')
#        print(f'Centena: {numero[2]}')        
#        print(f'Milhar: {numero[3]}')

# numero = int(input('Digite um número de 0 até 9999: '))
numero = 23
if 0 <= numero <= 9999:
    print(f'Unidade: {numero % 10}')
    print(f'Dezena: {(numero // 10) % 10}')
    print(f'Centena: {(numero // 100) % 10}')
    print(f'Milhar: {(numero // 1000) % 10}')
else:
    print("Número inválido")