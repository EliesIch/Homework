##This macro is to read the data from CSV file

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import collections
import os
import glob

path = r'C:\Users\wangjing\Homework\PMT Experiment\doublephoton' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    
    df1 = pd.read_csv(filename , skiprows=4950, nrows=350 , header=None , usecols=[1] , engine='python')
    df2 = pd.read_csv(filename , skiprows=0, nrows=4500 , header=None, usecols=[1] , engine='python')  
    df3 = pd.read_csv(filename , skiprows=6000, nrows=3000 , header=None, usecols=[1] , engine='python')  
    pd.set_option("display.float_format", "{:.11f}".format)

    #Plot
    #df1.plot()
    #plt.show()

    #print(df1.sum(0))

    #df2.plot()
    #plt.show()

    #print(df2.mean())

    #df3.plot()
    #plt.show()

   # print(df3.mean())

   #Calsulate Peak area 
    df4 = -(df1.sum() - (df2.sum() + df3.sum())/21.42857 )
    print(df4)
    
    #Store the peaks area    
    df4.to_csv('Result.csv', mode='a', header=False)


