# 015 - Escreva um programa que pergunte a quantidade de KM rodados percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo..
#..que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
# km = float(input("Qual a quantidade de KM rodado? "))
# dias = int(input("Qual a quantia em dias que o carro foi alugado? "))
km = 350
dias = 3
custo_km = (km*0.15)
custo_dia = (dias*60)
print(f"Valor total de R${custo_dia+custo_km:.2f}")