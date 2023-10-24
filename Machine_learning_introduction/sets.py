def setExample1():
    mySet = {1,2,3,4, "python", ("a","b")}
    mySet.add(500)
    #mySet.clear() without parameters it will delete all elements from the set}
    #mySet.discard(2) #discaard an element withoyt deleting it
    mySet.remove(2)

    print(mySet)

    print("\n\n----------OPERATIONS WITH SETS------------\n\n")

    setA = {1,2,3,4,5}
    setB = {5,4,6,7,8}
    print(setA | setB) #join sets with | operator, this union does NOT repeat the value or objects 
    print(setA & setB) #join sets with & operator, only add the repeated or duplicated values
    print(setA - setB) #join sets with - operator, only add the first values since the repeated values from set to the begining
    print(setA ^ setB) #join sets with ^ operator, does not add values that are duplicated in sets

setExample1()