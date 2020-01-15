import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import uncertainties.unumpy as unp
from uncertainties import ufloat

R = 50
L = 3.2351e-2
C = 8.385e-10
i=0
x = [2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
y = [4, 5, 5, 6, 8, 11, 14]
y_1 = [3, 4, 6, 7, 8, 10, 13]

while i<7:
    x[i] = ufloat(x[i], x[i]*0.003)
    i+=1

m, n, a, b, c = linregress(unp.nominal_values(x), y)
z = np.linspace(2, 10, 500)
z_y = m*z+n
del a, b, c
d, f, a, b, c = linregress(unp.nominal_values(x), y_1)
z_y_1 = d*z+f
del a, b, c

#plt.plot(z, z_y, '-b', label = "Ausgleichsgerade Max")
#plt.plot(z, z_y_1, '-y', label= "Ausgleichsgerade Min")
plt.errorbar(unp.nominal_values(x), y, xerr=unp.std_devs(x), fmt='r.', label='Maxima')
plt.errorbar(unp.nominal_values(x), y_1, xerr=unp.std_devs(x), fmt='g.', label='Minima')
plt.xlabel('C in nF')
plt.ylabel('Anzahl Extrema')
plt.legend()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
plt.close()

x1 = [1.01, 2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
y1 = [47090, 39990, 37275, 35730, 34760, 33870, 33260, 32740]
y2 = [30450, 30440, 30440, 30440, 30440, 30440, 30440, 30440]
x4 = np.linspace(1, 10, 500)
v2 = 1/(2*np.pi*np.sqrt(L/(1/C+2/(x4*10**(-9)))))
v3 = 1/(2*np.pi*np.sqrt(L*C))*x4/x4

plt.plot(x1, y1, 'r+', label="v-")
plt.plot(x1, y2, 'g+', label="v+")
plt.plot(x4, v2, 'b-', label="Theoriewerte v-")
plt.plot(x4, v3, 'y-', label="Theoriewerte v+")
plt.xlabel('C in nF')
plt.ylabel('f in Hz')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()

i=0
w1 = [2733.28125, 2811.375, 2811.375, 2733.28125, 2733.28125, 2733.28125, 2811.375]
w2 = [7340.8125, 6169.40625, 5388.46875, 4841.8125, 4373.25, 4060.875, 3826.59375]
x1 = [2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
plt.plot(x1, w1, '.y', label='Omega+')
plt.plot(x1, w2, '.r', label='Omega-')
plt.xlabel('C_k in nF')
plt.ylabel('Omega in kHz')
plt.legend(loc= 'best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')

print(1/(np.sqrt(3.2351e-2*8.015e-10)))
print(1/(np.sqrt(3.2351e-2*(8.015e-10+3.7e-11))))