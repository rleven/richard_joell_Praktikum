import numpy as np
import matplotlib.pyplot as plt

R = 50
L = 3.2351e-2
C = 8.385e-10
i=0

def lomegaplus(Ck):
    return 1/(R*np.sqrt(4+(R*R*Ck*Ck)/(L*C)))

def lomegaminus(Ck):
    return 1/(R*np.sqrt(4+(R*R*Ck*Ck)/(L*C)*(1+C/Ck)))

def vminus(Ck):
    return 1/(2*np.pi*np.sqrt(L/(1/C+2/Ck)))

C_k = [2.03e-9, 3.00e-9, 4.00e-9, 5.02e-9, 6.47e-9, 8.00e-9, 9.99e-9]
w1 = [0, 0, 0, 0, 0, 0, 0]
w2 = [0, 0, 0, 0, 0, 0, 0]
v1 = [39990, 37275, 35730, 34760, 33870, 33260, 32740]
v2 = [0, 0, 0, 0, 0, 0, 0]
ref = [0, 0, 0, 0, 0, 0, 0]

while i<7:
    w1[i] = lomegaplus(C_k[i])
    w2[i] = lomegaminus(C_k[i])
    v2[i] = vminus(C_k[i])
    ref[i] = (1-v1[i]/v2[i])*100
    i+=1



print("L+ : ", w1)
print("L- : ", w2)
print("Approximation: ", 1/(2*R))
I2 = 8*0.01
print("Finalwerte für I2: ", I2)
print("v- Werte: ", vminus(1.01e-9))
print("Abweichung: ", (1-47090/vminus(1.01e-9))*100)