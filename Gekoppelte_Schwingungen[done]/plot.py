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

plt.plot(x1, y1, 'r+', label=r"$v^-$")
plt.plot(x1, y2, 'g+', label=r"$v^+$")
plt.plot(x4, v2, 'b-', label=r"Theoriewerte für $v^-$")
plt.plot(x4, v3, 'y-', label=r"Theoriewerte für $v^+$")
plt.xlabel('C in nF')
plt.ylabel('f in Hz')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
plt.close()

i=0
w1 = [24.962, 24.972, 24.978, 24.978, 24.984, 24.978, 24.978]
w2 = [24.987, 24.928, 24.957, 24.965, 24.971, 24.967, 24.970]
x1 = [2.03, 3.00, 4.00, 5.02, 6.47, 8.00, 9.99]
plt.plot(x1, w1, '-y', label=r'$v^+$')
plt.plot(x1, w2, '-r', label=r'$v^-$')
plt.xlabel(r'$C_\mathrm{k}$ in nF')
plt.ylabel(r'$v$ in kHz')
plt.legend(loc= 'best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')

print(1/(np.sqrt(3.2351e-2*8.015e-10)))
print(1/(np.sqrt(3.2351e-2*(8.015e-10+3.7e-11))))