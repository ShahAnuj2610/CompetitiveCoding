t = int(raw_input())
 
for _ in xrange(t):
  n = int(raw_input())
  arr = []
  ans = 0
  for i in xrange(n):
    temp = map(int, raw_input().split())
    temp.sort()
    arr.append(temp)
 
  lastPicked = float('inf')
  flag = True
  for i in xrange(n-1, -1, -1):
    low = 0
    high = n-1
    index = -1
    while low <= high:
      mid = (low + high)/2
      if arr[i][mid] < lastPicked:
        index = mid
        low = mid + 1
      else:
        high = mid - 1
    
    if index == -1:
      flag = False
      break
 
    ans += arr[i][index]
    lastPicked = arr[i][index]
  
  if not flag:
    print -1
  else:
    print ans