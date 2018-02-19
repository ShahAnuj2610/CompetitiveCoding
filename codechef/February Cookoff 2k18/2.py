from math import ceil

t = int(raw_input())

for _ in xrange(t):
    divisors = set()
    n, a, b, c = map(int, raw_input().split())
    count = 0
    for i in xrange(1, int(n**0.5) + 3):
        if not n % i:
            divisors.add(i)
            divisors.add(n/i)

    for i in divisors:
        if i <= a:
            for j in divisors:
                if j <= b:
                    if not (n % (i*j)):
                        if (n/(i*j)) <= c:
                            count += 1
    print count
