# 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o valor 3.
# C) Quais fora os números pares

import cores

numLista = tuple(int(input('Digite o valor: ')) for _ in range(4))

print(f'\nValores digitados foram {numLista}')

# A) Quantas vezes apareceu o valor 9.
if (numLista.count(9)) != 0:
    print(f'O número 9 apareceu {numLista.count(9)} vez')
else:
    print('O numero 9 não aparece nessa listagem.')

# B) Em que posição foi digitado o valor 3.
if (numLista.count(3)) != 0:
    print(f'O número 3 foi digitado na posição {numLista.index(3)+1}')
else:
    print('O numero 3 não aparece nessa listagem.')

# C) Quais fora os números pares
print('Valores pares digitados são ', end='')
for numero in numLista:
    if numero % 2 == 0:
        print(numero, end=' ')