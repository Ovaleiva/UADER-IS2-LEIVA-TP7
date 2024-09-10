import numpy as np
import matplotlib.pyplot as plt

# Constantes del modelo (valores típicos para proyectos orgánicos en COCOMO)
a = 2.4  # Constante para calcular el esfuerzo
b = 1.05 # Exponente para el esfuerzo
c = 2.5  # Constante para calcular el tiempo
d = 0.38 # Exponente para el tiempo

# Función para calcular el esfuerzo basado en el tamaño
def calcular_esfuerzo(S):
    return a * S**b

# Función para calcular el tiempo basado en el esfuerzo
def calcular_tiempo(E):
    return c * E**d

# Generar los datos para el tamaño del proyecto (S) y el esfuerzo (E)
tamanos = np.linspace(0, 10000, 100)  # Tamaño del proyecto de 0 a 10000 KLOC
esfuerzos = calcular_esfuerzo(tamanos)

# Generar los datos para el esfuerzo (E) y el tiempo (td)
esfuerzos_intervalo = np.linspace(1, 500, 100)  # Esfuerzo de 1 a 500 persona-meses
tiempos = calcular_tiempo(esfuerzos_intervalo)

# Graficar esfuerzo (E) en función del tamaño (S)
plt.figure(figsize=(12, 6))

# Gráfico 1: Esfuerzo en función del tamaño del proyecto
plt.subplot(1, 2, 1)
plt.plot(tamanos, esfuerzos, label='Esfuerzo (E)', color='blue')
plt.xlabel('Tamaño del proyecto (KLOC)')
plt.ylabel('Esfuerzo (persona-meses)')
plt.title('Esfuerzo en función del tamaño del proyecto')
plt.grid(True)
plt.legend()

# Gráfico 2: Tiempo en función del esfuerzo
plt.subplot(1, 2, 2)
plt.plot(esfuerzos_intervalo, tiempos, label='Tiempo (td)', color='green')
plt.xlabel('Esfuerzo (persona-meses)')
plt.ylabel('Tiempo (meses)')
plt.title('Tiempo en función del esfuerzo')
plt.grid(True)
plt.legend()

# Mostrar gráficos
plt.tight_layout()
plt.show()
