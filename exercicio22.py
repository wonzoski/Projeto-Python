# 022 - Crie um programa que leia um nome completo de uma pessoa e mostre:
nome = '  Fabrício Wonzoski  '
# O nome com todas as letras maiúscilas
print(f'O nome com todas as letras maiúscilas: {nome.upper().strip()}')

# O nome com todas minúsculas
print(f'O nome com todas minúsculas: {nome.lower().strip()}')

# Quantas letras ao todo (sem considerar espaços)
print(f'Seu nome tem {len(nome.replace(' ',''))} letras ao todo')

# Quantas letras tem o primeiro nome
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')