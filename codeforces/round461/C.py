n, k = map(int, raw_input().split())

if (n % k) != k-1:
    print 'No'
else:
    print 'Yes'
