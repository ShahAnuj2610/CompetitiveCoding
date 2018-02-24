t = int(raw_input())

for _ in xrange(t):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    d = map(int, raw_input().split())
    b = map(int, raw_input().split())
    pair = []
    for i in xrange(n):
        pair.append([a[i], d[i]])

    pair = sorted(pair, key=lambda x: x[0])
    # print pair
    start = 0
    end = n-1
    rem = sum(d)
    for i in xrange(k):
        temp = rem-b[i]
        rem -= temp
        if (i+1) % 2:
            while temp != 0:
                temp2 = min(temp, pair[start][1])
                pair[start][1] -= temp2
                temp -= temp2
                if pair[start][1] == 0:
                    start += 1
        else:
            while temp != 0:
                temp2 = min(temp, pair[end][1])
                pair[end][1] -= temp2
                temp -= temp2
                if pair[end][1] == 0:
                    end -= 1
        # print pair

    ans = 0
    for i in pair:
        ans += i[0]*i[1]

    print ans
