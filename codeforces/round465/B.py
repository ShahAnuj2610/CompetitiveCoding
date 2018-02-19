n = int(raw_input())
s = raw_input()

currX = 0
currY = 0

if s[0] == 'U':
    phase = 1
    currY = 1
else:
    phase = 0
    currX = 1


count = 0

for i in xrange(1, len(s)):
    if s[i] == 'U':
        currY += 1
    else:
        currX += 1
    if currY > currX and phase == 0:
        count += 1
        phase = 1
    elif currY < currX and phase == 1:
        count += 1
        phase = 0

print count
