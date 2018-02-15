import sys
from fractions import Fraction
from collections import defaultdict

sys.setrecursionlimit(10000000)

mod = 10**9 + 7


def fib(n):
    # F = [[1, 1], [1, 0]]
    temp = 2*Fraction(d, l)*Fraction(d, l) - 1
    F = [[temp, Fraction(d, l)], [Fraction(d, l), 1]]
    power(F, n-1)
    print F
    return F[0][0]


def power(F,  n):
    if (n == 0):
        return
    # M = [[1, 1], [1, 0]]

    power(F, n/2)
    multiply(F, F)
    # print F
    if (n % 2 != 0):
        multiply(F, M)


def multiply(F, M):
    x = F[0][0]*M[0][0] + F[0][1]*M[1][0]
    y = F[0][0]*M[0][1] + F[0][1]*M[1][1]
    z = F[1][0]*M[0][0] + F[1][1]*M[1][0]
    w = F[1][0]*M[0][1] + F[1][1]*M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def xgcd(a, b):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy


def modinv(a, m):
    g, x, y = xgcd(a, m)
    return x % m


def solve(time):
    if time == 1:
        return Fraction(d, l)
    elif time == 2:
        return 2*Fraction(d, l)*Fraction(d, l) - 1
    else:
        try:
            return dp[time]
        except:
            dp[time] = 2*Fraction(d, l)*solve(time-1) - solve(time-2)
            return dp[time]


d = 2
l = 4
M = [(2*Fraction(d, l), -1), (1, 0)]
dp = {}
var = int(raw_input())
print solve(var)
print fib(var)
# t = int(raw_input())

# for _ in xrange(t):
#     dp = {}
#     l, d, time = map(int, raw_input().split())
#     ans = l*solve(time)
#     print (ans.numerator*power(ans.denominator, mod-2)) % mod
