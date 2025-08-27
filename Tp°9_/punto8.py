# PNR_sistemis_mod.py
# Versión modificada para resolver consigna (a, b y c) del punto 8)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Definición de funciones del modelo PNR ---
def esfuerzo_instantaneo(t, a, K=1):
    """Esfuerzo instantáneo (PM por unidad de tiempo)"""
    return 2 * K * a * t * np.exp(-a * t**2)

def esfuerzo_acumulado(t, a, K=1):
    """Esfuerzo acumulado hasta tiempo t"""
    return K * (1 - np.exp(-a * t**2))


# --- Dataset histórico (del taller) ---
t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])        # Tiempo (meses)
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])  # Esfuerzo (PM)

# Esfuerzo total histórico
K_hist = np.sum(E_data)

# Calibrar parámetro "a" con datos históricos
popt, _ = curve_fit(lambda t, a: esfuerzo_instantaneo(t, a, K_hist),
                    t_data, E_data, p0=[0.1])
a_estimada = popt[0]

print(f"Esfuerzo total histórico: K = {K_hist:.1f} PM")
print(f"Parámetro a estimado: a = {a_estimada:.4f}")


# === (a) Gráfico con dataset, modelo calibrado y proyecto dado ===
K_usuario = float(input("Ingrese esfuerzo total en PM (72 para el punto b): ") or 72)

t_fit = np.linspace(min(t_data), max(t_data), 200)
E_fit_hist = esfuerzo_instantaneo(t_fit, a_estimada, K_hist)        # histórico suavizado
E_fit_usuario = esfuerzo_instantaneo(t_fit, a_estimada, K_usuario)  # proyecto nuevo

plt.scatter(t_data, E_data, label="Histórico (datos)", color="black")
plt.plot(t_fit, E_fit_hist, label="Modelo calibrado (histórico)", color="red")
plt.plot(t_fit, E_fit_usuario, label=f"Proyecto {K_usuario:.0f} PM", color="blue")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Esfuerzo instantáneo (PM)")
plt.legend()
plt.title("PNR - Histórico vs Modelo vs Proyecto dado")
plt.show()


# === (b) Distribución acumulada ===
E_acum_hist = esfuerzo_acumulado(t_fit, a_estimada, K_hist)
E_acum_usuario = esfuerzo_acumulado(t_fit, a_estimada, K_usuario)

plt.plot(t_fit, E_acum_hist, label="Acumulado histórico (suavizado)", color="red")
plt.plot(t_fit, E_acum_usuario, label=f"Acumulado proyecto {K_usuario:.0f} PM", color="blue")
plt.scatter(t_data, np.cumsum(E_data), label="Acumulado real", color="black")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Esfuerzo acumulado (PM)")
plt.legend()
plt.title("Distribución de esfuerzo acumulado en el tiempo")
plt.show()


# === (c) Efecto de multiplicar 'a' ×4 ===
a_mod = 4 * a_estimada
E_fit_mod = esfuerzo_instantaneo(t_fit, a_mod, K_usuario)

plt.plot(t_fit, E_fit_usuario, label=f"Normal (a={a_estimada:.4f})", color="blue")
plt.plot(t_fit, E_fit_mod, label=f"a x4 (a={a_mod:.4f})", color="orange")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Esfuerzo instantáneo (PM)")
plt.legend()
plt.title("Efecto de multiplicar 'a' ×4 → Zona imposible")
plt.show()
