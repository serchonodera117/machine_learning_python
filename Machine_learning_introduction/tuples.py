def tuple_example():
    tuple = (0,0,0,0,3,304,50)
    tuple_b = ('a', 'b', 'c', 'd', 'e', 'f')
    print(tuple + tuple_b)
    duplicatedElements = tuple.count(0)
    specific_index = tuple.index(304)
    print("0 appears ", duplicatedElements, " times")
    print("index of 304 is ", specific_index)
tuple_example()
print("\n\n\n ----------CONVERSION TUPLE TO LIST-----------------\n\n\n")

def conversion_example():#to edit tuple values is necesary to convert tuple to list, because list are editable
    x = ('red', 'green', 'blue', 'grey')
    y = list(x)
    y[1] = "black"
    x = tuple(y)
    print(x)