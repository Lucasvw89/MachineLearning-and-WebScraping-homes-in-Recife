import pandas as pd

from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


# importadno as informacoes
homes_data = pd.read_csv('amostra_final.csv', index_col=0)

# escolhendo as features usadas no modelo
homes_ML_model_features = ['tamanho', 'quartos', 'banheiros', 'garagens']

y = homes_data.preço

X = homes_data[homes_ML_model_features]

# sparando os dados para treinar e validar
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

# criando a RandomForestRegressor
rfr_model = rfr(random_state=1)

# incluindo os dados que ja temos
rfr_model.fit(train_X,train_y)

# realizando a previsão
validation_predictions = rfr_model.predict(val_X)

print(mean_absolute_error(val_y, validation_predictions))       # aproximadadmente 316 000 reais de margem de erro

rfr_model_complete = rfr(random_state=1)

rfr_model_complete.fit(X, y)
