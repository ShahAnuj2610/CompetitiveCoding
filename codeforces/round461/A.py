x, y = map(int, raw_input().split())
if y == 0:
    print 'No'
else:
    temp = x-(y-1)
    if temp < 0:
        print 'No'
    elif temp % 2:
        print 'No'
    else:
        print 'Yes'
