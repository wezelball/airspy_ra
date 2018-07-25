import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal
from datetime import datetime, timedelta

# Read the data file in
df = pd.read_csv ("~/Documents/devel/airspy_ra/spectro_plottools/h120180722-tp.csv", \
	usecols=(0,1,2,3,4,5,9), header=None)

# Assign column values
df.columns=['UTC_h', 'UTC_m', 'UTC_s', 'LST_h', 'LST_m','LST_s','tp']

# UTC dataframe
#df_utc = df[['UTC_h', 'UTC_m', 'UTC_s', 'tp']]
# LST dataframe
#df_lst = df[['LST_h', 'LST_m', 'LST_s', 'tp']]

# Create a column that is can be read by pandas, H:M:S
df['utime'] = df['UTC_h'].astype(str) + ':' \
	+ df['UTC_m'].astype(str) + ':' + df['UTC_s'].astype(str)
df['ltime'] = df['LST_h'].astype(str) + ':' \
	+ df['LST_m'].astype(str) + ':' + df['LST_s'].astype(str)

# Try to get dates
df['time'] = pd.to_datetime(df['utime'], format="%H:%M:%S")


# This is scipy low pass filter
# spell out the args that were passed to the Matlab function
N = 10
Fc = 40
Fs = 1600
# provide them to firwin
h = scipy.signal.firwin(numtaps=N, cutoff=40, nyq=Fs/2)
# 'filterseries' is the time-series data you are filtering
# pd.Series returns numpy array of tp points that can now
# be operated on by scipy.signal
filterseries = pd.Series(df['tp'])	
df['filtered'] = scipy.signal.lfilter(h, 1.0, filterseries)

# Try to select a time range, a little daunting, but logical
# I tried to do this on the time series, but it didn't seem to
# work correctly, although the utime did

# between 2 times
#df_utc_range = df[(df['utime'] > '12:35:34') & (df['utime'] < '12:35:52')]
# greater than a particular time
df_utc_range = df[(df['utime'] > '18:00:00')]

#df_utc_range = df_utc[(df_utc['utime'] > '18:00:00')]


# See what they look like
print(df.head())

# Plot the values
df.plot('time', 'tp')
df_utc_range.plot('time', 'tp')
df_utc_range.plot('time', 'filtered')
plt.show()

