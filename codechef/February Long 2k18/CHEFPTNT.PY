# Formatted code with proper identation
t = int(raw_input())

for _ in xrange(t):
    n, m, x, k = map(int, raw_input().split())
    s = raw_input()
    even = s.count('E')
    odd = s.count('O')
    for i in xrange(m):
        if (i+1) % 2:
            n -= min(odd, x)
            odd = max(0, odd-min(x, odd))
        else:
            n -= min(even, x)
            even = max(0, even-min(x, even))
    if n <= 0:
        print 'yes'
    else:
        print 'no'
