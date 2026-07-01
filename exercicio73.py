# 073 - Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
import cores

lista_times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'RB Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')

# A) Apenas os 5 primeiros.
print(f'{cores.amarelo}Top 5 times da tabela são:{cores.fimCor} {lista_times[:5]}')

# B) Os últimos 4 colocados da tabela.
print(f'{cores.verde}Os últimos 4 colocados da tabela são:{cores.fimCor} {lista_times[-4:]}')

# C) Uma lista com os times em ordem alfabética.
print(f'{cores.amarelo}Times em ordem alfabética:{cores.fimCor} {sorted(lista_times)}')

# D) Em que posição na tabela está o time da Chapecoense.
print(f'{cores.verde}Chapecoense está em:{cores.fimCor} {lista_times.index("Chapecoense")+1}° lugar')