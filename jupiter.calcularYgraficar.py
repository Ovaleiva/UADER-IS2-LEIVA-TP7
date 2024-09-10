import numpy as np
import matplotlib.pyplot as plt

def calcular_esfuerzo(tamano):
    return 8 * tamano**0.95

def calcular_tiempo_calendario(esfuerzo):
    return 2 * 4 * esfuerzo**0.33

tamano_intervalo = np.linspace(0, 10000, 1000)
esfuerzo = calcular_esfuerzo(tamano_intervalo)

esfuerzo_intervalo = np.linspace(1, 500, 1000)
tiempo_calendario = calcular_tiempo_calendario(esfuerzo_intervalo)

fig, axs = plt.subplots(2, 1, figsize=(10, 12))

axs[0].plot(tamano_intervalo, esfuerzo, label='Esfuerzo (E)')
axs[0].set_xlabel('Tamaño del proyecto (S)')
axs[0].set_ylabel('Esfuerzo (E)')
axs[0].set_title('Esfuerzo vs Tamaño del Proyecto')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(esfuerzo_intervalo, tiempo_calendario, label='Tiempo Calendario (td)', color='orange')
axs[1].set_xlabel('Esfuerzo (E)')
axs[1].set_ylabel('Tiempo Calendario (td)')
axs[1].set_title('Tiempo Calendario vs Esfuerzo')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.show()
