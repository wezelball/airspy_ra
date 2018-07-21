import numpy as np
import scipy.signal as signal
import matplotlib
import matplotlib.pyplot as plt

F_station = int(88.9e6) # NPR
F_offset = 250000 # Offset to capture at

# We capture at an offset to avoid DC spike
Fc = F_station - F_offset # Capture center frequency
Fs = int(1140000) 	# Sample rate
N = int(8192000)	# Samples to capture

samples = np.fromfile("my_rtldata.dat")
print ("samples.dtype", samples.dtype)

# Convert samples to a numpy array
x1 = np.array(samples).astype("complex64")

# Plot the spectrogram of the acquired samples
plt.specgram(x1, NFFT=2048, Fs=Fs)
plt.title("x1")
plt.ylim(-Fs/2, Fs/2)
plt.show()
