import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

R = 271.6
C = 5e-9
L = 0.0035

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
y = [0.8, 0.85, 0.9, 1, 1.2, 1.6, 2, 1.7, 1.1, 0.75, 0.55, 0.43, 0.34, 0.28, 0.24]
t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def func(x):
    return 0.75/(np.sqrt((1-L*C*(x*x))**2+(x*x)*(R*R)*(C*C)))
a = np.linspace(0, 75, 500)
#i=0
#while i<15:
    #t[i]=func(x[i]*10000)
    #i+=1
#print(t)
plt.plot(x, y, '+g', label='Messwerte')
plt.plot(a, func(a*6000), '-b', label='Theorie-Kurve')
#plt.plot(a, b, '-b', label='Vergleich')
plt.xlabel(r'$v$ in $kHz$')
plt.ylabel(r'$U_C$ in $V$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot2.pdf')
