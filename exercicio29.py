# 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada KM acima do limite.
from random import randint
velocidade = randint(50,100)

if(velocidade > 80):
    multa = (velocidade-80)*7
    print(f'Você atingiu o limite de velocidade, {velocidade}KM/h! Tome sua multa de R${multa:.2f}.')
