import pandas as pd
import numpy as np

route = 'file_resources\converted_file_character_students.csv'
df = pd.read_csv(route)

#print(df)

def access_by_positions(): #cordinates
    #df.iloc[i,j] #i rows, j cols
    data = df.iloc[1,3]
    print("single data", data)
    print('range data: \n', df.iloc[2, :3])

    print(f"\n\n loc: \n {df.loc[1,('EDAD', 'CARRERA')]}")#acces by name, when you need to search by more than one name, is necessary to agroup them like this ('name', 'name2')
#access_by_positions()


def add_colums_to_dataframe():
    df['TURNO'] = pd.Series(['tarde', 'noche', 'tarde', 'tarde', 'noche', 'tarde'])
    print(df)

#add_colums_to_dataframe()

def delete_column():
    SEMESTRE = df.pop('SEMESTRE')
    print(df)

#delete_column()

def add_row_to_dataframe():
    data = np.array([['Alison', 23, 'F', 'Odontology', 'nineth']])#create an array with the values
    row = pd.DataFrame(data, columns=['NOMBRE','EDAD', 'GENERO', 'CARRERA', 'SEMESTRE']) #create a dataframe with the columns
    mydf = pd.read_csv(route)#use your dataframe, in this case i created other because for some reason df is not valid in this scope

    #concat the dataframe with the new row
    mydf = pd.concat([mydf, row], ignore_index=True) #ignore index to add in bottom position, if you set it yes, you have to specify it
    print(mydf)

#add_row_to_dataframe()

def delete_row_from_dataframe():
   myData =  df.drop([1,2]) #delete row from dataframe, in this case i saved the value in a local variable because in global scope is not possible
   print(myData)

#delete_row_from_dataframe()

def filter_by_row():
    mydf = df[(df['GENERO']=='F') & (df['EDAD'] >22 )]
    print(f"filtered by gender and age: \n {mydf}")

#ilter_by_row()

def order_a_dataframe():
    mydf = df.sort_values('CARRERA') #df.dropna() to drop/delete Nan values
    print(f"Sorted by career:\n {mydf}")
    print(f"Sorted by  age:\n {df.sort_values('EDAD')}")

order_a_dataframe()