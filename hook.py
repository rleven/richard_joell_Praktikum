import numpy as np
import matplotlib.pyplot as plt

x = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
print(x)
F = [0.15, 0.29, 0.44, 0.59, 0.74, 0.89, 1.04, 1.19, 1.34, 1.49]
print(F)

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    a[i] = x[i]/F[i]

b = np.sum(a)
print('Der Mittelwert der Federkonstante beträgt: ', b/10, 'kg/s^2.')

plt.plot(x, F, '.', label = 'Messdaten')
plt.xlabel(r"$x$ in [m]")
plt.ylabel(r"$F$ in [N]")
plt.legend(loc = 'best')
plt.show()