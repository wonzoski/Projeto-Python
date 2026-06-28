# 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = int(input('Digite o terceiro número: '))

if(num_3 < num_1 > num_2):
    print(f'{num_1} é maior que {num_2} e {num_3}')
elif (num_3 < num_2 > num_1):
    print(f'{num_2} é maior que {num_1} e {num_2}')
else:
    print(f'{num_3} é maior que {num_2} e {num_1}')