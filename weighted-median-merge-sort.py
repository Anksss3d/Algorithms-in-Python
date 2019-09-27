def merge(X, W, p, mid, r):
    n1 = mid-p+1
    n2 = r-mid
    i = 0
    j = 0
    k = p
    A1 = [0] * n1
    A2 = [0] * n2
    pt1 = [0.0] * n1
    pt2 = [0.0] * n2
    for m in range(p, mid+1):
        A1[i] = W[m]
        pt1[i] = X[m]
        i = i+1
        m = m+1
    for m in range(mid+1, r+1):
        A2[j] = W[m]
        pt2[j] = X[m]
        j = j+1
        m = m+1
    i = 0
    j = 0
    while i<n1 and j<n2:
        if A1[i]<A2[j] :
            W[k] = A1[i]
            X[k] = pt1[i]
            i = i+1
        else:
            W[k] = A2[j]
            X[k] = pt2[j]
            j = j+1
        k = k+1

    while i<n1:
        W[k] = A1[i]
        X[k] = pt1[i]
        i = i + 1
        k = k+1

    while j<n2:
        W[k] = A2[j]
        X[k] = pt2[j]
        j = j + 1
        k = k+1


def mergeSort(X, W, p, r):

    if p<r:
        mid = int((p+r)/2)
        mergeSort(X, W, p, mid)
        mergeSort(X, W, mid+1, r)
        merge(X, W, p, mid, r)



X = [5, 1, 10, 7, 20, 3, 8, 27]
W = [0.1, 0.05, 0.4, 0.17, 0.03, 0.13, 0.11, 0.01]

mergeSort(W, X,0,len(X)-1)
print(X)
print(W)



sum = 0.0
i=0
while sum < 0.5:
    sum = sum + W[i]
    i = i+1
    print(sum)
print(sum)
print(W[i-1])
print("Median is: "+X[i-1].__str__())