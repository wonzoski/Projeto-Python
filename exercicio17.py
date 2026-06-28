# 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto ajacente de um triângulo retângulo, calcule e mostre o comprimento de hipotenusa.
from math import hypot
# co = float(input("Digite o valor do cateto oposto: "))
# ca = float(input("Digite o valor do cateto adjacente: "))
co = 10.1239
ca = 19.329
hi = hypot(co, ca)
print(f'A valor da hipotenuse vai medir {hi}')

