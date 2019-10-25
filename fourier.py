import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

A1 = integrate.fixed_quad(lambda x: abs(np.sin(x))*np.cos(x), -np.pi, np.pi)
print('Ergebnis für A1: ', A1)
B1 = integrate.quad(lambda x: abs(np.sin(x))*np.sin(x), -np.pi, np.pi)
print('Ergebnis für B1: ', B1)
#Nur ein Versuch für Github!

A2 = integrate.quad(lambda x: x*np.cos(x), -np.pi, np.pi)
print('Ergebnis für A2: ', A2)
B2 = integrate.quad(lambda x: x*np.sin(x), -np.pi, np.pi)
print('Ergebnis für B2: ', B2)
#Test für VSCodium!