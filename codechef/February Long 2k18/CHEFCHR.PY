# Formatted code with proper identation
from itertools import permutations
import string

perms = [''.join(p) for p in permutations('chef')]

t = int(raw_input())

for _ in xrange(t):
    s = raw_input().replace(' ', '')
    s = s.translate(None, string.punctuation)
    count = 0
    for i in xrange(len(s)-4+1):
        temp = ''
        for j in xrange(i, i+4):
            temp += s[j]
        if temp in perms:
            count += 1

    # print perms
    if count == 0:
        print 'normal'
    else:
        print 'lovely', count
