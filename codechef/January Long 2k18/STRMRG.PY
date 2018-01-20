def lcs(X , Y):
    m = len(X)
    n = len(Y)
 
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    return L[m][n]
 
t = int(raw_input())
 
for _ in xrange(t):
  n, m = map(int, raw_input().split())
  a = raw_input()
  b = raw_input()
  tempA = a[0]
  tempB = b[0]
  for i in xrange(n-1):
    if a[i] != a[i+1]:
      tempA += a[i+1]
  for i in xrange(m-1):
    if b[i] != b[i+1]:
      tempB += b[i+1]
 
  lenA = len(tempA)
  lenB = len(tempB)
  dp = [[-1 for _ in xrange(lenB)] for _ in xrange(lenA)]
  temp = lcs(tempA, tempB) 
  print temp + (lenA - temp) + (lenB - temp)