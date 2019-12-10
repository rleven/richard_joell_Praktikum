import matplotlib.pyplot as plt
import numpy as np

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
y = [0.8, 0.85, 0.9, 1, 1.2, 1.6, 2, 1.7, 1.1, 0.75, 0.55, 0.43, 0.34, 0.28, 0.24]

plt.plot(x, y, '+g', label='Messwerte')
#plt.plot(a, b, '-b', label='Vergleich')
plt.xlabel(r'$kHz$')
plt.ylabel(r'$V$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
