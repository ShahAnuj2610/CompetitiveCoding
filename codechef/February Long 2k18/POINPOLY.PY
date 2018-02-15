from math import floor
from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

dx = [-1, 0, 1]
dy = [-1, 0, 1]


def insidePoly(x, y):
    if x > l and x < r and y > u and y < d:
        return True
    return False


def solve(x, y, count):
    if count == 0:
        return True
    else:
        vis[x][y] = True
        for i in dx:
            for j in dy:
                if i != 0 or j != 0:
                    try:
                        vis[x+i][y+j]
                    except:
                        if insidePoly(x+i, y+j):
                            ans.append((x+i, y+j))
                            if (solve(x+i, y+j, count-1)):
                                return True
        return False


t = int(raw_input())

for _ in xrange(t):
    ans = []
    vis = defaultdict(dict)
    n = int(raw_input())
    l = float('inf')
    r = -float('inf')
    u = float('inf')
    d = -float('inf')
    for i in xrange(n):
        x, y = map(int, raw_input().split())
        l = min(l, x)
        r = max(r, x)
        u = min(u, y)
        d = max(d, y)

    medX = (l+r)/2
    medY = (u+d)/2
    count = int(floor(n/10))
    oriCount = count
    if insidePoly(medX, medY):
        ans.append((medX, medY))
        count -= 1

    if solve(medX, medY, count):
        for i in xrange(oriCount):
            print ans[i][0], ans[i][1]
    else:
        print -1
