import numpy as np
import matplotlib.pyplot as plt
# ray tracing euler
ds = 0.1

N = 600
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
for i in range(N-1):
    xz = xz + (p*v)*ds
    p = p + (dp)*ds
    v = v0 + dv*xz[1]
    # v2 = v0
    dp[1] = -dv/(v**2)
    # dp[1] = ((1/v2) - (1/v))/ (xz[])
    xz0 = np.append(xz0, xz)

print(xz0)
xz0 = np.reshape(xz0, (N-1, 2))
print(xz0)
plt.ylim(20, 0)
plt.plot(xz0[:, 0], xz0[:, 1])
plt.grid()
plt.show()



