import math

def fun(X, k):
    pivot = SELECT(X)
    print("Selected Pivot is: "+pivot.__str__())
    X1 = []
    X2 = []
    for i in range(0, len(X)):
        if X[i] < pivot:
            X1.append(X[i])
        elif X[i] > pivot:
            X2.append(X[i])

    if len(X1) == (k-1):
        return pivot
    elif len(X1) > (k-1):
        return fun(X1, k)
    else:
        return fun(X2, k-len(X1)-1)


def SELECT(A):
    print("Now Processing: "+A.__str__())
    if len(A) > 5:
        parts = len(A)/5
        newA = []
        for i in range(0, math.ceil(parts)):
            newA.append(SELECT(A[(5*i):(5*(i+1)-1)]))
        print("newA is : "+newA.__str__())
        return SELECT(newA)
    else:
        A.sort()
        print("returning median as : "+str(A[int(len(A)/2)]))
        return A[int(len(A)/2)]


X = [5, 1, 10, 7, 20, 3, 8, 27]

print(fun(X, 4))

