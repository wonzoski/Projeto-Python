# 024 - Crie um programa que leia o nome de uma cidade e diga se ela começa um não com o nome "Santo".
# cidade = input('Digite o nome da cidade: ')
cidade = ' Santo Antônio de Saudade'

if cidade.strip().lower().find('santo') == 0:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')