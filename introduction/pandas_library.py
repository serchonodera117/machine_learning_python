import pandas as pd
import numpy as np

#creations of dataframes
print("\n\n DataFrame-------------\n")
data = np.array([['', 'col1', 'col2'], ["row 1", 11, 22], ["row 2", 33, 44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

print("\n\n Series-------------\n")
series = pd.Series({
        "Argentina": "Buenos Aires",
        "Chile": "Santiago de chile",
        "Colombia": "Bogotá"
    })
print("series")
print(series) #similar to hashmaps or objects in javascript


print("\n\n Shape of the data-------------\n")
data = np.array([['', 'col1', 'col2'], ["row 1", 11, 22], ["row 2", 33, 44], ["row 3", 33, 44]])
df = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])
#print(df)
print(df.shape) #shape of the data
print(len(df.index)) #height of data

#statistics fom the Dataframe
print("\n\nStatistics from the dataframe\n",df.describe())
#Measyre of all collumns
print("\n\nMeasure of all collumns\n",df.mean)
#correlation 
print("\n\nCorrelation of dataframe\n",df.corr())
#count data from dataframe
print("\n\nCounting of not null data from dataframe\n",df.count())

#know maximun value fron each column from dataframe
print("\n\n Greatest value from column\n", df.max())

#know maximun value fron each column from dataframe
print("\n\n Minimun value from column\n", df.min())

#know average or median from dataframe
#print("\n\n median value from column\n", df.median()) #only works with nummber

#standard desvieation
#print("\n\n Standard deviatio from column from dataframe", data.std()) #only works with nummber


#* Oppening local file 
# file example (this file is created only for the example)
file = pd.read_csv('resources/train.csv')
# clean dataframe 
print(file.isnull())   #(will print a matriz of falze or true in the same shape of the file)
# 
# sum of null data in dataframe----------------------------------------------------------------
print("sum of datanums",df.isnull().sum())