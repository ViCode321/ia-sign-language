import cv2
import pyttsx3
from ultralytics import YOLO
import time

# Inicializar síntesis de voz
voz = pyttsx3.init()
voz.setProperty('rate', 150)

# Cargar modelo
modelo = YOLO("data/best.pt")
clases = modelo.model.names  # Obtener nombres de clases

# Iniciar captura de video
cap = cv2.VideoCapture(0)

# Control de tiempo y letras pronunciadas
ultima_letra = ""
tiempo_ultimo = time.time()

print("🔍 Iniciando detección. Presiona 'q' para salir.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)  # Mejora brillo

    # Realizar predicción
    resultados = modelo.predict(source=frame, conf=0.5, verbose=False)
    #resultados = modelo.predict(source=frame, conf=0.25, verbose=False)

    boxes = resultados[0].boxes

    if boxes:
        for box in boxes:
            cls_id = int(box.cls[0])
            letra = clases[cls_id]

            # Dibujar bounding box y etiqueta
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, letra, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Pronunciar solo si es una letra nueva o pasó tiempo
            if letra != ultima_letra or (time.time() - tiempo_ultimo) > 2:
                voz.say(letra)
                voz.runAndWait()
                ultima_letra = letra
                tiempo_ultimo = time.time()
            break  # Solo procesa la primera detección relevante

    # Mostrar video en pantalla
    cv2.imshow("Detección de Lengua de Señas", frame)

    # Salida con tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
