import numpy as np 
import sys   #provide acces to variables from the interpreter
import time #to use time methods like measure time exexution of an algoeithm


#unidimentional and bidimentional arrays
a = np.array([1,2,4])
print('1D Array:')
print(a)

b = np.array([(1,3,5),(22,4,5)])
print('2D Array:')
print(b)


#comparation of space in memmory
#sys operation
s= range(1000)
print ("list result of python")
print (sys.getsizeof(5)*len(s))
print()
#numpy operation
d=np.arange(1000)
print ("list result of numpy array")
print (d.size*d.itemsize)


#time execution
SIZE = 100_000
L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x,y) for x,y in zip(L1, L2)]
print("Result of python list time:")
res = ((time.time()-start)*1000)
print(str(res) + " seconds")
print()

start = time.time()
result = A1+A2
print("Result of NumPy array : ")
res = ((time.time()-start)*1000)
print( str(res) + ' milliseconds')