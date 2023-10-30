import pandas as pd

#conversion excersises
def simple_string_serie():
    colors = pd.Series(["red","blue","yellow", "green", "purple"])
    print(colors)

def use_of_dictionaries():
    materias = pd.Series({'Math': 60, 'Physics': 100, 'Chemestry':78})
    print(materias)
    #accesing to a dictionary part

    print(f"Physics: {materias['Physics']} two signatures:\n {materias[['Math','Chemestry']]}")
#use_of_dictionaries()

def series_properties():
    numbers = pd.Series([1,2,3,4,5,6,7,8,9,0])
    size_serie = numbers.size
    index_serie = numbers.index
    data_serie = numbers.dtype
    print(f"number size: {size_serie}  Data tyoe: {data_serie} \n\n index: {index_serie}")

    #acces to a serie

    print(f"{numbers[2]}")


#series_properties()


def basic_operations():
    numbers = pd.Series([1,2,3,4,5,6])
    print(f"basic operations {numbers*2}")

basic_operations()
