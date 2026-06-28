# 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
lista_nomes = ["Fabricio", "Marcelo", "Pedro", "João", "Gustavo"]
print(random.choice(lista_nomes))