import pandas as pd
import numpy as np

#the principal requirement to combine or concat DataFrames is necessary to have the same index of columns (even the name of then bevause if name is diferent, otherwise, will generate NaN values)

DF1 = pd.DataFrame({
                    'Name': ['Jose', 'Maz'],
                    'Career': ['Economy', 'Architecture'],
                    'Age': [23, 26]
                     }).set_index('Name') #to concat is necesary to set an index to use it as a reference 

DF2 = pd.DataFrame({
                    'Name': ['Aurora', 'Kayolica'],
                    'Career': ['Medicine', 'lawyer'],
                    'Age': [22, 24]
                     }).set_index('Name')


# print(f"First dattaframe: \n{DF1} \n Second dattaframe: \n{DF2}")

def concatenation_of_dataframes_byRows():
    tempDef = pd.concat([DF1, DF2])
    print(tempDef)
    pass


#concatenation_of_dataframes_byRows()


def concatenation_of_dataframes_byCols():
    df1 = pd.DataFrame({'Cars': ['Nissan', 'Ford', 'Audi'], #concat by cols, you gonna need a row as an index
                        'Color': ['White', 'Blue', 'Red']}).set_index('Cars')

    df2 = pd.DataFrame({'Cars': ['Nissan', 'Ford', 'Audi'],
                        'Models': [2018, 2020, 2022]}).set_index('Cars')
    
    newDF = pd.concat([df1, df2], axis=1)

    print(newDF)


#concatenation_of_dataframes_byCols()                


def mix_of_dataframes(): #alows to mix two darafeames that have common information by using a key
    df1 = pd.DataFrame({'Cars': ['Nissan', 'Ford', 'Audi'], 
                        'Color': ['White', 'Blue', 'Red']}) #it rquieres to have the same information in the index

    df2 = pd.DataFrame({'Cars': ['Toyota', 'Ford', 'Audi'],
                        'Models': [2018, 2020, 2022]})
    
    newDf = pd.merge(df1, df2, on='Cars') #inner is default value
    newDf1 = pd.merge(df1, df2, on='Cars', how='outer') #means that only looks for the rows, (outer=rows, inner=columns) in case the data is different in index, outer will add it anyway
    print(newDf)
    print("\n\n",newDf1)
    #how= left || how=right makes reference to the first or the second dataframe

mix_of_dataframes()