# 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção interira.
# Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6
from math import trunc
# num = float(input("Digite um número qualquer: "))
num = 8283.1231235159
numUpdated = trunc(num)
print(f"O número {num} tem a parte inteira {numUpdated}")