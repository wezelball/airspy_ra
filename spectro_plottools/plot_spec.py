import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.signal
from datetime import datetime, timedelta

# Read the data file in
df = pd.read_csv ("~/Documents/devel/airspy_ra/spectro_plottools/h120180728-spec.csv", \
	header=None)
	
# Assign column headers for UTC/LST times, and the frequency
# You have to fix this later with a for loop
# UTC
df.rename(columns ={0: 'UTC_h'}, inplace =True)
df.rename(columns ={1: 'UTC_m'}, inplace =True)
df.rename(columns ={2: 'UTC_s'}, inplace =True)
# LST
df.rename(columns ={3: 'LST_h'}, inplace =True)
df.rename(columns ={4: 'LST_m'}, inplace =True)
df.rename(columns ={5: 'LST_s'}, inplace =True)
# freq
df.rename(columns ={6: 'freq'}, inplace =True)

# Insert the utime column that is can be read by pandas, H:M:S
df.insert(0, 'utime', df['UTC_h'].astype(str) + ':' \
	+ df['UTC_m'].astype(str) + ':' + df['UTC_s'].astype(str))

# Insert the ltime column that is can be read by pandas, H:M:S
df.insert(1, 'ltime', df['LST_h'].astype(str) + ':' \
	+ df['LST_m'].astype(str) + ':' + df['LST_s'].astype(str))

# have a look
print(df.head())

# I think this selects the first row, and the 11th to last column
# Remember, I add 2 columns the dataframe so it's wider than the csv
row1 = df.iloc[0,10:-1]	# 1st row
row2 = df.iloc[1,10:-1]	# 2nd row, why not

# Plot the rows
row1.plot()		# it plots them on one axis, great!
row2.plot()

plt.show()
