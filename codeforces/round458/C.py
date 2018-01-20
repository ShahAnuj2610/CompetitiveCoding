#not done (dynamic programming)
from collections import defaultdict

def solve(i):
  if i == 1:
    return 0
  elif dp[i] != -1:
    return dp[i]
  else:
    temp = "{0:b}".format(i).count('1')
    dp[temp] = solve(temp)
    return dp[temp]

dp = [-1 for _ in xrange(10000)]

n = int(raw_input())

k = int(raw_input())

var = "{0:b}".format(n).count('1')

print var

for i in xrange(1, var):
  solve(i)

print dp[: 10]