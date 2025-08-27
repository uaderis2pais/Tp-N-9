import matplotlib.pyplot as plt
import numpy as np


# Datos históricos
LOC = np.array([794, 1336, 1572, 1572, 1126])
E_hist = np.array([1.07, 1.34, 2.27, 2.39, 0.93])


# Modelo exponencial
k = 0.000046
b = 1.392


LOC_range = np.linspace(200, 10000, 200)
E_model = k * LOC_range**b


# Predicciones
LOC_pred = [9100, 200]
E_pred = [k * loc**b for loc in LOC_pred]


# Graficar
plt.figure(figsize=(8,6))
plt.scatter(LOC, E_hist, color="black", label="Datos históricos")
plt.plot(LOC_range, E_model, color="red", label="Modelo exponencial ajustado")
plt.scatter(LOC_pred, E_pred, color="blue", marker="x", s=100, label="Predicciones")


for loc, e in zip(LOC_pred, E_pred):
    plt.text(loc, e+2, f"({loc}, {e:.2f})", ha="center", fontsize=9)


plt.xlabel("Tamaño del proyecto (LOC)")
plt.ylabel("Esfuerzo (persona-mes)")
plt.title("Ajuste de Modelo Exponencial y Predicciones")
plt.legend()
plt.grid(True)


plt.savefig("modelo_exponencial.png", dpi=300)  # Guarda el gráfico como imagen
plt.show()
