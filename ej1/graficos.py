import numpy as np
import matplotlib.pyplot as plt


datoscsv = np.loadtxt('datos1.csv', delimiter=',')
plt.plot(datos[:,0], datos[:,1], label='Fuerza Bruta')
plt.legend()
