import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Definindo os dados de entrada e saída
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [[0], [1], [1], [0]]

# Convertendo para arrays do numpy
import numpy as np
X = np.array(X)
y = np.array(y)

# Criando o modelo
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilando o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
model.fit(X, y, epochs=1000, batch_size=4, verbose=2)

# Avaliando o modelo
loss, accuracy = model.evaluate(X, y)
print(f"Acurácia do modelo: {accuracy*100:.2f}%")

# Testando o modelo
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = model.predict(test_data)
print("Previsões:")
for i in range(len(predictions)):
    print(f"Entrada: {test_data[i]}, Saída Prevista: {predictions[i]}")