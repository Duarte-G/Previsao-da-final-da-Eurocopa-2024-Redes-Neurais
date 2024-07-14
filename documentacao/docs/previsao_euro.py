import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import accuracy_score

# Carregar dados
base = pd.read_csv('Euro_2024_Matches.csv')

# Separar jogos da Inglaterra e Espanha
inglaterra = base[(base['home_team'] == 'England') | (base['away_team'] == 'England')]
espanha = base[(base['home_team'] == 'Spain') | (base['away_team'] == 'Spain')]

# Colunas relevantes
selected_columns = [
    'home_goals', 'away_goals',
    'Home Expected goals(xG)', 'Away Expected goals(xG)',
    'Home Total shots.', 'Away Total shots',
    'Home Shots on target.', 'Away Shots on target',
    'Home Passes', 'Away Passes',
    'home_team', 'away_team'
]

# Preparar dados da Espanha
dados_espanha = espanha[selected_columns].copy()
dados_espanha['resultado_espanha'] = 0
espanha_home_win = (dados_espanha['home_team'] == 'Spain') & (dados_espanha['home_goals'] > dados_espanha['away_goals'])
espanha_away_win = (dados_espanha['away_team'] == 'Spain') & (dados_espanha['away_goals'] > dados_espanha['home_goals'])
dados_espanha.loc[espanha_home_win | espanha_away_win, 'resultado_espanha'] = 1
x_espanha = dados_espanha.drop(['home_team', 'away_team', 'resultado_espanha'], axis=1)
y_espanha = dados_espanha['resultado_espanha'].values

# Preparar dados da Inglaterra
dados_inglaterra = inglaterra[selected_columns].copy()
dados_inglaterra['resultado_inglaterra'] = 0
inglaterra_home_win = (dados_inglaterra['home_team'] == 'England') & (dados_inglaterra['home_goals'] > dados_inglaterra['away_goals'])
inglaterra_away_win = (dados_inglaterra['away_team'] == 'England') & (dados_inglaterra['away_goals'] > dados_inglaterra['home_goals'])
dados_inglaterra.loc[inglaterra_home_win | inglaterra_away_win, 'resultado_inglaterra'] = 1
x_inglaterra = dados_inglaterra.drop(['home_team', 'away_team', 'resultado_inglaterra'], axis=1)
y_inglaterra = dados_inglaterra['resultado_inglaterra'].values

# Modelo para Espanha
classificador_espanha = Sequential()
classificador_espanha.add(Dense(units=64, activation='relu', input_dim=x_espanha.shape[1]))
classificador_espanha.add(Dropout(0.2))
classificador_espanha.add(Dense(units=32, activation='relu'))
classificador_espanha.add(Dropout(0.2))
classificador_espanha.add(Dense(units=1, activation='sigmoid'))
classificador_espanha.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classificador_espanha.fit(x_espanha, y_espanha, epochs=500, batch_size=10, verbose=1)

# Avaliação para Espanha
resultados_previstos_espanha = classificador_espanha.predict(x_espanha).round().flatten()
acuracia_espanha = accuracy_score(y_espanha, resultados_previstos_espanha)
print(f'Acurácia do modelo para jogos da Espanha: {acuracia_espanha}')

# Modelo para Inglaterra
classificador_inglaterra = Sequential()
classificador_inglaterra.add(Dense(units=64, activation='relu', input_dim=x_inglaterra.shape[1]))
classificador_inglaterra.add(Dropout(0.2))
classificador_inglaterra.add(Dense(units=32, activation='relu'))
classificador_inglaterra.add(Dropout(0.2))
classificador_inglaterra.add(Dense(units=1, activation='sigmoid'))
classificador_inglaterra.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classificador_inglaterra.fit(x_inglaterra, y_inglaterra, epochs=500, batch_size=10, verbose=1)

# Avaliação para Inglaterra
resultados_previstos_inglaterra = classificador_inglaterra.predict(x_inglaterra).round().flatten()
acuracia_inglaterra = accuracy_score(y_inglaterra, resultados_previstos_inglaterra)
print(f'Acurácia do modelo para jogos da Inglaterra: {acuracia_inglaterra}')

# Previsão individual
resultado_previsto = classificador_espanha.predict(x_inglaterra.iloc[0].values.reshape(1, -1))
print(f"Probabilidade de vitória da Espanha sobre a Inglaterra: {resultado_previsto[0][0]}")
