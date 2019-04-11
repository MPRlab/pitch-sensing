# -*- coding: utf-8 -*-
"""
FFT

https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files

https://www.dummies.com/programming/python/performing-a-fast-fourier-transform-fft-on-a-sound-file/

https://www.oreilly.com/library/view/elegant-scipy/9781491922927/ch04.html
"""

import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
from scipy.io import wavfile # get the api
from numpy import argmax

fs, data = wavfile.read(r"G:\WPI\MPR Lab\Cyther\CREPE\Creper\320.wav") # load the data
time=2 #seconds
a = data.T
c = fft(a) # calculate fourier transform (complex numbers list)
d = int(len(c))  # Divide by 2: you only need half of the fft list
signal=abs(c[0:(d-1)])

freqs = fftfreq(len(signal)) * fs

plt.plot(freqs, signal,'r') 
plt.show()

max_mag_index=argmax(signal)
max_freq_mag=freqs[max_mag_index]
print(f"Peaks at {max_freq_mag} Hz")