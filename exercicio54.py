# 054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import cores, time

ano_Atual = time.localtime().tm_year

nome = []

qtd_Menor = 0
qtd_Maior = 0


for _ in range(7):
    ano = int(input('Ano: '))
    idade = ano_Atual - ano
    if idade < 18:
        qtd_Menor += 1
    else:
        qtd_Maior += 1

print(f'{qtd_Maior} pessoas atingiram a maioridade e {qtd_Menor} são de menor.')