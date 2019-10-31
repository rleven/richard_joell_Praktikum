import numpy as np
import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(x)
F = [0.15, 0.29, 0.44, 0.59, 0.74, 0.89, 1.04, 1.19, 1.34, 1.49]
print(F)

a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    a[i] = x[i]/F[i]

b = np.sum(a)
print(a, b/10)