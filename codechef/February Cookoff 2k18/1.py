n = int(raw_input())

for _ in xrange(n):
    a = map(int, raw_input().split())
    cou = a.count(1)
    if cou == 0:
        print 'Beginner'
    elif cou == 1:
        print 'Junior Developer'
    elif cou == 2:
        print 'Middle Developer'
    elif cou == 3:
        print 'Senior Developer'
    elif cou == 4:
        print 'Hacker'
    else:
        print 'Jeff Dean'
