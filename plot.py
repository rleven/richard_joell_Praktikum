import matplotlib.pyplot as plt
import numpy as np
R = 30
C = 5e-6
L = 0.0035
x = [0, 25e-6, 54e-6, 78e-6, 105e-6, 130e-6, 158e-6, 184e-6, 210e-6, 247e-6]
y = [0.2, 0.14, 0.1, 0.07, 0.05, 0.04, 0.03, 0.02, 0.014, 0.008]
a = np.linspace(0, 250e-6, 1000)
b = 0.2*np.exp(-R/(2*L)*a)
#plt.subplot(1, 2, 1)
plt.plot(x, y, '+r', label='Messwerte')
plt.plot(a, b, '-g', label='Vergleich')
plt.xlabel(r'$s$')
plt.ylabel(r'$V$')
plt.legend(loc='best')

#plt.subplot(1, 2, 2)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
#plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
#plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
