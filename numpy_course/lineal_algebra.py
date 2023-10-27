import numpy as np

def trasposition_of_an_array():
    m= np.array([[1,-1,3], [3, 2, 0]])
    one_col_mateiz = np.array([[1], [2], [3]])
    print(np.transpose(one_col_mateiz))

#trasposition_of_an_array()

def ecuation_system():
    A = np.array([
        [2, 1, -2],
        [3, 0,  1],
        [1, 1, -1]
    ])
    B = np.array([
        [-3],
        [5],
        [-2]
    ])


    print(f"Array A:\n {A} \n")
    print(f"Array B:\n {B} \n")

    print(f"B transposed: {np.transpose(B)} \n")

    X = np.linalg.solve(A,B)
    print(f"Solution X : \n",X)
    print(f"\n Is result correct?: {np.allclose(np.dot(A,X),B)}") #check if result is correct, true is correct, false is incorrect

#equation_system()

def second_equation_system():
    m1 = np.array([[2,7,3], [2,8,2], [1,3,1]])
    m2 = np.array([1,1,0])
    m2.shape=(3,1) #tranpose 3 rows one column
    print(f"Array 1: \n {m1}")
    print(f"Array 2: \n {m2}")
    print("---------------------------------")
    X = np.linalg.solve(m1, m2)
    print(f"Solution:\n {X}")

second_equation_system()