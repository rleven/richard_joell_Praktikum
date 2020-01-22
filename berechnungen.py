import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy
from scipy.signal import argrelextrema
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

del x1, x2, x3, x4, x5, x6, x7, x8, t

x1 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=1)
x2 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=2)
x3 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=3)
x4 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=4)
x5 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=5)
x6 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=6)
x7 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=7)
x8 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=8)
t = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=9)

#print(argrelextrema(x2, np.greater))
#print(argrelextrema(x2, np.less))
#print(x2[9], x2[25], x2[42], x2[58], x2[74], x2[90], x2[106], x2[122])
#print(t[9], t[25], t[42], t[58], t[74], t[90], t[106], t[122])
#print("_______")
#print(x2[17], x2[33], x2[49], x2[66], x2[82], x2[98], x2[114])
#print(t[17], t[33], t[49], t[66], t[82], t[98], t[114])
print(argrelextrema(x8, np.greater))
print(argrelextrema(x7, np.greater))

s = 1
s1 = 0.5
a = [8, 9, 10, 10, 11, 11, 11, 11.5, 11.5, 11.5, 11, 11.5, 11, 11.5, 11.5]
a0 = ufloat(a[0], s)
a1 = ufloat(a[1], s)
a2 = ufloat(a[2], s)
a3 = ufloat(a[3], s)
a4 = ufloat(a[4], s)
a5 = ufloat(a[5], s)
a6 = ufloat(a[6], s)
a7 = ufloat(a[7], s)
a8 = ufloat(a[8], s)
a9 = ufloat(a[9], s)
a10 = ufloat(a[10], s)
a11 = ufloat(a[11], s)
a12 = ufloat(a[12], s)
a13 = ufloat(a[13], s)
a14 = ufloat(a[14], s)

ages0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]

i=0
while i<15:
    ages0[i] = ages0[i]/2
    #print(ages[i])
    i+=1

#print(ages0)
print(sum(ages0)/15)

del a, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, i

a = [1, 1, 1.5, 1.5, 2, 2, 2.5, 2.5, 2.5, 3, 3, 3, 3, 3.5, 3.5]
a0 = ufloat(a[0], s1)
a1 = ufloat(a[1], s1)
a2 = ufloat(a[2], s1)
a3 = ufloat(a[3], s1)
a4 = ufloat(a[4], s1)
a5 = ufloat(a[5], s1)
a6 = ufloat(a[6], s1)
a7 = ufloat(a[7], s1)
a8 = ufloat(a[8], s1)
a9 = ufloat(a[9], s1)
a10 = ufloat(a[10], s1)
a11 = ufloat(a[11], s1)
a12 = ufloat(a[12], s1)
a13 = ufloat(a[13], s1)
a14 = ufloat(a[14], s1)

ages = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14]

i=0
while i<15:
    ages[i] = ages[i]/2
    #print(ages[i])
    i+=1

#print(ages)
print(sum(ages)/7)
j=0
aln = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while j<15:
    aln[j] = unumpy.log(ages0[j]/ages[j])
    #print(ages[i])
    j+=1
#print("Logarithmus: ", aln)
print("Logarithmus: ", sum(aln)/7)

tmax = [t[44], t[81], t[119], t[157], t[197], t[236], t[276], t[315], t[355], t[395], t[435], t[475], t[515], t[555], t[596]]
tmax1 = [t[21], t[61], t[101], t[141], t[181], t[221], t[261], t[301], t[342], t[382], t[422], t[462], t[502], t[542], t[582]]
i=0
for i in range(0,15):
    print(tmax[i]-tmax1[i])

print("Wärmeleitfähigkeit: ", (8000*400*0.03*0.03)/(2*76.333*ufloat(3.38, 0.16)))