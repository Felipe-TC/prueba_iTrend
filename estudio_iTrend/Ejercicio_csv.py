# Importar librerias
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#print("Hola mundo")
dv = pd.read_csv('datos_ventas.csv')

#print(dv)
dv_array = np.array(dv)

#print(dv_array)
#print(dv_array[0, 1])


total_ventas_por_producto = dv_array[:, 2] * dv_array[:, 3]
print(total_ventas_por_producto)
