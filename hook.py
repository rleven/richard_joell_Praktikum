import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]
e_x = [0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005]
F = [0.15, 0.29, 0.44, 0.59, 0.74, 0.89, 1.04, 1.19, 1.34, 1.49]
e_F = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

m, n, r, p, std = linregress(x, F)
#print(m, n, r, p, std)

for i in range(0, 10):
    y[i] = m*x[i]+n


for i in range(0, 10):
    a[i] = x[i]/F[i]

b = np.sum(a)
print('Der Mittelwert der Federkonstante beträgt: ', b, 'kg/s^2.')
print('Die Steigung der Ausgleichsgerade beträgt: ', m, 'kg/s^2.')

plt.errorbar(x, F, xerr=e_x, yerr=e_F, fmt='b.', label='Messdaten')
plt.plot(x, y, c='red', label = 'Ausgleichsgerade')
plt.xlabel(r"$x$ in [m]")
plt.ylabel(r"$F$ in [N]")
plt.legend(loc = 'best')
#plt.savefig("Ausgleichsgerade.pdf")