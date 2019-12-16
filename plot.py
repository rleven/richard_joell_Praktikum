import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import uncertainties.unumpy as unp
from uncertainties import ufloat

i=0
x = [2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
y = [4, 5, 5, 6, 8, 11, 14]

while i<7:
    x[i] = ufloat(x[i], x[i]*0.003)
    i+=1

m, n, a, b, c = linregress(unp.nominal_values(x), y)
z = np.linspace(2, 10, 500)
z_y = m*z+n

del a, b, c

plt.plot(z, z_y, '-b', label = "Ausgleichsgerade")
plt.errorbar(unp.nominal_values(x), y, xerr=unp.std_devs(x), fmt='r.', label='Messwerte')
plt.xlabel('C in nF')
plt.ylabel('Anzahl Maxima')
plt.legend()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()

x1 = [1.01, 2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
y1 = [47090, 39990, 37275, 35730, 34760, 33870, 33260, 32740]
y2 = [30450, 30440, 30440, 30440, 30440, 30440, 30440, 30440]

plt.plot(x1, y1, 'r+', label="v-")
plt.plot(x1, y2, 'g+', label="v+")
plt.xlabel('C in nF')
plt.ylabel('f in Hz')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()

i=0
a1 = [1.75, 1.75, 1.75, 1.75, 1.75, 1.8, 1.8]
a2 = [1.4, 1.5, 1.55, 1.55, 1.6, 1.6, 1.6]
a = [17.5, 18, 18, 17.5, 17.5, 17.5, 18]
b = [29.5, 21.5, 16.5, 13.5, 10.5, 8.5, 6.5]
s = [47, 39.5, 34.5, 31, 28, 26, 24.5]
plt.plot(a, a1, '.y', label='Erste Amplitude')
plt.plot(s, a2, '.r', label='Zweite Amplitude')
plt.xlabel('t in ms')
plt.ylabel('U in V')
plt.legend(loc= 'best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')