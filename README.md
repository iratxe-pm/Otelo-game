# Juego de Otelo (Reversi) con IA ♟️🤖

Este proyecto implementa el clásico juego de **Otelo (Reversi)** con diferentes modos de juego, incluyendo partidas contra la **IA** y simulaciones automáticas.
La inteligencia artificial combina **Monte Carlo Tree Search (MCTS)** y **redes neuronales** para la toma de decisiones estratégicas.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red.svg)](https://keras.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Características principales

✅ Implementación completa del juego de Otelo con validación de reglas y movimientos.✅ Diferentes modos de juego:

- 🎮 **Partida manual** (jugador vs jugador).
- 🧠 **Jugador vs IA**.
- ⚔️ **IA vs IA**.

✅ IA basada en **MCTS** (Monte Carlo Tree Search) para simular jugadas y optimizar decisiones.
✅ Integración de **redes neuronales** para mejorar la calidad de las jugadas.
✅ Código modular: reglas, movimientos, validaciones y partidas organizadas en diferentes módulos.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.9+**
- **NumPy** y **Pandas** (gestión y análisis de datos)
- **TensorFlow / Keras** (IA basada en redes neuronales)
- **MCTS** (Monte Carlo Tree Search)

---

## 📂 Estructura del proyecto

├── documentacion/ # Documentación relevante al desarrollo del proyecto

├── reglas_juego/ # Reglas, validaciones, lógica del juego y posibles excepciones

├── partidas/ # Modos de partida y representación del tablero

├── mcts.py # Implementación de Monte Carlo Tree Search

├── partida_ia_vs_ia.py # Script para simular partidas entre dos IA

├── main.py # Punto de entrada principal

├── partidas_ia_vs_ia.csv # Datos de entrenamiento para la red neuronal

├── requirements.txt # Dependencias del proyecto

└── README.md # Documentación del proyecto

---

## ⚡ Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/iratxe-pm/Otelo-game.git
   cd Otelo-game

   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

   ```
3. Ejecutar el juego:
   ```bash
   python main.py

   ```

---

## 🎯 Resultados

Simulaciones con MCTS permiten a la IA mejorar la calidad de sus jugadas.

Se pueden ejecutar partidas completas: jugador vs jugador, jugador vs IA o IA vs IA.

El sistema es modular y extensible, facilitando futuras mejoras.

---

## 📌 Futuras mejoras

Añadir interfaz gráfica para mejorar la experiencia de usuario.

Optimizar parámetros de MCTS para mayor eficiencia.

---

## 👩‍💻 Autor

Proyecto desarrollado por **Iratxe Parra Moreno** y **María Auxiliadora Quintana Fernández**
como práctica y aprendizaje en IA aplicada a juegos de tablero.
