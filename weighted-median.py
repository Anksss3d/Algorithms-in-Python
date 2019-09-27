import math


def fun2(X, W, w1, w2):
    print("in function now w1="+str(w1)+", w2="+str(w2))
    pivot = SELECT(X)
    X1 = []
    X2 = []
    W1 = []
    W2 = []
    for i in range(1, len(X)):
        if X[i] < pivot:
            X1.append(X[i])
            W1.append(W[i])
        elif X[i] > pivot:
            X2.append(X[i])
            W2.append(W[i])
    print("In Fun2")
    print(X1)
    print(W1)
    print(sum(W1))
    print(X2)
    print(W2)
    print(sum(W2))
    if sum(W1) < w1 and sum(W2) <= w2:
        return pivot
    elif sum(W1) >= w1:
        return fun2(X1, W1, w1, sum(W1)-w1)
    else:
        return fun2(X2, W2, sum(W2)-w2, w2)


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
W = [0.1, 0.05, 0.4, 0.17, 0.03, 0.13, 0.11, 0.01]

print(fun2(X, W, 0.5, 0.5))

