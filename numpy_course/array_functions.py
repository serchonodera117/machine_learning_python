import  numpy as np

def array2d():
    m = np.arange(9).reshape(3,3)
    print(m.shape)
    print(m.size)#length
    print(m.ndim)#num of dimentions

    zero_array = np.zeros((4,2))#generate a zeros arrays
    print(zero_array)

    otherArrayForm = np.linspace(99,88, 5)
    print(otherArrayForm)

array2d()

def array3d():
    myArray = np.arange(27).reshape(3,3,3)
    print(myArray)

print("\n\n\n---------------------")
array3d()