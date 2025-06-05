import cv2
import mediapipe as mp
import numpy as np
from tensorflow.keras.models import load_model

# Configurar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Carregar modelo
model = load_model('../models/lstm_h_model.h5')

# Parâmetros
n_frames = 20
n_features = 63
sequence = []

# Captura de vídeo
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível ler o frame da webcam.")
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            sequence.append(landmarks)
            
            if len(sequence) > n_frames:
                sequence = sequence[-n_frames:]
            
            if len(sequence) == n_frames:
                sequence_array = np.array([sequence])
                sequence_array = (sequence_array - np.min(sequence_array)) / (np.max(sequence_array) - np.min(sequence_array) + 1e-10)
                prediction = model.predict(sequence_array)
                label = 'H' if np.argmax(prediction) == 0 else 'No identification'
                cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Teste Letra H', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()