import numpy as np

def matriz_with_list():
    matriz = np.array([1,2,4,5])

def anonympus_onject():
    anonObj = {
        "edad": 10,
        "peso": 70,
        "saludo": lambda: print("hi")
    }

    print(anonObj["edad"])
    anonObj["saludo"]()


def array2d():
    list = [
        [1,2,3],
        [5,6,7],
        [8,9,0]
    ]
    m2d = np.array([[1,2,4,5],[1,2,3,4]]) #both types are the same unlike the part to convert a list into an array, thats an implicit conversion
    m2dList = np.array(list)

    print("2D array: \n",m2d)
    print("2D array parsed a pyhon lisnt into a numpy array: \n",m2dList)


def quick_way_matriz2d():
    m = np.arange(25).reshape(5,5) #arange amount of values, and reshape the dimentions (dimentions must be divisble betwen the amount)
    print(m)

quick_way_matriz2d()