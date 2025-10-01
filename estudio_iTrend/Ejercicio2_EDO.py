# Ejercicio 2 EDO simple
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt



b = 0.0
c = 1.0

y0 = [1.0, 0.0]
t = np.linspace(1, 10, 101)

sol = odeint(pend, y0, t, args=(b, c))

print(sol)


plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()