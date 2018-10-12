import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt('datos1.csv', delimiter=',')

plt.plot(datos[:,0], datos[:,1], label='Fuerza bruta')
plt.plot(datos[:,0], datos[:,2], label='D&Q Upsort')
plt.plot(datos[:,0], datos[:,3], label='D&Q Bubble sort')
plt.plot(datos[:,0], datos[:,4], label='D&Q Merge sort')
plt.plot(datos[:,0], datos[:,5], label='D&Q Quicksort')
plt.xlabel('Cantidad de elementos')
plt.ylabel('Tiempo de ejecucion (s)')
plt.legend()
plt.show()
