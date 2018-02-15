# Formatted code with proper identation
t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())
    a = [int(x) for x in raw_input().split()]
    c, d, s = [int(x) for x in raw_input().split()]
    print max(a)*(c-1)
