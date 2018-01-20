from itertools import permutations
  
t = int(raw_input())
  
for _ in xrange(t):
  a = map(int, raw_input().split())
  flag = False
  for i in permutations(a):
    if i[0] == i[2] and i[1] == i[3]:
      flag = True
      break
  if flag:
    print 'YES'
  else:
    print 'NO' 