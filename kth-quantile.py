import math

def k_quantiles(items, k):
    print("Solving for items: %s, \tk:%d: "%(items.__str__(), k))
    index = median_index(len(items))
    if k == 1:
        return []
    elif k % 2:
        n = len(items)
        left_index  = math.ceil((k // 2) * (n / k)) - 1                         #O(1)
        right_index = n - left_index - 1                                        #O(1)

        left = select(items, left_index)                                        #O(n)
        right = select(items, right_index)                                      #O(n)

        partition(items, left)                                                  #O(n)
        lower = k_quantiles(items[:left], k // 2)                               #Recursion
        partition(items, right)                                                 #O(n)
        upper = k_quantiles(items[right + 1:], k // 2)                          #Recursion
        ret = lower + [left, right] + upper

        print("Returning now from odd : %s \t lower:%s \t [left,right]:%s \t right:%s"%(ret.__str__(), lower.__str__(), [left,right].__str__(), upper.__str__()))
        return ret                                                              #O(1)
    else:
        index = median_index(len(items))                                        #O(1)
        median = select(items, index)                                           #O(n)
        partition(items, median)                                                #O(n)
        ret = k_quantiles(items[:index], k // 2) + [median] + k_quantiles(items[index + 1:], k // 2)    #Recusrion
        print("Returning now from even : " + ret.__str__())
        return ret

def median_index(n):
    if n % 2:
        return n // 2
    else:
        return n // 2 - 1

def partition(items, element):
    i = 0

    for j in range(len(items) - 1):
        if items[j] == element:
            items[j], items[-1] = items[-1], items[j]

        if items[j] < element:
            items[i], items[j] = items[j], items[i]
            i += 1

    items[i], items[-1] = items[-1], items[i]

    return i

def select(items, n):
    if len(items) <= 1:
        return items[0]

    medians = []

    for i in range(0, len(items), 5):
        group = sorted(items[i:i + 5])
        items[i:i + 5] = group
        median = group[median_index(len(group))]
        medians.append(median)

    pivot = select(medians, median_index(len(medians)))
    index = partition(items, pivot)

    if n == index:
        return items[index]
    elif n < index:
        return select(items[:index], n)
    else:
        return select(items[index + 1:], n - index - 1)

A = [10,20,16,4,1,11,29,54,55,33,22,14,3,9,45, 41,42,43,44,45,46,47,48,49]
Q = k_quantiles(A,5)
A.sort()
print("Sorted array is: "+A.__str__())
print("Quantile array is : "+Q.__str__())
