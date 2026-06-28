# ------------------------------------------------------------------------------------------------------------------------ #
#  035 - Desenvolva um programa que leia o comprimento de três retas e diga o usuário se eles podem ou não formar um triângulo.
# reta01 = float(input('Digite o valor da primeira reta: '))
# reta02 = float(input('Digite o valor da segunda reta: '))
# reta03 = float(input('Digite o valor da terceira reta: '))
# 
# if (reta01 < (reta02 + reta03)) and (reta02 < (reta01 + reta03)) and (reta03 < (reta02 + reta01)):
#     print('\033[1;32mPerfeito!\033[m O triângulo pode ser formado com sucesso.')
# else:
#     print('\033[1;31mAh não...\033[m o valor das retas não podem formar um triângulo!')
# ------------------------------------------------------------------------------------------------------------------------ #

# 042 - Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triãgulo será formado:
# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes

reta01 = float(input('Digite o valor da primeira reta: '))
reta02 = float(input('Digite o valor da segunda reta: '))
reta03 = float(input('Digite o valor da terceira reta: '))

if (reta01 < (reta02 + reta03)) and (reta02 < (reta01 + reta03)) and (reta03 < (reta02 + reta01)):
    if (reta01 == reta02 and reta01 != reta03) or (reta02 == reta03 and reta02 != reta01) or (reta03 == reta01 and reta03 != reta02):
        print('\033[1;32mPerfeito!\033[m O \033[4;33mtriângulo isóceles\033[m pode ser formado com sucesso!')
    elif (reta01 == reta02) and (reta02 == reta03) and (reta03 == reta01):
        print('\033[1;32mPerfeito!\033[m O \033[4;33mtriângulo equilátero\033[m pode ser formado com sucesso!')
    elif (reta01 != reta02) and (reta02 != reta03) and (reta03 != reta01):
        print('\033[1;32mPerfeito!\033[m O \033[4;33mtriângulo escaleno\033[m pode ser formado com sucesso!')
else:
    print('\033[1;31mAh não...\033[m o valor das retas não podem formar um triângulo!')