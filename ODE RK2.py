""""
Iqram Haris Fahromi
12320021
"""
import numpy as np
import matplotlib.pyplot as plt

n = 100
t = np.linspace(1, 2, n)
h = dt = t[1] - t[0]
T = np.zeros(n)
T2 = np.zeros(n)
T2 = 0.5*np.exp(0.5*(t**2))

T[0] = 0.5

fungsi = lambda T, t: t*T

k1 = k2 = 0
for i in range(n-1):
    k1 = fungsi(t[i], T[i])*h
    k2 = fungsi(t[i] + h, T[i]+k1)*h
    T[i+1] = T[i] + (k1+k2)/2

trun_error = abs(T2-T)

plt.plot(t, trun_error, color = 'green', label = 'Truncation Error')
plt.plot(t, T, color = 'red', label = 'Runge-Kutta orde 2')

plt.grid()
plt.legend()
plt.show()