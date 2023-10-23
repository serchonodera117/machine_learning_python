import numpy as np

#empty arrays
#create arrays of ones - num of rows and n num of columns
print("\n\nARRAY WITH ONES------------------------------\n\n")
onesArray = np.ones((3,4)) 
print(onesArray)

print("\n\nARRAY WITH ZEROS------------------------------\n\n")
#create an empty array of zeros
zerosArray = np.zeros((3,4))
print(zerosArray)


print("\n\nARRAY WITH RANDOM NUMBERS------------------------------\n\n")
#create an array of random numbers
randomArray = np.random.random((2,2))
print(randomArray)

print("\n\nEMPTY ARRAY------------------------------\n\n")
#create an empty array
emptyArray = np.empty((3,4))
print(emptyArray)

print("\n\nONLY ONE VALUE------------------------------\n\n")
#creating an array with only one value
fullArray = np.full((3,3), 7)
print(fullArray)

print("\nSapacing values------------------------------\n\n")
#CREATING A VALYE WITH SPACING VALUES 
space1 = np.arange(0,30,5)
print(space1)

space2 = np.linspace(0,4,5)
print(space2)


print("\n Creating an identity array------------------------------\n\n")
identity1 = np.eye(4,4)
print(identity1)

identity2 = np.eye(4,4)
print(identity2)



print("\n Knowing num of dimentions of an array------------------------------\n\n")
#knowing num of dimention of an array
dimentions = np.array([(1,2,3,5), (1,2,4,5)])
print(dimentions.ndim)


print("\n Knowing  data type------------------------------\n\n")
dataTypeArray = np.array([1,2,4])
dataTypeArrayFloat = np.array([1.5,2.23,4.23])
dataTypeArrayString = np.array(["c","B","a"])
dataTypeArrayMultiple= np.array([12, 1.56,"a"])
print(dataTypeArray.dtype)
print(dataTypeArrayFloat.dtype)
print(dataTypeArrayString.dtype)
print(dataTypeArrayMultiple.dtype)



print("\n Knowing size and shape of array------------------------------\n\n")
experimentalArray = np.array([1,3,5,4])
print(experimentalArray.size)
print(experimentalArray.shape)

print("\n Reshape of array------------------------------\n\n")
a = np.array([(8,4,5), (2,3,4)])
print(a)
print("resped 3x2")
a = a.reshape(3,2)
print(a)


print("\n Get values from an array------------------------------\n\n")
a = np.array([(8,4,5), (2,3,4)])
print(a[0:, 2]) #double dot means that it's going to get the entire row

print("\n Array operations------------------------------\n\n")
a = np.array([1,2,4,5,6,7,8])
print(a.min())
print(a.max())
print(a.sum())
print(np.sqrt(a))
print(np.std(a))