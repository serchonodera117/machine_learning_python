import pandas as pd

def first_function():
    numbers = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
    sum_whole_serie= numbers.sum()
    minValue = numbers.min()
    maxValue = numbers.max()
    myStd = numbers.std()

    sumarize = numbers.describe()

    print(f"sum of the whole serie {sum_whole_serie}")
    print(f"minimun value:  {minValue}")
    print(f"maximun value: {maxValue}")
    print(f"standard desviation: {myStd}")
    print(f"\n sumarize of the whole serie: \n{sumarize}")


#first_function()

def filter_by():
    series = pd.Series({'math': 8, 'economy': 6, 'programing': 10, 'physics': 5})
    filter = series[series > 6]
    
    sorted_values = series.sort_values()
    sorted_by_index = series.sort_index(ascending=False)

    print(f"sorted values: \n{sorted_values} \n")
    print(f"filtered series by values greaters than 6 \n  {filter} \n")

    print(f"sorted by index : \n{sorted_by_index}")

#filter_by()

def scalable_value():
    data = 5
    dataSeries = pd.Series(data, index=[0,1,2,3,4,5])
    print(f"Generated serie from the variable data (where 5 is the value and the array are the index):  {dataSeries}")

#scalable_value()

def serie_defined_index():
    dataList = ['Messi', 'Ronaldo', 'Xd']
    indices = ['psg', 'manchester', 'xddddd']

    myFSerie = pd.Series(index=indices, data=dataList)
    print(myFSerie)

serie_defined_index()