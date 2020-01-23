import numpy as np
import matplotlib.pyplot as plt
import csv


x7 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=1)
x1 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=2)
x2 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=3)
x3 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=4)
x4 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=5)
x5 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=6)
x6 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=7)
x8 = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=8)
t = np.genfromtxt("content/Dynamo_80C.txt",encoding="utf-16",unpack=True,usecols=9)
#### damit deklariert ihr die erste Spalte der datei "Messwerte.csv" als array x, die zweite als array y usw

#nun rechnet ihr mit eurem Messergebnis wie ihr wollt, am ende erhaltet ihr das array "ergebnis"
#Python schreibt SEHR viele Nachkommastellen, wenn ihr nicht aufpasst. Bevor ihr also eure Ergebnisse + Messwerte
#in eine neue csv datei schreibt, damit man diese in Latex einbinden kann, muss gerundet werden.

x7max = [x7[21], x7[61], x7[101], x7[141], x7[181], x7[221], x7[261], x7[301], x7[342], x7[382], x7[422], x7[462], x7[502], x7[542], x7[582]]
x8max = [x8[44], x8[81], x8[119], x8[157], x8[197], x8[236], x8[276], x8[315], x8[355], x8[395], x8[435], x8[475], x8[515], x8[555], x8[596]]
t7 = [t[21], t[61], t[101], t[141], t[181], t[221], t[261], t[301], t[342], t[382], t[422], t[462], t[502], t[542], t[582]]
t8 = [t[44], t[81], t[119], t[157], t[197], t[236], t[276], t[315], t[355], t[395], t[435], t[475], t[515], t[555], t[596]]

plt.plot(t, x7, '-r', label="Abgriffstelle 7")
plt.plot(t, x8, '-b', label="Abgriffstelle 8")
plt.plot(t7, x7max, '.g', label="Maxima von T7")
plt.plot(t8, x8max, '.y', label="Maxima von T8")
plt.xlabel(r"t in $s$")
plt.ylabel(r"T in $°C$")
plt.legend(loc="best")
plt.savefig("build/plot6.pdf")
plt.close()

#Ergebnisrundx = ["%.3f" % elem for elem in ergebnisx]
#Ergebnisrundy = ["%.3f" % elem for elem in ergebnisy]
#xrund = ["%.2f" % elem for elem in x3]
#yrund = ["%.3f" % elem for elem in y]

# Jeder Wert im array "Ergebnis" wird auf 3 dezimalstellen gerundet.
# Jetzt schreiben wir unsere Messergebnisse + Ergebnis in eine CSV Datei

with open("content/Dynamo_80C.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x1, x2, x3, x4, x5, x6, x7, x8, t))