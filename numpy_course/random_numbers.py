import  numpy as np

def random1():
    m = np.random.randint(10, size=(3,3)) #limit, size is designed to create an array
    d = np.random.rand(5, 4)#decimal values

    getRandomValueFromAnArray = np.random.choice([1,2,4,5,6])
    print("2d array with int value", m)
    print("\n2d array with int value", d)
    print("\n the chosen value from n array is: ", getRandomValueFromAnArray)
#random1()

def random_distribution():#prediction of all posible results
    m = (np.random.choice
         ([2,4,6], p=[0.5,0.5, 0.0], size=(6)))#array, probability 1, size of returned array 1
    print(m)

#random_distribution()
def random_distributionExcercise():
    m = (np.random.choice
         ([2,4,6,8,10], p=[0.2, 0.2, 0.2, 0.2, 0.2], size=(50))) #p is the probably that a value has to be chosen by the algorithm, each value must have a porcentage and the entire sum must be 1
    print(m)

random_distributionExcercise()