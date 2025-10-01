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
#print(total_ventas_por_producto)

mean_of_sells = np.mean(dv_array[:, 2])
#print(mean_of_sells)

#Detectar si hay algun producto con venta total mayor a 1000

for valorsito in total_ventas_por_producto:
    if valorsito > 1000:
        print("efectivamente")
        break

total_ventas_por_producto_con_nombres = np.vstack([dv_array[:, 1], total_ventas_por_producto])
#print(np.transpose(total_ventas_por_producto_con_nombres))
#print(total_ventas_por_producto_con_nombres[0])

plt.bar(total_ventas_por_producto_con_nombres[0], total_ventas_por_producto_con_nombres[1])
print(total_ventas_por_producto_con_nombres)
print(total_ventas_por_producto_con_nombres[1])
plt.show()
