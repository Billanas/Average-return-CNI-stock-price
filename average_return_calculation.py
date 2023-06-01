import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#read the data
CNI = pd.read_csv('/home/billys/MacroTrends_Data_Download_CNI.csv', index_col='Date')

CNI.tail()

# Log returns:ln (Pt / Pt-1)

CNI['log_return'] = np.log(CNI['open'] / CNI['open'].shift(1))

CNI['log_return'].plot(figsize=(8, 5))

#Daily return
log_return_d = CNI['log_return'].mean()
log_return_d

#Annual return 
log_return_a = CNI['log_return'].mean() * 250
log_return_a

# Annual return as percentage
print (str(round(log_return_a,5)*100), '%')

# Variance calculation
CNI_var = CNI['log_return'].var() * 250

CNI_var

