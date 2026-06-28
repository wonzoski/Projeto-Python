# 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# numero_inteiro = int(input("Digite um número inteiro: "))
numero_inteiro = 5
for x in range(1,11):
    print(f"{numero_inteiro}x{x}={numero_inteiro*x}")