<h1 align="center">
  <br>
  Desarrollado por
  <br>
  <a href="https://github.com/ViCode321" target="_blank">ViCode321</a>
  <br>
</h1>

<h4 align="center">Detector de Alfabeto en Lenguaje de Señas con Python y <a href="https://yolov8.com/" target="_blank">YOLOv8</a></h4>

<p align="center">
  <a href="#contexto">Contexto</a> •
  <a href="#requisitos">Requisitos</a> •
  <a href="#modelo-entrenado">Modelo entrenado</a> •
  <a href="#instalacion-y-uso">Instalación y uso</a> •
  <a href="#dependencias">Dependencias</a> •
  <a href="#como-funciona">¿Cómo funciona?</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/docker-library/docs/01c12653951b2fe592c1f93a13b4e289ada0e3a1/python/logo.png" alt="python" height="100"/>
  <img src="https://cdn.sanity.io/images/k7elabj6/production/43ed2a0bd025b8f5d7ef611cc85726af8c3da57a-252x264.svg" alt="yolov8" height="100"/>
  <img src="icon/logo.png" alt="roboflow" height="100"/>
</p>

# Contexto

Este proyecto implementa un detector de letras del **lenguaje de señas americano (ASL)** usando **YOLOv8**. A través de la cámara web de tu computadora, reconoce las letras en tiempo real y las pronuncia en voz alta mediante **síntesis de voz offline** con `pyttsx3`.

---

## Requisitos

- Python 3.8 o superior  
- Cámara web funcional  
- Sistema operativo compatible (Windows, Linux o macOS)  
- Entorno local (no funciona en Google Colab para cámara y voz)

---

## Modelo entrenado

Se utlizó un dataset con mas de 700 imágenes que provienen de un workspace de [Roboflow](https://roboflow.com/), puedes ver cómo se entrenó el modelo en Google Colab con este dataset haciendo clic aquí:  
📎 [Google Colab - Entrenamiento del modelo](https://colab.research.google.com/drive/1ECUquYyBYq3z-AQDh3JGNbyAbcNuXlvO?usp=sharing)

---

## Instalacion y uso

1. Clona este repositorio:

```bash
git clone https://github.com/ViCode321/ia-sign-language.git
cd ia-sign-language
```

2. Crea un entorno virtual:
```bash
python -m venv myvenv
```

3. Activar entorno virtual
```bash
source myvenv/Scripts/activate
```

4. Instalar dependencias
```bash
pip install -r requirements.txt
```

5. Descargar dataset generado por Modelo de GoogleColab
```bash
/data/best.pt
```
6. Ejecutar
```bash
python ia_sign_reader.py
``` 

## Dependencias

```bash
ultralytics==8.0.178
opencv-python
pyttsx3
numpy
```

---

## Como funciona

* El modelo YOLOv8 detecta letras del lenguaje de señas desde la cámara.

* Cuando identifica una letra con confianza suficiente, la dice en voz alta.

* Funciona completamente offline y en tiempo real.

## Créditos

[David Lee](https://universe.roboflow.com/david-lee-d0rhs)
