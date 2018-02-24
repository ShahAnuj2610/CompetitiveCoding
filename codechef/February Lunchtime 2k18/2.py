t = int(raw_input())

for _ in xrange(t):
    n, u, d = map(int, raw_input().split())
    h = map(int, raw_input().split())
    flag = True
    for i in xrange(n):
        if i == n-1:
            break
        if h[i+1] > h[i]:
            if (h[i+1]-h[i]) > u:
                break
        elif h[i+1] < h[i]:
            if (h[i]-h[i+1]) > d:
                if flag:
                    flag = False
                else:
                    break
    print i+1
