import numpy as np
import matplotlib.pyplot as plt
import csv


x1 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=1)
x2 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=2)
x3 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=3)
x4 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=4)
x5 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=5)
x6 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=6)
x7 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=7)
x8 = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=8)
t = np.genfromtxt("content/Dynamo_40_5V.txt",encoding="utf-16",unpack=True,usecols=9)
#### damit deklariert ihr die erste Spalte der datei "Messwerte.csv" als array x, die zweite als array y usw
tmax = [45, 125, 210, 290, 370, 450, 530, 610]
tmin = [85, 165, 245, 330, 410, 490, 570]
x2max = [31.03, 34.08, 36.1, 37.8, 39.2, 40.37, 41.39, 42.25]
x2min = [27.32, 29.81, 31.72, 33.3, 34.51, 35.58, 36.56]
x1max = [x1[14], x1[29], x1[45], x1[61], x1[77], x1[93], x1[109], x1[125]]
x1min = [x1[18], x1[35], x1[51], x1[67], x1[84], x1[100], x1[116]]
tmax1 = [t[14], t[29], t[45], t[61], t[77], t[93], t[109], t[125]]
tmin1 = [t[18], t[35], t[51], t[67], t[84], t[100], t[116]]
x5max = [x5[12], x5[27], x5[43], x5[59], x5[75], x5[91], x5[107], x5[124]]
x6max = [x6[9], x6[25], x6[41], x6[57], x6[74], x6[90], x6[106], x6[122]]
tmax2 = [t[12], t[27], t[43], t[59], t[75], t[91], t[107], t[124]]
tmax3 = [t[9], t[25], t[41], t[57], t[74], t[90], t[106], t[122]]
#nun rechnet ihr mit eurem Messergebnis wie ihr wollt, am ende erhaltet ihr das array "ergebnis"
#Python schreibt SEHR viele Nachkommastellen, wenn ihr nicht aufpasst. Bevor ihr also eure Ergebnisse + Messwerte
#in eine neue csv datei schreibt, damit man diese in Latex einbinden kann, muss gerundet werden.

plt.plot(t, x1, '-b', label="Verhältnis für T1")
plt.plot(t, x2, '-r', label="Verhältnis für T2")
#plt.plot(tmin, x2min, '.y', label="Minima für T2")
plt.plot(tmax, x2max, '.g', label="Maxima für T2")
#plt.plot(tmin1, x1min, '.c', label="Minima für T1")
plt.plot(tmax1, x1max, '.m', label="Maxima für T1")
plt.xlabel(r"t in $s$")
plt.ylabel(r"Temp. in $°C$")
plt.grid(True)
plt.legend(loc="best")
plt.savefig("build/plot4.pdf")
plt.close()

plt.plot(t, x5, '-g', label="Verhältnis für T5")
plt.plot(t, x6, '-m', label="Verhältnis für T6")
plt.plot(tmax3, x6max, '.r', label="Maxima für T6")
plt.plot(tmax2, x5max, '.b', label="Maxima für T5")
plt.xlabel(r"t in $s$")
plt.ylabel(r"Temp. in $°C$")
plt.grid(True)
plt.legend(loc="best")
plt.savefig("build/plot5.pdf")
plt.close()

#Ergebnisrundx = ["%.3f" % elem for elem in ergebnisx]
#Ergebnisrundy = ["%.3f" % elem for elem in ergebnisy]
#xrund = ["%.2f" % elem for elem in x3]
#yrund = ["%.3f" % elem for elem in y]

# Jeder Wert im array "Ergebnis" wird auf 3 dezimalstellen gerundet.
# Jetzt schreiben wir unsere Messergebnisse + Ergebnis in eine CSV Datei

with open("content/Dynamo_40_5V.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x1, x2, x3, x4, x5, x6, x7, x8, t))