import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
i = 0
x = [0, 0, 0, 0, 0, 0]
#x1 = [0, 0, 0, 0, 0, 0]
a = [4.2, 0.8, 0.3, 0.2, 0.1, 0.08]
b = [22.5, 15.5, 11, 10, 8, 7]
y = [40, 60, 80, 100, 120, 140]

#for i in x:
    #x[i]=a[i]/b[i]*360
    #print(x[i])
    #i=i+1

while i <=5:
    x[i] = a[i]/b[i]*360
    print(x[i])
    i += 1

#m, n, r, p, std = linregress(y, x)

#while i <=5:
    #x1[i] = m*y[i]+n
    #i += 1

plt.plot(y, x, '+g', label='Messwerte')
#plt.plot(y, x1, '-b', label='Vergleich')
plt.xlabel(r'$kHz$')
plt.ylabel(r'$\Delta\phi$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')
