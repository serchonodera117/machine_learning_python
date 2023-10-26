import array as ar
import numpy as np

#arrays from array code
def arrays_module_array():
    matriz = ar.array('i',[1,2,3,4,5]) #i from int
    matriz1 = ar.array('d',[1,2,3,4.0,5.5]) #d from decimals
    matriz2 = ar.array('f',[1,2,3,4.0,5.5]) #f from float

    print(matriz)
    for i in matriz2:
        print(i)

arrays_module_array()

def array_numpy():
    matriz = np.array([1,2,3,4,5])
    print("array from numpy",matriz)

array_numpy()

def numpy_logic_operations():
    matris1 = np.array([1,3,4,5])
    matriz2 = np.array([5,3,2,1])
    print(f"Array 1: {matris1} \nArray 2: {matriz2} \n---------------------------\n\n\n")


    print("multiplication: ", matris1*matriz2)
    print("Division: ", matris1/matriz2)
    print("sum: ", matris1+matriz2)
    print("subtraction: ", matris1-matriz2)

numpy_logic_operations()