import cv2
import pyttsx3
from ultralytics import YOLO
import time

# Inicializar síntesis de voz
voz = pyttsx3.init()
voz.setProperty('rate', 150)  # velocidad

# Cargar el modelo entrenado (ajusta la ruta si es necesario)
modelo = YOLO("data/best.pt")

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Tiempo entre pronunciaciones
tiempo_ultimo = time.time()
ultima_letra = ""

print("🔍 Iniciando detección. Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar predicción
    resultados = modelo.predict(source=frame, conf=0.5, verbose=False)
    anotaciones = resultados[0].boxes
    clases = resultados[0].names

    if anotaciones is not None and len(anotaciones) > 0:
        for box in anotaciones:
            cls_id = int(box.cls[0].item())
            letra = clases[cls_id]

            # Dibujar el bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, letra, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Decir la letra si ha pasado suficiente tiempo y es nueva
            if letra != ultima_letra or time.time() - tiempo_ultimo > 2:
                voz.say(letra)
                voz.runAndWait()
                ultima_letra = letra
                tiempo_ultimo = time.time()

    # Mostrar el video
    cv2.imshow("Detección de Lenguaje de Señas", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
