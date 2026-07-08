# 089 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
import cores

lista_alunos, dados = [], []

while True:
    nome = str(input('\nDigite o nome do aluno: '))
    dados.append(nome)
    lista_alunos.append(dados[:])
    dados.clear()
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota no aluno: '))
    dados.append(nota1)
    dados.append(nota2)
    lista_alunos.append(dados[:])
    dados.clear()

    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? S/N')).strip().upper()[0]

    if pergunta == 'N':
        for pos, itens in enumerate(lista_alunos):
            if pos % 2 == 0:
                print(f'Nome do aluno: {itens[0]}')
            else:
                print(f'Média: {(itens[0]/itens[1]):.2f}')

                

print(lista_alunos)

