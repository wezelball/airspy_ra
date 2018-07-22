import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from cStringIO import StringIO

# Read the data file in
df = pd.read_csv ("~/Documents/devel/airspy_ra/spectro_plottools/h120180722-tp.csv", usecols=(0,1,2,3,4,5,9), header=None)
#df = pd.read_csv ("h120180722-tp.csv", usecols=(0,1,2,3,4,5,9), header=None)
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

# See what they look like
print(df.head())
print(df_utc.head())
print(df_lst.head())


# Plot the values
df_utc.plot('time', 'tp')
df_lst.plot('time', 'tp')
plt.show()
