import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt('datos1.csv', delimiter=',')

plt.plot(datos[:,0], datos[:,1], label='Fuerza Bruta')
plt.plot(datos[:,0], datos[:,2], label='D&Q up')
plt.plot(datos[:,0], datos[:,3], label='D&Q bubble')
plt.plot(datos[:,0], datos[:,4], label='D&Q merge')
plt.plot(datos[:,0], datos[:,5], label='D&Q quick')
plt.xlabel('largo de listas', color='blue')
plt.ylabel('tiempo de ejecucion (s)', color= 'blue')
plt.legend()
plt.show()
