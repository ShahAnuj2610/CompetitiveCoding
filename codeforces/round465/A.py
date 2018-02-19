n = int(raw_input())
count = 0

for i in xrange(1, n):
    if (n-i) % i == 0:
        count += 1

print count
