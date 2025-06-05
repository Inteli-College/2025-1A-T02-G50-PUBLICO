import numpy as np
import os

def load_sequences(data_dir, classes=['h', 'not_h'], max_frames=20):
    X, y = [], []
    expected_features = 63  # 21 pontos-chave x 3 coordenadas
    for idx, class_name in enumerate(classes):
        class_dir = os.path.join(data_dir, class_name)
        for file in os.listdir(class_dir):
            if file.endswith('.npy'):
                sequence = np.load(os.path.join(class_dir, file))
                # Verificar forma da sequência
                print(f"Carregando {file} de {class_name}, forma: {sequence.shape}")
                if sequence.ndim != 2 or sequence.shape[1] != expected_features:
                    print(f"Ignorando {file}: forma inválida {sequence.shape}, esperado [n, {expected_features}]")
                    continue
                # Ajustar número de frames
                if len(sequence) > max_frames:
                    sequence = sequence[:max_frames]
                elif len(sequence) < max_frames:
                    sequence = np.pad(sequence, ((0, max_frames - len(sequence)), (0, 0)), 'constant')
                # Normalizar
                sequence = (sequence - np.min(sequence)) / (np.max(sequence) - np.min(sequence) + 1e-10)
                X.append(sequence)
                y.append(idx)  # 0 para H, 1 para não-H
    X = np.array(X)
    y = np.array(y)
    print(f"Total de sequências válidas: {len(X)}")
    return X, y

# Carregar dados
data_dir = '../dataset'
X, y = load_sequences(data_dir)
np.save('../X.npy', X)
np.save('../y.npy', y)
print(f'Dataset shape: {X.shape}, Labels shape: {y.shape}')