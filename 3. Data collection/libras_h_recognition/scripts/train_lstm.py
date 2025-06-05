import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np

# Parâmetros
n_frames = 20
n_features = 63
n_classes = 2

# Carregar dados
X = np.load('../X.npy')
y = np.load('../y.npy')

# Criar modelo LSTM
model = Sequential([
    LSTM(64, input_shape=(n_frames, n_features), return_sequences=False),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(n_classes, activation='softmax')
])

# Compilar modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Treinar modelo
model.fit(X, y, epochs=30, batch_size=32, validation_split=0.2)

# Salvar modelo
model.save('../models/lstm_h_model.h5')