def multiply(n):
    return n*5
    
myList = [1,2,3,4,5,6,7]
maped_list = list(map(multiply, myList)) #by following js logic, map reuqieres 2 parameters, code and the list,
                                        #in this case the code is the function multoply, that will multiply each 
                                        # item from list beacuse map function, and resylt is converted into a list

print("Map a list ading code into a function: ", maped_list)

def courses(course):
    return course.upper() #convert to upper case the characters

myTuple = ('php', 'python', 'java', 'c#', 'javascript', 'c++', 'css', 'kotlin')
updated_tuple = tuple(map(courses, myTuple))
print("Upercase strings: ",updated_tuple)


def filterImpar(n):
    if(n%2 == 1):
        return n

numberList = [1,2,3,4,5,6,7,8,9,10,11,12,13]
updatedlist = list(filter(filterImpar, numberList))

print("Filtered list: ",updatedlist)