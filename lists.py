def lists():
    myList = [1,2,3,4,5,6]
    string_list = ["xd", "a", "curso"]

    generic_list = [1,2,3,4,"xdddd", 0.7, ["list","string"]]

    #print(myList, string_list[1])
    print(generic_list)


def sum_of_lists(list1, list2):
    return list1+list2

def test_list():
    totalLists  = sum_of_lists([1,2,3,4,5], [6,7,8,9,10])
    print("list ",totalLists, "\n list size: ", len(totalLists))
    #cut lists
    print("\n-------------------------------\n")
    print("cut lists 0 position to thirtd position: ",totalLists[0:3]) #dpuble dot sets the range of positions to take
    print("cut lists second position to final position: ",totalLists[2:]) 
    print("cut lists since begining to 6th position: ",totalLists[:6]) 

    print("\n-------------------------------\n")

    totalLists.insert(6,"new") #requiere 2 parameters index and object
    totalLists.append("added to the final")
    totalLists.pop(1) #removing array element by index
    totalLists.remove(7) #removinig the first element with that value
    print("list ",totalLists, "\n list size: ", len(totalLists))

#test_list()

def addingmultiplevaluestoalist():
    list1= [1,2,3,4,5,0,6,6,7]
    list2 = ["a", "b", "c", "d", "e", "f"]
    list1.extend(list2) 
    print(list1)

#addingmultiplevaluestoalist()

def sorting_lists():
    list1= [41,2,123,4251,6]
    list2= ["cas", "zansd", "pi", "art", "def", "bar"]
    list2.sort()
    list1.sort()
    print("list 1:", list1, "\n list2:", list2)
 

#sorting_lists()

def reversing_lists():
    list1= [1,2,3,4,5]
    list1.reverse()
    print("list 1:", list1)

reversing_lists()