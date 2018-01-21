t = int(raw_input())

for _ in xrange(t):
  n, k, s = map(int, raw_input().split())
  if n < k:
    print -1
  else:
    curr = 0
    day = 0
    box = 0
    flag = True
    while True:
      for i in xrange(5):
        if day == s:
          break
        if curr < k:
          curr += n
          box += 1
        curr -= k
        day += 1
      if day == s:
        break
      if curr < 2*k:
        curr += (n-k)
        box += 1
        day += 1
      if day == s:
        break
      if curr < k:
        flag = False
        break
      curr -= k
      day += 1
    if flag:
      print box
    else:
      print -1
      
    