# 041 - A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos:  Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima:       Master
import time, cores

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = time.localtime().tm_year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Mirim')
elif (idade <= 14):
    print('Infantil')
elif (idade <= 19):
    print('Junior')
elif idade == 20:
    print('Sênior')
elif idade > 20:
    print('Master')