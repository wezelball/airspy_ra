import numpy as np
import scipy.signal as signal
import matplotlib
import matplotlib.pyplot as plt

Fs = int(2500000)	# Sample rate for (airspy)
N = int(12500000)	# Samples to capture (airspy)

a = np.fromfile("my_iq32floatdata.dat")
print ("a.dtype", a.dtype)
a = np.fromfile("my_iq32floatdata.dat", dtype="float64")
#a = np.fromfile("my_iq32floatdata.dat", dtype="complex64")
#a = np.fromfile("my_iq32floatdata.dat", dtype="float32")
b = np.copy(a)

b = a.astype(np.float64).view(np.complex64)

#print("a shape ", a.shape)
#print("a dtype ", a.dtype)
#print("b shape ", b.shape)
#print("a dtype ", b.dtype)

print a[:4]
print b[:4]

# Plot the spectrogram of the acquired samples
plt.specgram(b, NFFT=2048, Fs=Fs)
plt.title("b")
plt.ylim(-Fs/2, Fs/2)
#plt.savefig("x1_spec.pdf", bbox_inches='tight', pad_inches=0.5)
plt.show()
