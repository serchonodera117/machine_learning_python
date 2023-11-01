import pandas as pd

route = 'file_resources\characters_info.csv'
routeExcel = 'file_resources\characters_info.xlsx'
characters = pd.read_csv(route)

def testFile():
    print(characters) 

#testFile()

def conversion(): #conversion xls to csv 
    convert = pd.read_excel('file_resources\characters_info.xlsx')
    print(convert)
    convert.to_csv('converted_file_character_students.csv', index=None, header=True)

conversion()
