def dobleNumber(x): #normal function with name, lamnda is an anonymous function
    return x *2

print(dobleNumber(20))

double = lambda x:x*2

print(double(30))
print("\n\n----LAMNDA IN LISTS------------\n\n")

myList = [1,2,3,4,5,6,7,8,9,10,11]
par_elements = list(filter(lambda x: (x%2==0) , myList))
print(par_elements)
