import  numpy as np

#*0 are rows, example:
# [1,2,3,4]  |
# [1,2,3,4]  |
# _________+ V
# [2,4,6,8]
#
#1 are cols, example
# ----------> +
# [1,2,3,4]| (10)
# [1,2,3,4]| (10)  : [10 10]#


def array_axis():
    m = np.array([[0,1,2,3], [4,5,6,7]]) #axis ara coll and rows, 0 are rows, and 1 are cols
    print(m)
    print("Sum cols")
    print(np.sum(m, axis=1))

#array_axis()

def concatenation_Arrays():
    m1 = np.array([[1,1], [1,1]])
    m2 = np.array([[2,2,], [2,2]])

    print("Array 1 : \n", m1, "\nArray 2 : \n", m2)
    print("")
    print("Cocatenated Array by rows :  \n",np.concatenate([m1,m2], axis=0))
    print("\n Cocatenated Array by cols :  \n",np.concatenate([m1,m2], axis=1))

concatenation_Arrays()