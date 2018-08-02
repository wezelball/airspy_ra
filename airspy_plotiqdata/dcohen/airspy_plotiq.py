#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:33:30 2018

@author: dcohen
"""

from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import os

# set up basic parameters
frequency = 610.0   # frequency in MHz
filename = "./airspytestiq.dat"
num_samples = 10000000
sample_rate = 2500000
linear_gain = 10


# delete the file if it exists
try:
    os.remove(filename)
except OSError:
    pass

# open the airspy receive application using subprocess
process = Popen(["airspy_rx", "-t","0", "-r", filename, "-a"  "0", "-f", \
                 str(frequency), "-g", str(linear_gain), "-n", str(num_samples), "-d"], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
print stdout

# now read the bloody file into "dat"
dat = np.fromfile(filename, dtype="float32", count = num_samples)

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
dat = dat[0::2] + 1j*dat[1::2]

# Plot the spectogram of this data
plt.specgram(dat, NFFT=1024, Fs=2500000)
plt.title("Spectrogram of signal")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()

# Let's try a PSD plot of the same data
plt.psd(dat, NFFT=1024, Fs=2500000)
plt.title("PSD of signal")
plt.show()

# What happens when you filter your data with a lowpass filter?
f_bw = 150000
Fs  = 1000000
n_taps = 64 
lpf = signal.remez(n_taps, [0, f_bw, f_bw+(Fs/2-f_bw)/4, Fs/2], [1,0], Hz=Fs)

# Plot your filter's frequency response:
w, h = signal.freqz(lpf)
plt.plot(w, 20 * np.log10(abs(h)))
plt.xscale('log')
plt.title('Filter frequency response')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.margins(0, 0.1)
plt.grid(which='both', axis='both')
plt.show()

y = signal.lfilter(lpf, 1.0, dat)

# How has our PSD changed?

plt.psd(dat, NFFT=1024, Fs=2500000, color="blue")  # original
plt.psd(y, NFFT=1024, Fs=2500000, color="green")  # filtered
plt.title("PSD of filtered signal loaded from file")
plt.show()