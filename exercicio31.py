# 031 - Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas.
distancia = float(input('Digite a kilometragem desejada para cálculo: '))

if(distancia <= 200):
    print(f'O valor total da viagem é R${distancia*0.50:.2f}')
else:
    print(f'O valor total da viagem é R${distancia*0.45:.2f}')