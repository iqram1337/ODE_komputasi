import numpy as np
import matplotlib.pyplot as plt

### ODE Metode EULER
n = 1001
t = np.linspace(1, 2, n)
dt = t[1] - t[0]
T = np.zeros(n)
T2 = np.zeros(n)
T[0] = 0.5
T2 = 0.5*np.exp(0.5*(t**2))

for i in range(0, n-1, 1):
    T[i+1] = T[i] + t[i]*T[i]*dt


errort = abs(T2-T)
plt.plot(t, errort, label = 'Truncation Error')
plt.plot(t, T, color = 'red', label = 'Euler Method')

plt.legend()
plt.grid()
plt.xlabel('t(m/s)', color = 'blue')
plt.ylabel('Euler & Error', color = 'red')

plt.show()