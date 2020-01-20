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

#nun rechnet ihr mit eurem Messergebnis wie ihr wollt, am ende erhaltet ihr das array "ergebnis"
#Python schreibt SEHR viele Nachkommastellen, wenn ihr nicht aufpasst. Bevor ihr also eure Ergebnisse + Messwerte
#in eine neue csv datei schreibt, damit man diese in Latex einbinden kann, muss gerundet werden.

plt.plot(t, x1, '-b', label="Verhältnis für T1")
plt.plot(t, x2, '-r', label="Verhältnis für T2")
plt.xlabel(r"t in $s$")
plt.ylabel(r"Temp. in $°C$")
plt.grid(True)
plt.legend(loc="best")
plt.savefig("build/plot4.pdf")
plt.close()

plt.plot(t, x5, '-g', label="Verhältnis für T5")
plt.plot(t, x6, '-m', label="Verhältnis für T6")
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