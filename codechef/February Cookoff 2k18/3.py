t = int(raw_input())

for _ in xrange(t):
    n, k, b = map(int, raw_input().split())
    a = map(int, raw_input().split())
    a.sort()
    curr = 0
    next = 1
    count = 1
    while next < n:
        if a[curr] * k + b <= a[next]:
            count += 1
            next += 1
            curr += 1
        else:
            next += 1
    print count
