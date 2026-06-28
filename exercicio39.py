# 039 - Faça um programa que leia o ano de nascimento de uma jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar no serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostarr o tempo que falta ou que passou do prazo.
import time

birthYear = int(input('Digite seu ano de nascimento: '))
yearNow = time.localtime().tm_year
idade = yearNow - birthYear
anoAlistamento = yearNow - 18

if idade == 18:
    print('\033[4;32mÉ hora de se alistar!\033[m')
elif idade < 18:
    print(f'Você vai se alistar daqui \033[1;33m{birthYear - anoAlistamento}\033[m ano(s).')
elif idade > 18:
    print(f'Já passou do tempo de alistamento! \033[4;31mSe você ainda não se aprentou, deveiar ter se alistado em {birthYear + 18}\033[m')