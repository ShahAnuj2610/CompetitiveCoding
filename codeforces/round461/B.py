n = int(raw_input())

count = 0

for i in xrange(1, n+1):
    for j in xrange(i, n+1):
        temp = i ^ j
        if temp >= i and temp >= j and (i+j) > temp and temp <= n:
            # print i, j, temp
            count += 1

print count
