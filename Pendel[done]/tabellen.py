import numpy as np
import csv

x = np.genfromtxt("datena.csv",delimiter=",",unpack=True,usecols=0)
y = np.genfromtxt("datena.csv",delimiter=",",unpack=True,usecols=1)

x1 = np.genfromtxt("datenb.csv",delimiter=",",unpack=True,usecols=0)
y1 = np.genfromtxt("datenb.csv",delimiter=",",unpack=True,usecols=1)

x2 = np.genfromtxt("datenc.csv",delimiter=",",unpack=True,usecols=0)
y2 = np.genfromtxt("datenc.csv",delimiter=",",unpack=True,usecols=1)

x3 = np.genfromtxt("datend1.csv",delimiter=",",unpack=True,usecols=0)
y3 = np.genfromtxt("datend1.csv",delimiter=",",unpack=True,usecols=1)
z3 = np.genfromtxt("datend1.csv",delimiter=",",unpack=True,usecols=2)
u3 = np.genfromtxt("datend1.csv",delimiter=",",unpack=True,usecols=3)
#### damit deklariert ihr die erste Spalte der datei "Messwerte.csv" als array x, die zweite als array y usw

#nun rechnet ihr mit eurem Messergebnis wie ihr wollt, am ende erhaltet ihr das array "ergebnis"
#Python schreibt SEHR viele Nachkommastellen, wenn ihr nicht aufpasst. Bevor ihr also eure Ergebnisse + Messwerte
#in eine neue csv datei schreibt, damit man diese in Latex einbinden kann, muss gerundet werden.
ergebnisx = x/5
ergebnisy = y/5
ergebnisx1 = x1/5
ergebnisy1 = y1/5
ergebnisx2 = x2/5
ergebnisy2 = y2/5
ergebnisx3 = x3/8
ergebnisy3 = y3/12
#print(sum(ergebnisx)/9)
#print(sum(ergebnisy)/9)

#print(sum(ergebnisx1)/9)
#print(sum(ergebnisy1)/9)

#print(sum(ergebnisx2)/9)
#print(sum(ergebnisy2)/9)

#print(sum(ergebnisx3)/10)
#print(sum(ergebnisy3)/10)
#print(sum(z3)/10)
#print(sum(u3)/10)
print(sum(2*np.pi/ergebnisx1)/9)
print(sum(2*np.pi/ergebnisy1)/9)

print(sum(2*np.pi/ergebnisx2)/9)
print(sum(2*np.pi/ergebnisy2)/9)

Ergebnisrundx = ["%.3f" % elem for elem in ergebnisx]
Ergebnisrundy = ["%.3f" % elem for elem in ergebnisy]
xrund = ["%.3f" % elem for elem in x]
yrund = ["%.3f" % elem for elem in y]

Ergebnisrundx1 = ["%.3f" % elem for elem in ergebnisx1]
Ergebnisrundy1 = ["%.3f" % elem for elem in ergebnisy1]
x1rund = ["%.3f" % elem for elem in x1]
y1rund = ["%.3f" % elem for elem in y1]

Ergebnisrundx2 = ["%.3f" % elem for elem in ergebnisx2]
Ergebnisrundy2 = ["%.3f" % elem for elem in ergebnisy2]
x2rund = ["%.3f" % elem for elem in x2]
y2rund = ["%.3f" % elem for elem in y2]

Ergebnisrundx3 = ["%.3f" % elem for elem in ergebnisx3]
Ergebnisrundy3 = ["%.3f" % elem for elem in ergebnisy3]
z3rund = ["%.3f" % elem for elem in x3]
u3rund = ["%.3f" % elem for elem in y3]
# Jeder Wert im array "Ergebnis" wird auf 3 dezimalstellen gerundet.
# Jetzt schreiben wir unsere Messergebnisse + Ergebnis in eine CSV Datei

with open("tabelle1.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(xrund,yrund,Ergebnisrundx, Ergebnisrundy))

with open("tabelle2.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x1rund,y1rund,Ergebnisrundx1, Ergebnisrundy1))

with open("tabelle3.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(x2rund,y2rund,Ergebnisrundx2, Ergebnisrundy2))

with open("tabelle4.csv", "w") as f:
    writer= csv.writer(f)
    writer.writerows(zip(Ergebnisrundx3, Ergebnisrundy3, z3rund, u3rund))