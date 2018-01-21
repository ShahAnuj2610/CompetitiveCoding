def solve(ini, rep):
  summ = ini%3 + (((k-3)/4)*20)%3
  rem = (k-3)%4
  for i in xrange(rem):
    summ += rep[i]
    summ %= 3
  return summ%3

t = int(raw_input())

for _ in xrange(t):
  k, d0, d1 = map(int, raw_input().split())
  temp = (d0 + d1)%10
  summ = d0 + d1
  ans = -1
  if k == 2:
    ans = (d0 + d1)%3
  else:
    if temp == 0:
      ans = 1
    elif temp == 1:
      ans = solve(summ+1, [2, 4, 8, 6])
    elif temp == 2:
      ans = solve(summ+2, [4, 8, 6, 2])
    elif temp == 3:
      ans = solve(summ+3, [6, 2, 4, 8])
    elif temp == 4:
      ans = solve(summ+4, [8, 6, 2, 4])
    elif temp == 5:
      ans = 0
    elif temp == 6:
      ans = solve(summ+6, [2, 4, 8, 6])
    elif temp == 7:
      ans = solve(summ+7, [4, 8, 6, 2])
    elif temp == 8:
      ans = solve(summ+8, [6, 2, 4, 8])
    else:
      ans = solve(summ+9, [8, 6, 2, 4])

  if ans:
    print 'NO'
  else:
    print 'YES'