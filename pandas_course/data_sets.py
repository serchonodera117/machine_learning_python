import pandas as pd

fileRoute = 'file_resources\ModalidadVirtual.csv'

def printdataframeFromFile():
    df = pd.read_csv(fileRoute)
    print(df)

#printdataframeFromFile()

def searchByName():
    df = pd.read_csv(fileRoute)
    print(df['carrera'][1])

#searchByName()

def looksbyRange():
    df = pd.read_csv(fileRoute)
    #print(df['edad']>23) #print with condition but prints true or fals if the condition is true

    filtered = df['edad'] > 23  #aplies the condition and the result can be used in the same dataframe to filter by the result, in this cases values greaters than 23
    df_filtered = df[filtered]

    print(df_filtered)
#looksbyRange()


def dataframeMethods():
    df = pd.read_csv(fileRoute)
    print(f"---------Head-------------\n  {df.head(10)} \n\n -------Tail-----------\n {df.tail(10)}")

dataframeMethods()
