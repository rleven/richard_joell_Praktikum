import numpy as np
import scipy
import matplotlib.pyplot as plt
a=[4, 8, 10, 12]
b=[5, 10, 15, 20]
plt.plot(a, b, '+r', label='Messwerte')
x=np.linspace(3, 14, 200)
plt.plot(x, 0.13*x**2, '-b', label='const*x²')
plt.ylabel('y in cm')
plt.xlabel('x in mü*100')
plt.legend()
plt.savefig('build/graph.pdf')