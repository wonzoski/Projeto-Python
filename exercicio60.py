# 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120
import cores

Total = 1
Contador = 1

Num_Esc_User = int(input('Digite um número qualquer para o fatorial: '))

for x in range(1, Num_Esc_User+1):
    Total *= x
print(Total)