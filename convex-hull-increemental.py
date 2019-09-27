import numpy as np
import math
import matplotlib.pyplot as plt


def isOnRight(p0, p1, p2):
    v1 = [p1[0] - p0[0], p1[1] - p0[1]]
    v2 = [p2[0] - p0[0], p2[1] - p0[1]]
    det = v1[0] * v2[1] - v1[1] * v2[0]
    if det > 0:
        return False
    else:
        return True


def findConvexHull(pts):

    if len(pts) <= 3:
        return pts
    else:
        hull = [[0, 0], [0, 0], [0, 0]]
        if not isOnRight(pts[0], pts[1], pts[2]):
            hull = [pts[0], pts[1], pts[2]]
            lastpt = 2
        else:
            hull = [pts[0], pts[2], pts[1]]
            lastpt = 1
        for i in range(3, len(pts)):
            u = lastpt
            count1=0
            while isOnRight(pts[i], hull[u], hull[(u + 1) % len(hull)]):
                u = (u + 1) % len(hull)
                count1 = count1+1


            l = lastpt
            count2 = 0
            while not isOnRight(pts[i], hull[l], hull[((l - 1) + len(hull) % len(hull))]):
                l = ((l - 1) + len(hull) % len(hull))
                count2 = count2+1
            lg = math.log((i+1),2)
            myflag = True
            if count1>lg or count2>lg:
                myflag = False
            print("for n = %d \t log(n) = %f \t count1 = %d \t count2 = %d \t %s"%(i+1, lg, count1, count2, str(myflag)))
            if l != u:
                flag = True
                while flag:
                    if (l + 1) % len(hull) != u:
                        hull.pop((l + 1) % len(hull))
                        if u != 0:
                            u = ((u - 1) + len(hull) % len(hull))
                    else:
                        flag = False
            hull.insert(l + 1, pts[i])
            lastpt = l + 1
#           plotPoints(pts, hull)

        return hull


def plotPoints(pts, hull, seq='normal'):
    plt.clf()
    for i in range(0, len(pts)):
        if seq == 'normal':
            plt.text(pts[i][0] + 0.1, pts[i][1], '(%d,%d)' % (pts[i][0], pts[i][1]), horizontalalignment="left")
        else:
            plt.text(pts[i][0] + 0.1, pts[i][1], "p%d" % i, horizontalalignment="left")
    plt.xticks(np.arange(0, 25, 1))
    plt.yticks(np.arange(0, 25, 1))

    xh = [x[0] for x in hull]
    yh = [x[1] for x in hull]

    xs = [x[0] for x in pts]
    ys = [x[1] for x in pts]

    plt.scatter(xs, ys, c="red")
    if hull:
        xh.append(xh[0])
        yh.append(yh[0])

    plt.plot(xh, yh, 'ro-', c="green")

    plt.show()


def merge(pts, p, mid, r):
    n1 = mid - p + 1
    n2 = r - mid
    i = 0
    j = 0
    k = p
    pt1 = [[0, 0]] * n1
    pt2 = [[0, 0]] * n2
    for m in range(p, mid + 1):
        pt1[i] = pts[m]
        i = i + 1
        m = m + 1
    for m in range(mid + 1, r + 1):
        pt2[j] = pts[m]
        j = j + 1
        m = m + 1
    i = 0
    j = 0
    while i < n1 and j < n2:
        if pt1[i] < pt2[j]:
            pts[k] = pt1[i]
            i = i + 1
        elif pt1[i] > pt2[j]:
            pts[k] = pt2[j]
            j = j + 1
        else:
            if pt1[i][1] < pt2[j][1]:
                pts[k] = pt1[i]
                i = i + 1
            else:
                pts[k] = pt2[j]
                j = j + 1
        k = k + 1

    while i < n1:
        pts[k] = pt1[i]
        i = i + 1
        k = k + 1

    while j < n2:
        pts[k] = pt2[j]
        j = j + 1
        k = k + 1


def mergeSort(pts, p, r):
    if p < r:
        mid = int((p + r) / 2)
        mergeSort(pts, p, mid)
        mergeSort(pts, mid + 1, r)
        merge(pts, p, mid, r)


def main():
    ptt = []
    for i in range(0, 15):
        ptt.append([np.random.randint(low=1, high=10), np.random.randint(low=1, high=10)])

    pts = []
    for i in ptt:
        if i not in pts:
            pts.append(i)
    mergeSort(pts, 0, len(pts) - 1)
    hull = findConvexHull(pts)
    print("Final Hull is : " + pts.__str__())
    print("Sorted Points are : " + pts.__str__())
    plotPoints(pts, hull)


if __name__ == "__main__":
    main()
