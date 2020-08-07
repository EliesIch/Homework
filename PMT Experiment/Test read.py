##This macro is to read the data from CSV file

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import collections
import os
import glob

path = r'C:\\Users\\wangjing\\Homework\\PMT Experiment\\Data' # use your path
all_files = glob.glob(path + "/*.csv")

for filename in all_files:
    
    df1 = pd.read_csv(filename , skiprows=2000, nrows=6000 , header=None , usecols=[1] , engine='python')        #Signal reigon
    df2 = pd.read_csv(filename , skiprows=0, nrows=2000 , header=None, usecols=[1] , engine='python')         #Background 
    #df3 = pd.read_csv(filename , skiprows=700, nrows=300 , header=None, usecols=[1] , engine='python')  
    pd.set_option("display.float_format", "{:.12f}".format)

    #Plot
    #df1.plot()
    #plt.show()
    #Calsulate Peak area 
    df4 = -(df1.sum() - df2.sum()*3 )
    print(df4)

    #Store the peaks area    
    df4.to_csv('test.csv', mode='a', header=False, index = False)
print("Finished!")

