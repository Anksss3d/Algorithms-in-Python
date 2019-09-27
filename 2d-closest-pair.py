import math
import numpy as np
import matplotlib.pyplot as plt


def plotPoints(pts, min_pts, seq="normal"):
    plt.clf()
    for i in range(0, len(pts)):
        if seq == 'normal':
            plt.text(pts[i][0]+0.2, pts[i][1]+0.2, '(%d,%d)' % (pts[i][0], pts[i][1]), horizontalalignment="left")
        else:
            plt.text(pts[i][0]+0.1, pts[i][1], "p%d" % i, horizontalalignment="left")
    plt.xticks(np.arange(0, 25, 1))
    plt.yticks(np.arange(0, 25, 1))

    xs = [x[0] for x in pts]
    ys = [x[1] for x in pts]
    plt.scatter(xs, ys, c="red")

    xh = [x[0] for x in min_pts]
    yh = [x[1] for x in min_pts]
    plt.plot(xh, yh, 'ro-', c="green")
    plt.show()


def euclidean(pt1, pt2):
    return math.sqrt(math.pow(pt1[0]-pt2[0], 2)+math.pow(pt1[1]-pt2[1], 2))


def minimum(d1, d2, pts1, pts2):
    if d1 < d2:
        return d1, pts1
    else:
        return d2, pts2


def merge_d1d2(x_sorted_pts, d):
    new_x_sorted = []
    final_pts = [[0, 0], [0, 0]]
    mid = (x_sorted_pts[(len(x_sorted_pts) // 2)-1][0] + x_sorted_pts[len(x_sorted_pts) // 2][0])/2
    for pt in x_sorted_pts:
        if (mid - d) < pt[0] < (mid + d):
            new_x_sorted.append(pt)
    new_y_sorted = sorted(new_x_sorted, key=lambda x: x[1])
    for i in range(len(new_y_sorted)):
        mx = min(len(new_y_sorted)-i-1, 6)
        for j in range(1, mx):
            if euclidean(new_y_sorted[i], new_y_sorted[i+j]) < d:
                d = euclidean(new_y_sorted[i], new_y_sorted[i+j])
                final_pts[0] = new_y_sorted[i]
                final_pts[1] = new_y_sorted[i+j]
    return d, final_pts


def closest_pair_2d(x_sorted_pts):
    if len(x_sorted_pts) == 2:
        return euclidean(x_sorted_pts[0], x_sorted_pts[1]) , x_sorted_pts
    elif len(x_sorted_pts) == 3:
        d01 = euclidean(x_sorted_pts[0], x_sorted_pts[1])
        d12 = euclidean(x_sorted_pts[2], x_sorted_pts[1])
        d02 = euclidean(x_sorted_pts[0], x_sorted_pts[2])

        if d01 < d12 and d01 < d02:
            return d01, [x_sorted_pts[0], x_sorted_pts[1]]
        elif d02 < d12 and d02 < d01:
            return d02, [x_sorted_pts[0], x_sorted_pts[2]]
        else:
            return d12, [x_sorted_pts[1], x_sorted_pts[2]]

    else:
        mid = len(x_sorted_pts) // 2
        d1, pts1 = closest_pair_2d(x_sorted_pts[:mid])
        d2, pts2 = closest_pair_2d(x_sorted_pts[mid:])
        d, min_pts = minimum(d1, d2, pts1, pts2)
        final_min, final_pts = merge_d1d2(x_sorted_pts, d)
        if d != final_min:
            return final_min, final_pts
        else:
            return d, min_pts


ptts = []
for i in range(10):
    ptts.append([np.random.randint(20), np.random.randint(20)])
pts = []
for i in ptts:
    if not pts.__contains__(i):
        pts.append(i)
print(pts)
pts.sort(key=lambda x: x[0])
dist, min_pts = closest_pair_2d(pts)
print("Minimum distance is: " + str(dist))
print("Closest Points Are: "+min_pts.__str__())
plotPoints(pts, min_pts)

