import cv2
import mediapipe as mp
import numpy as np
import os

# Configurar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Configurar captura de vídeo
cap = cv2.VideoCapture(0)
class_name = 'not_h'  # Mude para 'not_h' para coletar gestos não-H
output_dir = f'../dataset/{class_name}'
os.makedirs(output_dir, exist_ok=True)

# Contar arquivos existentes para continuar a numeração
existing_files = [f for f in os.listdir(output_dir) if f.endswith('.npy')]
video_count = len(existing_files)  # Inicia a partir do próximo índice
max_videos = video_count + 100  # Adiciona 100 vídeos
frames_per_video = 20
sequence = []

while cap.isOpened() and video_count < max_videos:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível ler o frame da webcam.")
        break
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        print("Mão detectada!")
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])
            sequence.append(landmarks)
            print(f"Frames capturados: {len(sequence)}")
    
        if len(sequence) >= frames_per_video:
            sequence_array = np.array(sequence[:frames_per_video])
            np.save(f'{output_dir}/video_{video_count}.npy', sequence_array)
            print(f'Salvo: video_{video_count}.npy')
            video_count += 1
            sequence = []
    else:
        print("Nenhuma mão detectada neste frame.")
    
    cv2.imshow('Captura', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Encerrado pelo usuário.")
        break

cap.release()
cv2.destroyAllWindows()
print(f"Total de vídeos salvos: {video_count}")