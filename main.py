
import numpy as np
from scipy.fft import fft
import scipy.io.wavfile as wf

M = 1024
audio = 'sample-6s.wav'
audio, mass = wf.read(audio)

a = mass.T[0]
b=[(ele/2**8.)*2-1 for ele in a]
c = fft(b)
S = np.abs(c)
S = 20 * np.log10(S / np.max(S))
for x in np.nditer(S):
    print(x)




