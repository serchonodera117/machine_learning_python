import numpy as np

def maximun_minimun():
    m = np.array([[1,2,3], [4,5,6], [7,8,0]])
    print(m)
    print("")
    print("maximun : ",np.amax(m), " minimun : ", np.amin(m))
    print("\n-----with axis---------\n")
    print("maximun rows : ", np.amax(m,0), " minimun cols : ", np.amin(m,1))


#maximun_minimun()

def rangeArray():
    m = np.array([[2,9,8], [7,6,5], [4,3,2]])
    print(np.ptp(m)) #range maximun - minimun values (9 - 1) beacuse is a 3X3 array
    print("Same range but with axis 0", np.ptp(m, axis=0))
    print("Same range but with axis 1", np.ptp(m, axis=1))

#rangeArray()

def percentiles():# q(n+1)/100
    m = np.array([[2,9,8], [7,6,5], [4,3,2]])  #can work with axis and without them
    print(np.percentile(m, 50, axis=1))#only works when n is impar (only arrays with impar length)

#percentiles()

def median():#median = (n+1)/2
    m = np.array([[2,9,8], [7,6,5], [4,3,2]]) #can work with axis and without them
    print(np.median(m, axis=0))

#median()

def arithmetic_media(): #(X1 + X2 +...Xn)/n
    m = np.array([[2,9,8], [7,6,5], [4,3,2]]) #can work with axis and without them
    print(np.mean(m))
#arithmetic_media()

def ponderan_average(): #(X1*P1 + . . .Xn*Pn)/Σ(P)
    m = np.array([1,2,3,4,5,6]) #when p is not defined, it's default value is 1
    print(np.average(m))

#ponderan_average()

def standard_desviation(): #√(Σ|x - x'|^2)/n
    m = np.array([1,2,3,4,5,6]) #when p is not defined, it's default value is 1
    print(np.std(m))

standard_desviation()