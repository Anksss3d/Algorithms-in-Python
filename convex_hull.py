import math
import matplotlib.pyplot as plt
import numpy as np


def isOnRight(p0,p1,p2):
    v1 = [p1[0]-p0[0], p1[1]-p0[1]]
    v2 = [p2[0]-p0[0], p2[1]-p0[1]]
    det = v1[0]*v2[1] - v1[1]*v2[0]
    if det > 0:
        print("for "+str(p0)+" and "+str(p1)+", "+str(p2)+" is on left")
        return False
    else:
        print("for "+str(p0)+" and "+str(p1)+", "+str(p2)+" is on right")
        return True


def plotPoints(pts, hull, seq='normal'):
    plt.clf()
    for i in range(0, len(pts)):
        if seq == 'normal':
            plt.text(pts[i][0]+0.1, pts[i][1], '(%d,%d)' % (pts[i][0], pts[i][1]), horizontalalignment="left")
        else:
            plt.text(pts[i][0]+0.1, pts[i][1], "p%d" % i, horizontalalignment="left")
    plt.xticks(np.arange(0, 25, 1))
    plt.yticks(np.arange(0, 25, 1))

    xh = [x[0] for x in hull]
    yh = [x[1] for x in hull]

    xs = [x[0] for x in pts]
    ys = [x[1] for x in pts]

    plt.scatter(xs, ys, c="red")

    xh.append(xh[0])
    yh.append(yh[0])

    plt.plot(xh, yh, 'ro-', c="green")

    plt.show()


def getLowestPt(pts):
    pt = pts[0]
    ind = 0
    for i in range(0, len(pts)):
        if pts[i][1] < pt[1]:
            pt = pts[i]
            ind = i
    return pt


def getPolarAngles(pts, lowest_pt):
    angles = []
    i=0
    for pt in pts:
        if(pt != lowest_pt):
            if (lowest_pt[0]-pt[0]) != 0:
                angle = math.atan((lowest_pt[1]-pt[1])/(lowest_pt[0]-pt[0]))
            else:
                angle = math.pi/2
            if pt[1] == lowest_pt[1]:
                if pt[0] < lowest_pt[0]:
                    angles.insert(i, 180)
                else:
                    angles.insert(i, 0)
            else:
                angles.insert(i, round(((180 + math.degrees(angle)) % 180), 2))
        else:
            angles.insert(i,-9999)




        i = i + 1
    return angles


def merge(pts, angles, p, mid, r):
#    print("value of p: %d, mid: %d, r: %d" %(p,mid,r))
    n1 = mid-p+1
    n2 = r-mid
    i = 0
    j = 0
    k = p
    A1 = [0.0] * n1
    A2 = [0.0] * n2
    pt1 = [[0, 0]] * n1
    pt2 = [[0, 0]] * n2
    for m in range(p, mid+1):
        A1[i] = angles[m]
        pt1[i] = pts[m]
        i = i+1
        m = m+1
    for m in range(mid+1, r+1):
        A2[j] = angles[m]
        pt2[j] = pts[m]
        j = j+1
        m = m+1
    i = 0
    j = 0
    while i<n1 and j<n2:
        if A1[i]<A2[j] :
            angles[k] = A1[i]
            pts[k] = pt1[i]
            i = i+1
        else:
            angles[k] = A2[j]
            pts[k] = pt2[j]
            j = j+1
        k = k+1

    while i<n1:
        angles[k] = A1[i]
        pts[k] = pt1[i]
        i = i + 1
        k = k+1

    while j<n2:
        angles[k] = A2[j]
        pts[k] = pt2[j]
        j = j + 1
        k = k+1


def mergeSort(pts, angles, p, r):

    if p<r:
        mid = int((p+r)/2)
#        if p < r:
#            print("angles Before Sorting: " + angles[p:r+1].__str__())
#           print("points Before Sorting: " + pts[p:r+1].__str__())
        mergeSort(pts, angles, p, mid)
        mergeSort(pts, angles, mid+1, r)
        merge(pts, angles, p, mid, r)
#        if p < r:
#           print("Angles After Sorting: " + angles[p:r+1].__str__())
#           print("points After Sorting: " + pts[p:r+1].__str__())


def findConvexHull(pts):
    hull = []
    for pt in pts[0:3]:
        hull.append(pt)

    for i in range(3, len(pts)):
        while isOnRight(hull[len(hull)-2], hull[len(hull)-1], pts[i]):
            hull.pop()
        hull.append(pts[i])

    return hull


def main():
    pts = []
    for i in range(0, 10):
        pts.append([np.random.randint(low=1, high=10), np.random.randint(low=1, high=10)])
    print("Points is: " + pts.__str__())
    lowest_pt = getLowestPt(pts)
    print("Lowest point is: "+lowest_pt.__str__())
    angles = getPolarAngles(pts, lowest_pt)
    print("Angles are : "+angles.__str__())
    mergeSort(pts, angles, 0, len(angles)-1)
    print("Sorted Angles are : " + angles.__str__())
    print("Sorted Points are : " + pts.__str__())
    hull = findConvexHull(pts)
    print("Sorted Points are : " + pts.__str__())
    plotPoints(pts,hull)


if __name__ == "__main__":
    main()