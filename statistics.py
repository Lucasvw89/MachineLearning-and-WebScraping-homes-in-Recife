import pandas as pd

homes_data = pd.read_csv('amostra_final.csv')

# way too many entries in "Boa Viagem"
print(homes_data['bairro'].value_counts())
