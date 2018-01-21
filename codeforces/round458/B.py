#System test passed
from collections import defaultdict

n = int(raw_input())

a = map(int, raw_input().split())

freq = defaultdict(int)

for i in a:
  freq[i] += 1

key = freq.keys()

for i in xrange(len(key)-1, -1, -1):
  if freq[key[i]]%2:
    print 'Conan'
    exit()

print 'Agasa'