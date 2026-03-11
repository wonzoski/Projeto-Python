# 035 - Desenvolva um programa que leia o comprimento de três retas e diga o usuário se eles podem ou não formar um triângulo.
reta01 = float(input('Digite o valor da primeira reta: '))
reta02 = float(input('Digite o valor da segunda reta: '))
reta03 = float(input('Digite o valor da terceira reta: '))

if (reta01 < (reta02 + reta03)) and (reta02 < (reta01 + reta03)) and (reta03 < (reta02 + reta01)):
    print('\033[1;32mPerfeito!\033[m O triângulo pode ser formado com sucesso.')
else:
    print('\033[1;31mAh não...\033[m o valor das retas não podem formar um triângulo!')