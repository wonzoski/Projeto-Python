# 045 - Crie um programa que faça o computador jogar JOKENPÔ com você.
import os, random

os.system('clear')

compEscolhe = random.randint(1,3)

userEscolhe = int(input('-'*20 + '\n\033[1;33m  1 - Pedra\033[m\n' \
'\033[1;34m  2 - Papel\033[m\n' \
'\033[1;35m  3 - Tesoura\033[m\n' +\
'-'*20+'\n'))

print(compEscolhe)
if userEscolhe == compEscolhe:
    print('\033[33mEmpate!\033[m')
elif (userEscolhe == 1 and compEscolhe == 3) or (userEscolhe == 2 and compEscolhe == 1) or (userEscolhe == 3 and compEscolhe == 2):
    print('\033[32mVitória!\033[m')
elif (userEscolhe == 3 and compEscolhe == 1) or (userEscolhe == 1 and compEscolhe == 2) or (userEscolhe == 2 and compEscolhe == 3):
    print('\033[31mDerrota!\033[m')
else:
    print('Opção inválida!')