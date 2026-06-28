# 026 - Faça um programa que leia uma frase pelo teclado e mostre:
frase = str('Amanda ama Pedro').lower().strip()

# Quantas vezes aparece a letra "A".
print(frase.count('a'))

# Em que posição ela aparece a primeira vez.
print(frase.find('a')+1)

# Em que posição aparece a última vez.
print(frase.rfind('a')+1)