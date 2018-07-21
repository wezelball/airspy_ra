# includes core parts of numpy, matplotlib
import matplotlib.pyplot as plt
import numpy as np
# include scipy's signal processing functions
import scipy.signal as signal

# practice reading in complex values stored in a file
# Read in data that has been stored as raw I/Q interleaved 32-bit float samples

dat = np.fromfile("iqsamples.float32", dtype="float32")
# Look at the data. Is it complex?
dat

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
dat = dat[0::2] + 1j*dat[1::2]

# Note: a quicker way to turn the interleaved I and Q samples  into complex values
# (courtesy of http://stackoverflow.com/a/5658446/) would be:
# dat = dat.astype(np.float32).view(np.complex64)

# Now look at the data again. Verify that it is complex:
dat 

# Plot the spectogram of this data
plt.specgram(dat, NFFT=1024, Fs=1000000)
plt.title("PSD of 'signal' loaded from file")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()  # if you've done this right, you should see a fun surprise here!

# Let's try a PSD plot of the same data
plt.psd(dat, NFFT=1024, Fs=1000000)
plt.title("PSD of 'signal' loaded from file")
plt.show() 


# And let's look at it on the complex plan
# Note that showing *every* data point would be time- and processing-intensive
# so we'll just show a few
plt.scatter(np.real(dat[0:100000]), np.imag(dat[0:100000]))
plt.title("Constellation of the 'signal' loaded from file")
plt.show()

Fs = 1000000 # define sampling rate

# Let's try a frequency translation. For a complex signal, 
# frequency translation is achieved with multiplication by a complex exponential

# To mix the data down, generate a complex exponential 
# with phase -f_shift/Fs
fc = np.exp(-1.0j*2.0*np.pi* 50000/Fs*np.arange(len(dat)))
# Try plotting this complex exponential with a scatter plot of the complex plan - 
# what do you expect it to look like?
y = dat * fc

# How has our PSD changed?

plt.psd(dat, NFFT=1024, Fs=1000000, color="blue")  # original
plt.psd(y, NFFT=1024, Fs=1000000, color="green")  # translated
plt.title("PSD of 'signal' loaded from file")
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

plt.psd(dat, NFFT=1024, Fs=1000000, color="blue")  # original
plt.psd(y, NFFT=1024, Fs=1000000, color="green")  # filtered
plt.title("PSD of 'signal' loaded from file")
plt.show() 

# Let's try decimating following a lowpass filter

# Figure out our best decimation rate
dec_rate = int(Fs / f_bw)
z = signal.decimate(y, dec_rate)
Fs_z = Fs/dec_rate

# New PSD - now with new Fs
plt.psd(z, NFFT=1024, Fs=Fs_z, color="blue")
plt.show()

# Given a signal x (in a numpy array)
y = x[1:] * np.conj(x[:-1])
z = np.angle(y)

# The de-emphasis filter
# Given a signal 'x5' (in a numpy array) with sampling rate Fs_y
d = Fs_y * 75e-6   # Calculate the # of samples to hit the -3dB point
x = np.exp(-1/d)   # Calculate the decay between each sample
b = [1-x]          # Create the filter coefficients
a = [1,-x]
x6 = signal.lfilter(b,a,x5)

# Given a signal x (in a numpy array)
x *= 10000 / np.max(np.abs(x))               # scale so it's audible
x.astype("int16").tofile("wbfm-mono.raw")    # write to file

