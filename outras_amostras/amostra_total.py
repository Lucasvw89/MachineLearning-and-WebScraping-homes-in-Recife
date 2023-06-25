import pandas as pd

amostra_de_apartamentos = pd.read_csv('amostra_de_apartamentos.csv', index_col=0)
amostra_de_casas = pd.read_csv('amostra_de_casas.csv', index_col=0)
amostra_de_casas_em_condominio = pd.read_csv('amostra_de_casas_em_condominio.csv', index_col=0)
amostra_de_flat = pd.read_csv('amostra_de_flat.csv', index_col=0)

amostra_total = pd.concat([amostra_de_apartamentos, amostra_de_casas, amostra_de_casas_em_condominio, amostra_de_flat], ignore_index=True)

amostra_total.to_csv('amostra_total.csv')