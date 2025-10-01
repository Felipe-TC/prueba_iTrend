# Ejercicio 2 EDO simple
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

condiciones_iniciales_read = pd.read_csv('condiciones_iniciales.txt')
#print(condiciones_iniciales_read)

condiciones_iniciales_array = np.array(condiciones_iniciales_read)
print(condiciones_iniciales_array)

b = 0.0
c = 1.0

y0 = condiciones_iniciales_array[0]
t = np.linspace(1, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))

#print(sol)


plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()