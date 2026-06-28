# 030 - Crie um programa que leia um número interiro e mostre na tela se ele é PAR ou ímpar.
numero = randint(1,100)

if(numero % 2 == 0):
    print(f'{numero} é par')
else:
    print(f'{numero} é ímpar')