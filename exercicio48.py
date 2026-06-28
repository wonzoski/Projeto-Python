# 048 - Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
import cores
soma = 0

for count in range(1,501,2):
    if (count) % 3 == 0:
        soma += count
print(f'A soma entre todos os números impares que são multiplos de três é {soma}.')