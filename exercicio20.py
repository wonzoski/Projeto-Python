# 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
lista_nomes = 'Fabricio Marcelo Pedro João Gustavo'.split()
shuffle(lista_nomes) 
print("Os seguintes alunos foram sorteados aleatóriamente para apresentação de trabalho:")
print(f"1° {lista_nomes[0]}\n2° {lista_nomes[1]}\n3° {lista_nomes[2]}\n4° {lista_nomes[3]}\n5° {lista_nomes[4]}")