#from rtlsdr import RtlSdr
import numpy as np
import scipy.signal as signal
import matplotlib
matplotlib.use('Agg') # necessary for headless mode
# see http://stackoverflow.com/a/3054314/3524528
import matplotlib.pyplot as plt

#sdr = RtlSdr()

F_station = int(88.9e6) # NPR
F_offset = 250000 # Offset to capture at

# We capture at an offset to avoid DC spike
Fc = F_station - F_offset # Capture center frequency
#Fs = int(1140000) 	# Sample rate
Fs = int(2500000)	# Sample rate for (airspy)
#N = int(8192000)	# Samples to capture
N = int(12500000)	# Samples to capture (airspy)
					# 5 seconds of signal?

# This is where we wish we could access the Airspy in python 

# configure device
#sdr.sample_rate = Fs # Hz
#sdr.center_freq = Fc  # Hz
#sdr.gain = 'auto'

# Read samples
#samples = sdr.read_samples(N)

# Clean up the SDR device
#sdr.close()
#del(sdr)

# We'll have to read from a file created by airspy_rx instead
# airspy_rx -f 88.9.0 -a 1 -t 0 -v 15 -m 15 -l 14 -n 12500000 -d 
# 	-r my_iq32floatdata.dat
#samples = np.fromfile("my_iq32floatdata.dat", dtype="float32")
samples = np.fromfile("my_iq32floatdata.dat", dtype="complex64")

# Turn the interleaved I and Q samples into complex values
# the syntax "dat[0::2]" means "every 2nd value in 
# array dat starting from the 0th until the end"
#samples = samples[0::2] + 1j*samples[1::2]
# I tested this, and it verifies as complex64

# Note: a quicker way to turn the interleaved I and Q samples
#  into complex values
# (courtesy of http://stackoverflow.com/a/5658446/) would be:
# dat = dat.astype(np.float32).view(np.complex64)

# Convert samples to a numpy array
#x1 = np.array(samples).astype("complex64")
x1  = np.copy(samples)


# Plot the spectrogram of the acquired samples
plt.specgram(x1, NFFT=2048, Fs=Fs)
plt.title("x1")
plt.ylim(-Fs/2, Fs/2)
plt.savefig("x1_spec.pdf", bbox_inches='tight', pad_inches=0.5)
plt.close()

# Looking at the spectogram, we can see that as expected, our FM
# radio signal is located at an offset from the center.
# To mix the data down, generate a digital complex exponential
# (with the same length as x1) with phase -F_offset/Fs
fc1 = np.exp(-1.0j*2.0*np.pi* F_offset/Fs*np.arange(len(x1)))
# Now, just multiply x1 and the digital complex expontential
x2 = x1 * fc1

#  and generate the plot of the shifted signal with
plt.specgram(x2, NFFT=2048, Fs=Fs)
plt.title("x2")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.ylim(-Fs/2, Fs/2)
plt.xlim(0,len(x2)/Fs)
plt.ticklabel_format(style='plain', axis='y' )
plt.savefig("x2_spec.pdf", bbox_inches='tight', pad_inches=0.5)
plt.close()

# Our next step will be to filter and then downsample the signal to
# focus only the FM radio signal

# An FM broadcast signal has a bandwidth of 200 kHz
f_bw = 200000
dec_rate = int(Fs / f_bw)
x4 = signal.decimate(x2, dec_rate)
# Calculate the new sampling rate
Fs_y = Fs/dec_rate

# Now we are working with a narrower view of the spectrum, as
# seen in the spectogram of x4 :
plt.specgram(x4, NFFT=2048, Fs=Fs_y)
plt.title("x4")
plt.ylim(-Fs_y/2, Fs_y/2)
plt.xlim(0,len(x4)/Fs_y)
plt.ticklabel_format(style='plain', axis='y' )
plt.savefig("x4_spec.pdf", bbox_inches='tight', pad_inches=0.5)
plt.close()

# We can also plot the constellation, which should have the
# circular pattern typical of an FM signal:
# Plot the constellation of x4.

# Plot the constellation of x4.  What does it look like?
plt.scatter(np.real(x4[0:50000]), np.imag(x4[0:50000]), color="red", alpha=0.05)  
plt.title("x4")  
plt.xlabel("Real")  
plt.xlim(-1.1,1.1)  
plt.ylabel("Imag")  
plt.ylim(-1.1,1.1)  
plt.savefig("x4_const.pdf", bbox_inches='tight', pad_inches=0.5)  
plt.close()  


# If your constellation looks like a filled circle rather than an
# outline, this suggests a noisy signal. You'll know for certain when
# you listen to the audio output!

# Since we are left with just the 200kHz FM broadcast signal, we
# can now demodulate it with our polar discriminator:

### Polar discriminator
y5 = x4[1:] * np.conj(x4[:-1])
x5 = np.angle(y5)

# and we can visualize the signal with:

# Note: x5 is now an array of real, not complex, values
# As a result, the PSDs will now be plotted single-sided by default (since
# a real signal has a symmetric spectrum)
# Plot the PSD of x5
plt.psd(x5, NFFT=2048, Fs=Fs_y, color="blue")  
plt.title("x5")  
plt.axvspan(0,             15000,         color="red", alpha=0.2)  
plt.axvspan(19000-500,     19000+500,     color="green", alpha=0.4)  
plt.axvspan(19000*2-15000, 19000*2+15000, color="orange", alpha=0.2)  
plt.axvspan(19000*3-1500,  19000*3+1500,  color="blue", alpha=0.2)  
plt.ticklabel_format(style='plain', axis='y' )  
plt.savefig("x5_psd.pdf", bbox_inches='tight', pad_inches=0.5)  
plt.close()

# Compare this to the figure in the PDF showing the parts of the FM
# broadcast signal. Broadcasts vary with respect to which parts of
# the signal they include.

# Now we're ready for the de-emphasis filter:

# The de-emphasis filter
# Given a signal 'x5' (in a numpy array) with sampling rate Fs_y
d = Fs_y * 75e-6   # Calculate the # of samples to hit the -3dB point  
x = np.exp(-1/d)   # Calculate the decay between each sample  
b = [1-x]          # Create the filter coefficients  
a = [1,-x]  
x6 = signal.lfilter(b,a,x5)

# And then we can decimate once again to focus on the mono 
# audio part of the broadcast:

# Find a decimation rate to achieve audio sampling rate between 44-48 kHz
audio_freq = 44100.0  
dec_audio = int(Fs_y/audio_freq)  
Fs_audio = Fs_y / dec_audio

x7 = signal.decimate(x6, dec_audio)

# and finally, we can write to an audio file:

# Scale audio to adjust volume
x7 *= 10000 / np.max(np.abs(x7))  
# Save to file as 16-bit signed single-channel audio samples
x7.astype("int16").tofile("wbfm-mono.raw")  

# Find out what your audio sampling rate by checking the value of
print(Fs_audio)

# If you are running Linux, you can play back this file from the terminal with
# aplay wbfm-mono.raw -r 45600 -f S16_LE -t raw -c 1 

# Audacity can play the file, usign follwoing settings:
# File->Import->Raw Data
# Encoding: Signed 16-bit PCM
# Byte order: Little-endian
# Channels; 1-channel mono
# Start offset: 0 bytes
# Amount to Import: 100%
# Sample rate: 45600 Hz
