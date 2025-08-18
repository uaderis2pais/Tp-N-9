# Importar librerías
import numpy as np
import matplotlib.pyplot as plt

# Fórmulas
def calcular_esfuerzo(S):
    return 8 * (S ** 0.95)

def calcular_tiempo(E):
    return 2.4 * (E ** 0.33 )

# Intervalos
S = np.linspace(0, 10000, 500)   # 500 puntos entre 0 y 10000
E = calcular_esfuerzo(S)

E_range = np.linspace(1, 500, 500)
td = calcular_tiempo(E_range)

# Graficar Esfuerzo vs Tamaño
plt.figure(figsize=(8, 5))
plt.plot(S, E, label="Esfuerzo (E)")
plt.title("Esfuerzo en función del tamaño del proyecto")
plt.xlabel("Tamaño del Proyecto (S)")
plt.ylabel("Esfuerzo (E)")
plt.grid(True)
plt.legend()
plt.show()

# Graficar Tiempo vs Esfuerzo
plt.figure(figsize=(8, 5))
plt.plot(E_range, td, color='orange', label="Tiempo (td)")
plt.title("Tiempo en función del Esfuerzo")
plt.xlabel("Esfuerzo (E)")
plt.ylabel("Tiempo (td)")
plt.grid(True)
plt.legend()
plt.show()
