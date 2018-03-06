n = int(raw_input())

a = map(int, raw_input().split())

a.sort()

ans = 0

for i in a:
    ans += abs(i)

print ans
