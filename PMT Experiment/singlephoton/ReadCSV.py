##This macro is to read the data from CSV file

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import collections
import os
import glob

path = r'C:\Users\wangjing\Homework\PMT Experiment\singlephoton' # use your path
all_files = glob.glob(path + "/*.csv")



for filename in all_files:
    
    df1 = pd.read_csv(filename , skiprows=4700, nrows=500 , header=None , usecols=[1] , engine='python')
    df2 = pd.read_csv(filename , skiprows=0, nrows=500 , header=None, usecols=[1] , engine='python')  
    df3 = pd.read_csv(filename , skiprows=6000, nrows=500 , header=None, usecols=[1] , engine='python')  
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
    df4 = -(df1.sum() - (df2.sum() + df3.sum())/2 )
    print(df4)
    

    #Int.to_csv
    #pd.to_numeric(Int, downcast='float')
    #print(Int)
   # with open('Result.xlsx','w') as result_file:
    #    writer = csv.writer(result_file, delimiter=',')
     #   for line in Int:
      #      writer.writerow(line)
        
    df4.to_csv('Result.csv', mode='a')
#Define sum
#df1.loc['Col_sum'] = df1.apply(lambda x: x.sum())
#df2.loc['Col_sum'] = df1.apply(lambda y: y.sum())
#df1.loc['Col_ave'] = df1.apply(lambda y: y.mean())
#df2.loc['Col_ave'] = df1.apply(lambda y: y.mean())

#df4 = df1.loc[['Col_sum'],[1]] - df2.loc[['Col_ave'],[1]]
#print(df1.iloc[[4000],[0]])
#print(df1.loc[['Col_sum'],[1]])
#print(df2.loc[['Col_ave'],[1]])

#print(df4)
#print(df1.loc[['Col_sum'],[1]] - df2.loc[['Col_ave'],[1]])
#df1.to_csv('data_1.txt')
#for col in df1.columns:
    #print(df1[col[0]].mean())

