target = 'abcdefghijklmnopqrstuvwxyz'

s = list(raw_input())

start = 0

for i in xrange(len(s)):
    if s[i] <= target[start]:
        s[i] = target[start]
        start += 1
    if start >= len(target):
        break

if start == 26:
    print ''.join(s)
else:
    print -1
