t = int(raw_input())
  
for _ in xrange(t):
  x, n = map(int, raw_input().split())
  s = ['0' for _ in xrange(n)]
  s[x-1] = '2'
  if (n*(n+1)/2 - x)%2:
    print 'impossible'
  else:
    target = (n*(n+1)/2 - x)/2
    for i in xrange(n, 0, -1):
      if i != x:
        if i <= target:
          s[i-1] = '1'
          target -= i
    if target == 0:
      print ''.join(s)
    else:
      s = ['0' for _ in xrange(n)]
      s[x-1] = '2'
      target = (n*(n+1)/2 - x)/2
      for i in xrange(n-1, 0, -1):
        if i != x:
          if i <= target:
            s[i-1] = '1'
            target -= i
      if target == 0:
        print ''.join(s)
      else:
        print 'impossible'  