# 011 - Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
# largura = float(input("Digite a largura da parede em metros: "))
# altura = float(input("Digite a altura da parede em metros: "))
largura = 5
altura = 3
area = largura*altura
print(f"A área de parede é {area:.2f}m² sendo necessário {area/2:.2f}l de tinta para pintar totalmente a parede.")