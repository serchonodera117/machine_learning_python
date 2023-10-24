def range_in_cicle():
    for i in range(0,7):
        print("posirion: ", i, end=", ") #reserved word 'end' works to use the end of each element itetation in a list or range from cycle

def cycle_ramge_elements():
    for i in range(1, 10, 2): #third parameter generate steps, in this case goes by each 2 numbers
        print(i, end=", ") #

def triangle():
    for i in range(10):
        for j in range(i):
            print(i, end=" ")
        print()

triangle()

def reverse_range_():
    for i in reversed(range(10)):
        print("posirion: ", i, end=", ")

reverse_range_()

def conversion_range_to_list():
    myList = list(range(1,8))
    print("conversion: ", myList)

conversion_range_to_list()