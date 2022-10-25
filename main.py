
import numpy as np
from scipy.fft import rfft
import scipy.io.wavfile as wf

D = []
Z = []
M = 1024
audio = 'sample-6s.wav'
audio, mass = wf.read(audio)

a = mass.T[0]
b=[(ele/2**8.)*2-1 for ele in a]
c = rfft(b)
S = np.abs(c)
S = 20 * np.log10(S / np.max(S))
dlin = (len(S) / 2935) - 1
startMass = 0
while (dlin > 0):
    D.append(round(S[startMass * 2935 + 44: (startMass + 1) * 2935].sum() / 2935))
    dlin = dlin - 1
    startMass += 1
D = np.abs(D)
D.sort()
DecibelMAX = np.max(D)
DecibelMIN = np.min(D)
renges = 0
Gistoram = []
i = 0
iterat = 0
while renges <= DecibelMAX - DecibelMIN:
    for i in D:
        if DecibelMIN + renges == i:
            iterat += 1
    Gistoram.append(iterat)
    iterat = 0
    renges +=1
relProb = [ ]
for i in Gistoram:
    relProb.append(float("{0:.5f}".format(i/ sum(Gistoram))))
probab = 0
finalyMass = []
for i in relProb:
    finalyMass.append(probab + i)
    probab = probab + i
userProb = float(input("Введите доверительную вероятность: "))
for index in range(len(finalyMass)):
    if finalyMass[index] > userProb:
        print(str(index + DecibelMIN) + " dB")
        break
else: print("Такой доверительности не существует")









