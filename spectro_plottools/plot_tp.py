import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal
from datetime import datetime, timedelta
from cStringIO import StringIO

# Read the data file in
df = pd.read_csv ("~/Documents/devel/airspy_ra/spectro_plottools/h120180722-tp.csv", usecols=(0,1,2,3,4,5,9), header=None)
# Assign column values
df.columns=['UTC_h', 'UTC_m', 'UTC_s', 'LST_h', 'LST_m','LST_s','tp']

# UTC dataframe
df_utc = df[['UTC_h', 'UTC_m', 'UTC_s', 'tp']]
# LST dataframe
df_lst = df[['LST_h', 'LST_m', 'LST_s', 'tp']]

# Create a column that is can be read by pandas, H:M:S
df_utc['utime'] = df_utc['UTC_h'].astype(str) + ':' + df_utc['UTC_m'].astype(str) + ':' + df_utc['UTC_s'].astype(str)
df_lst['ltime'] = df_lst['LST_h'].astype(str) + ':' + df_lst['LST_m'].astype(str) + ':' + df_lst['LST_s'].astype(str)

# Try to get dates
df_utc['time'] = pd.to_datetime(df_utc['utime'], format="%H:%M:%S")
df_lst['time'] = pd.to_datetime(df_lst['ltime'], format="%H:%M:%S")

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
filterseries = pd.Series(df_utc['tp'])	
df_utc['filtered'] = scipy.signal.lfilter(h, 1.0, filterseries)

# See what they look like
#print(df.head())
print(df_utc.head())
print(df_lst.head())

# Plot the values
df_utc.plot('time', 'tp')
df_utc.plot('time', 'filtered')

#df_lst.plot('time', 'tp')
plt.show()

