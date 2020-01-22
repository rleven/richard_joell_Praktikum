import numpy as np
import csv

x1 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=0)
x2 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=1)
x3 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=2)
x4 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=3)
x5 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=4)
x6 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=5)
x7 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=6)
x8 = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=7)
t = np.genfromtxt("content/static_45c.csv",delimiter=',',unpack=True,usecols=8)

i=10
while i<51:
    print(x7[i]-x8[i])
    i+=10

print("haha ", -14.4*48e-6*10.48/0.03)