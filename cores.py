# ANSII
# 
#     style back
#      |     |
# \033[0;33;44m<código>\033[m
#        |
#       text
# 
# 🔹Style
#     0 --> None
#     1 --> Bold
#     4 --> Underline
#     7 --> Negative
# .
# 🔹Text
#     30 --> Branco
#     31 --> Vermelho
#     32 --> Verde
#     33 --> Amarelo
#     34 --> Azul
#     35 --> Majenta
#     36 --> Ciano
#     37 --> Cinza
# .
# 
# 🔹Back
#     40 --> Branco
#     41 --> Vermelho
#     42 --> Verde
#     43 --> Amarelo
#     44 --> Azul
#     45 --> Majenta
#     46 --> Ciano
#     47 --> Cinza

import os
os.system('clear')
os.system('cls')

vermelho = str('\033[31m')
verde = str('\033[32m')
amarelo = str('\033[33m')
azul = str('\033[34m')
majenta = str('\033[35m')
ciano = str('\033[36m')
cinza = str('\033[37m')

negrito = str('\033[1m')
linhado = str('\033[4m')
negativo = str('\033[7m')

backBranco = str('\033[0;30;40m')
backVemelho = str('\033[0;30;41m')
backVerde = str('\033[0;30;42m')
backAzul = str('\033[0;30;44m')
backMajenta = str('\033[0;30;45m')
backCiano = str('\033[0;30;46m')
backCinza = str('\033[0;30;47m')

fimCor = str('\033[m')