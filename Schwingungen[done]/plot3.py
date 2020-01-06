import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
i = 0
x1 = [0, 0, 0, 0, 0, 0]
#x1 = [0, 0, 0, 0, 0, 0]
a = [4.2, 0.8, 0.3, 0.2, 0.1, 0.08]
b = [22.5, 15.5, 11, 10, 8, 7]
y1 = [40, 60, 80, 100, 120, 140]
DataX = [40, 60, 80, 100, 120, 140]
#for i in x:
    #x[i]=a[i]/b[i]*360
    #print(x[i])
    #i=i+1

while i <=5:
    x1[i] = a[i]/b[i]*360
    #print(x[i])
    i += 1
DataY = x1
#m, n, r, p, std = linregress(y, x)
#i=0
#t = np.linspace(40,140)
#while i <6:
    #x1[i] = 67.2*np.exp(-0.02*x[i])
    #i += 1


NOfPoints = 100

XNew = np.linspace(float(DataX[0]), float(DataX[-1]), NOfPoints)
PolyCoeffs = np.polyfit(DataX, DataY, 2)
Polynom    = np.poly1d(np.polyfit(DataX, DataY, 2))

x = list()
y = list()

for i in range(NOfPoints):
    xval = XNew[i]
    x.append( xval )
    y.append( Polynom(xval) )

plt.plot(x, y, '--r', label='Ausgleichskurve')
plt.plot(y1, x1, '+b', label='Messwerte')
#plt.plot(t, 67.2*np.exp(-0.02*t), '-b', label='Vergleich')
plt.xlabel(r'$v$ in $kHz$')
plt.ylabel(r'$\Delta\phi$')
plt.legend(loc='best')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot3.pdf')
