t = int(raw_input())
    
for _ in xrange(t):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())
    summ = sum(a)
    curr_sum = a[0]
    max_sum = a[0]
    maxLeft = a[n-1]
    maxRight = a[0]
    if k == 1:
        var = n
    else:
        var = 2*n
  
    for i in xrange(1, var):
        curr_sum = max(curr_sum + a[i%n], a[i%n])
        max_sum = max(max_sum, curr_sum)
  
    curr_left = a[n-1]
    for i in xrange(n-2, -1, -1):
        curr_left += a[i]
        maxLeft = max(curr_left, maxLeft)
    curr_right = a[0]
    for i in xrange(1, n):
        curr_right += a[i]
        maxRight = max(maxRight, curr_right)
    
    if k == 1 or k == 2:
        print max(max_sum, k*summ)
    else:
        print max(max_sum, k*summ, maxLeft + (k-2)*summ + maxRight) 