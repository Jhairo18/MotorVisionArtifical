import cv2
import mediapipe as mp
import time
# Inicializar MediaPipe y OpenCV
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Función para contar dedos levantados
def contar_dedos(mano_landmarks, mano_label):
    dedos = []
    tips = [4, 8, 12, 16, 20]

    # Pulgar (compara eje X, cambia según la mano)
    if mano_label == "Right":
        if mano_landmarks.landmark[tips[0]].x < mano_landmarks.landmark[tips[0] - 1].x:
            dedos.append(1)
        else:
            dedos.append(0)
    else:  # Mano izquierda
        if mano_landmarks.landmark[tips[0]].x > mano_landmarks.landmark[tips[0] - 1].x:
            dedos.append(1)
        else:
            dedos.append(0)

    # Índice a meñique (compara eje Y)
    for id in range(1, 5):
        if mano_landmarks.landmark[tips[id]].y < mano_landmarks.landmark[tips[id] - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return sum(dedos)

# Captura de video
cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        total_dedos = 0
        # Si se detectan manos y sus etiquetas
        if results.multi_hand_landmarks and results.multi_handedness:
            for mano_landmarks, mano_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                mano_label = mano_info.classification[0].label  # "Left" o "Right"
                dedos_levantados = contar_dedos(mano_landmarks, mano_label)
                total_dedos += dedos_levantados
                # Dibujar puntos y conexiones
                mp_drawing.draw_landmarks(frame, mano_landmarks, mp_hands.HAND_CONNECTIONS)

                # Mostrar texto sobre el video
                coord_x = int(mano_landmarks.landmark[0].x * frame.shape[1])
                coord_y = int(mano_landmarks.landmark[0].y * frame.shape[0]) - 20
                cv2.putText(frame, f"{mano_label}: {dedos_levantados}", (coord_x, coord_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print(f"{total_dedos} dedos levantados")
        # Mostrar ventana
        cv2.imshow("Detector de Dedos", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
"Ref https://www.youtube.com/watch?v=ipHKQVtwRas&list=PLBg7GSvtrU2OaYp2F-FqqZk0RUB4IUvvb&index=3"

