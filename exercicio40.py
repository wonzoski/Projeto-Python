# 040 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0 -> Reprovado
# Média entre 5.0 e 6.9 -> Recuperação
# Média 7.0 ou superior -> Aprovado
import cores

notaA1 = float(input('Digite a primeira nota do aluno: '))
notaA2 = float(input('Digite a segunda nota do aluno: '))

mediaNota = ((notaA1 + notaA2) / 2)

if mediaNota < 5.0:
    print(f'{cores.vermelho}REPROVADO!{cores.fimCor}')
if (6.9 < mediaNota >= 5):
    print(f'{cores.amarelo}RECUPERAÇÃO{cores.fimCor}')
if mediaNota >= 7:
    print(f'{cores.verde}APROVADO!{cores.fimCor}')