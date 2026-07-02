# 077 - Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

import cores

lista_palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for palavra in lista_palavras:
    print(f'\nNa palavra {cores.verde}{palavra.upper()}{cores.fimCor} temos ', end='')
    for letra in range(0, len(palavra)):
        if palavra[letra] in 'aeiou':
            print(f'{palavra[letra]}',end=' ')