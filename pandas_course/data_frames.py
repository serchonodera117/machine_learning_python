import pandas as pd
import numpy as np

def dataframeDictionary():
    data =  {
            'Name': ['Marie', 'Ronette', 'Kayolica', 'Adaline'],
          'Career': ['Phisycs', 'Engeeneering', 'Writer', 'Lawyer'],
          'Emails': ['mari@gmail.com', 'r0nett3@gmail.com', 'ksyttadin@gmail.com', 'line_a@gmail.com']
          }
    
    students = pd.DataFrame(data)
    print(students)

#dataframeDictionary()

def dataFrameFromList():
    df = pd.DataFrame([['Marie', 27], ['kayolica', 18], ['Gisselle', 17], ['Ronette', 19]], columns=['NAME', 'AGE'])
    print(df)

#dataFrameFromList()

def dataframeFromNumpyArray():
    a = pd.DataFrame(np.random.randn(4,3), columns=['a', 'b', 'c'])
    print(a)

dataframeFromNumpyArray()