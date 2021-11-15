import numpy as np
import matplotlib.pyplot as plt
# ray tracing rk2
ds = 0.1

N = 1000
p = np.zeros(2)
dp = np.zeros(2)
xz = np.zeros(2)
thet = 45
v0 = 2
p[0] = np.cos(np.deg2rad(thet)/v0)
p[1] = np.sin(np.deg2rad(thet)/v0)

xz[0] = 0
xz[1] = 0

dv = 0.1
dp[0] = 0
dp[1] = -dv/(v0**2)

v = v0
xz0 = []
fungsi = lambda p, v: p*v

k1 = k2 = 0
for i in range(N-1):

    k1 = fungsi(p, v)*ds
    k2 = fungsi(p + ds, v + k1)*ds

    xz = xz + (0.5*k1) + (0.5*k2)

    p = p + (dp)*ds
    v = v0 + dv*xz[1]

    dp[1] = -dv/(v**2)
    xz0 = np.append(xz0, xz)

print(xz0)
xz0 = np.reshape(xz0, (N-1, 2))
print(xz0)
plt.ylim(25, 0)
plt.plot(xz0[:, 0], xz0[:, 1])
plt.grid()
plt.show()



