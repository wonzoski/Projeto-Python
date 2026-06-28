# 018 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
from math import radians,sin,cos,tan
# num = float(input("Digite o valor do ângulo desejado: "))
num = 45
seno = sin(radians(num))
coseno = cos(radians(num))
tangente = tan(radians(num))

print(f"\
Seno: {seno:.2f}\n\
Coseno: {coseno:.2f}\n\
Tangente: {tangente:.2f}"
)