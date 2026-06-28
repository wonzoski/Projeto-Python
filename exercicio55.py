# 055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
import cores

pesoMaior = 0
for _ in range(5):
    peso = float(input('Digite o peso: '))
    if peso > pesoMaior:
        pesoMaior = peso
print(f'{pesoMaior:2f}')