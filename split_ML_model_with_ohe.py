import pandas as pd

import tensorflow as tf
import keras
from keras import layers

from sklearn.ensemble import RandomForestRegressor as rfr
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as MAE
from sklearn.preprocessing import StandardScaler


# importadno as informacoes
homes_data = pd.read_csv('amostra_final.csv', index_col=0)

boa_viagem_data = homes_data[homes_data['bairro'] == 'Boa Viagem']
other_homes_data = homes_data[homes_data['bairro'] != 'Boa Viagem']

# escolhendo as features usadas no modelo
homes_ML_model_features = ['tipo', 'bairro', 'tamanho', 'quartos', 'banheiros', 'garagens']

y_boa_viagem = boa_viagem_data['preço']
y_others = other_homes_data['preço']

# usando OneHotEncoding a partir do metodo .get_dummies da biblioteca pandas
X_boa_viagem = pd.get_dummies(boa_viagem_data[homes_ML_model_features]).drop(columns=['bairro_Boa Viagem'])
X_others = pd.get_dummies(other_homes_data[homes_ML_model_features])

print(X_others)

scaler = StandardScaler()
X_boa_viagem = scaler.fit_transform(X_boa_viagem)
X_others = scaler.fit_transform(X_others)

print(X_others)

# sparando os dados para treinar e validar
train_X_bv, val_X_bv, train_y_bv, val_y_bv = train_test_split(X_boa_viagem, y_boa_viagem, random_state = 0)
train_X_ot, val_X_ot, train_y_ot, val_y_ot = train_test_split(X_others, y_others, random_state = 0)

# criando a RandomForestRegressor
rfr_model_bv = rfr(random_state=1)
rfr_model_ot = rfr(random_state=1)

NN_model_bv = keras.Sequential()
NN_model_bv.add(keras.Input(shape=[X_boa_viagem.shape[1]]))
# NN_model_bv.add(layers.Dropout(0.3))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(64, activation='relu'))
NN_model_bv.add(layers.Dense(1))

NN_model_ot = keras.Sequential()
NN_model_ot.add(keras.Input(shape=[X_others.shape[1]]))
NN_model_ot.add(layers.Dropout(0.3))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dropout(0.3))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dropout(0.3))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dense(64, activation='relu'))
NN_model_ot.add(layers.Dense(1))

NN_model_bv.compile(
    optimizer='adam',
    loss='mae',
    metrics=['mae']
)

NN_model_ot.compile(
    optimizer='adam',
    loss='mae',
    metrics=['mae']
)

# incluindo os dados que ja temos
rfr_model_bv.fit(train_X_bv, train_y_bv)
rfr_model_ot.fit(train_X_ot, train_y_ot)

train_X_bv = pd.DataFrame(train_X_bv).astype('float64')
train_y_bv = pd.DataFrame(train_y_bv).astype('float64')
val_X_bv = pd.DataFrame(val_X_bv).astype('float64')
val_y_bv = pd.DataFrame(val_y_bv).astype('float64')

train_X_ot = pd.DataFrame(train_X_ot).astype('float64')
train_y_ot = pd.DataFrame(train_y_ot).astype('float64')
val_X_ot = pd.DataFrame(val_X_ot).astype('float64')
val_y_ot = pd.DataFrame(val_y_ot).astype('float64')


history_bv = NN_model_bv.fit(
    train_X_bv, train_y_bv,
    validation_data=(val_X_bv, val_y_bv),
    epochs=200,
    batch_size=15,
)

history_ot = NN_model_ot.fit(
    train_X_ot, train_y_ot,
    validation_data=(val_X_ot, val_y_ot),
    epochs=200,
    batch_size=15,
)

# realizando a previsão
validation_predictions_bv = rfr_model_bv.predict(val_X_bv)
validation_predictions_ot = rfr_model_ot.predict(val_X_ot)
validation_predictions_bv_NN = NN_model_bv.predict(val_X_bv)
validation_predictions_ot_NN = NN_model_ot.predict(val_X_ot)

MAE_bv = MAE(val_y_bv, validation_predictions_bv)
MAE_ot = MAE(val_y_ot, validation_predictions_ot)
MAE_bv_NN = MAE(val_y_bv, validation_predictions_bv_NN)
MAE_ot_NN = MAE(val_y_ot, validation_predictions_ot_NN)

print("boa viagem", MAE_bv)       # aproximadadmente 260 000 reais de margem de erro
print("boa viagem neural", MAE_bv_NN)       # aproximadadmente 230 000 reais de margem de erro
print("others", MAE_ot)       # aproximadadmente 190 000 reais de margem de erro
print("others neural", MAE_ot_NN)       # aproximadadmente 290 000 reais de margem de erro
print("average MAE", (min(MAE_bv, MAE_bv_NN) + MAE_ot) / 2)
