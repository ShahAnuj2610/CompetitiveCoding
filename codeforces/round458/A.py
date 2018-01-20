#Pretests passed
n = int(raw_input())

a = map(int, raw_input().split())

ans = -1*float('inf')

for i in a:
  temp = int(abs(i)**0.5)
  if temp*temp != i:
    ans = max(ans, i)

print ans