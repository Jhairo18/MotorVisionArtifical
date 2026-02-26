# 🚀 Control de Velocidad de Motor con Visión Artificial

Sistema inteligente que controla la velocidad de un motor DC mediante gestos manuales detectados en tiempo real. El proyecto integra visión computacional con sistemas embebidos.

---
## 🎥 Demo del Proyecto
Video de demostración en TikTok:  
[Ver en TikTok](https://www.tiktok.com/@jhairoypp/video/7547905001130085639)
## 📂 Estructura del Proyecto

El proyecto se divide en dos componentes principales:

* **`src/main.py`**: Lógica de Visión Artificial (detección de dedos y procesamiento de imagen).
* **`src/main.cpp`**: Control de hardware y señales PWM con Arduino.

---

## 🧠 Descripción General

El sistema utiliza la cámara del computador para detectar la cantidad de dedos levantados. Este valor se procesa y se envía como un nivel de intensidad al Arduino, el cual ajusta la velocidad del motor mediante **PWM (Pulse Width Modulation)**.

### 🔄 Arquitectura del Flujo
`Cámara` ➡️ `Python (MediaPipe)` ➡️ `Nivel (0–9)` ➡️ `Serial/Arduino` ➡️ `Señal PWM` ➡️ `Motor DC`

---

## 🖥️ Parte 1: Visión Artificial (Python)

### Tecnologías:
* **OpenCV**: Procesamiento de video y renderizado.
* **MediaPipe**: Framework de Google para el tracking de manos y puntos de referencia.

### Funcionalidad:
1. Captura de video en tiempo real.
2. Detección de puntos clave de la mano (*landmarks*).
3. Conteo de dedos levantados mediante lógica de posición de falanges.
4. Envío del nivel detectado al microcontrolador.

---

## 🔌 Parte 2: Control de Hardware (Arduino/C++)

El firmware gestiona la potencia entregada al motor basándose en el nivel recibido:

* **Dirección:** Controlada vía pines `IN3` e `IN4`.
* **Velocidad:** Controlada mediante el pin `ENB` (PWM).
* **Feedback Visual:** Implementación de un display binario de 4 bits para visualizar el nivel actual.

### Lógica de Control:
El sistema mapea el rango de dedos (0-9) al rango de trabajo del motor:

```cpp
// Ejemplo de mapeo en C++
int pwm = map(nivel, 0, 9, 70, 255);
analogWrite(ENB, pwm);
```
## ⚙️ Hardware Utilizado

| Componente | Función |
| :--- | :--- |
| **Arduino (Uno/Nano)** | Procesamiento de señales y control lógico del sistema. |
| **Driver Puente H (L298N/L293D)** | Gestión de la etapa de potencia y dirección del motor. |
| **Motor DC** | Actuador final cuya velocidad es regulada. |
| **Display Binario (4 bits)** | Interfaz visual para confirmar el nivel detectado (0-9). |
| **Cámara Web** | Sensor de entrada para la captura de gestos (Visión Artificial). |

---

## 📊 Mapeo de Velocidad

El sistema traduce el conteo de dedos a un ciclo de trabajo PWM para ajustar el torque y la velocidad del motor:

| Nivel (Dedos) | Valor PWM | Estado de Velocidad |
| :---: | :---: | :--- |
| **0** | 70 | **Mínimo** (Umbral de arranque) |
| **5** | ~180 | **Media** (Velocidad crucero) |
| **9** | 255 | **Máxima** (100% Potencia) |



---

## 🎯 Aplicaciones

Este proyecto sienta las bases para diversas implementaciones en tecnología e industria:

* **Control Gestual:** Desarrollo de interfaces hombre-máquina (HMI) de próxima generación.
* **Automatización Industrial:** Control de bandas transportadoras o procesos sin contacto físico (entornos estériles).
* **Robótica:** Manipulación de robots y actuadores mediante telemetría visual.
* **Accesibilidad:** Creación de herramientas de asistencia para personas con movilidad reducida.

---

## 👨‍💻 Autor
**Jhairo Yurivilca**
