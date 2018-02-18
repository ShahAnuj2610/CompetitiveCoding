from math import ceil

t = int(raw_input())

for _ in xrange(t):
    n, a, b, c = map(int, raw_input().split())
    count = 0
    # for x in xrange(1, a+1):
    #     tempX = int(ceil(n/x))
    #     low = 1
    #     high = min(tempX+1, b+1)
    #     while low <= high:
    #         mid = (low+high)/2
    #         tempZ = int(ceil(tempX/mid))
    #         if x*mid*tempZ == n and tempZ <= c:
    #             count += 1
    #             high = mid-1
    #         elif x*mid*tempZ < n:
    #             low = mid+1
    #         else:
    #             high = mid-1
    #     # for y in xrange(1, min(tempX+1, b+1)):
    #     tempZ = int(ceil(tempX/y))
    #     if x*y*tempZ == n:
    #         count += 1
    cuberoot = int(n**(1.0/3))
    for x in xrange(1, min(cuberoot+2, a)+1):
        for y in xrange(1, min(cuberoot+2, b)+1):
            for z in xrange(1, min(cuberoot+2, c)+1):
                if x*y*z == n:
                    count += 1
    print count
