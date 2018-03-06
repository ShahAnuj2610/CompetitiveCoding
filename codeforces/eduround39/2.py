n, m = map(int, raw_input().split())

while True:
    if n == 0 or m == 0:
        break
    if n >= 2*m:
        temp = n/(2*m)
        n -= (2*m*temp)
    elif m >= 2*n:
        temp = m/(2*n)
        m -= (2*n*temp)
    else:
        break

print n, m
