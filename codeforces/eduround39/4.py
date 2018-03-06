import sys

sys.setrecursionlimit(10000000)

from collections import defaultdict
from heapq import heappush, heappop

n, m, k = map(int, raw_input().split())

heap = defaultdict(list)

for i in xrange(n):
    s = raw_input()
    for j in xrange(len(s)):
        if s[j] == '1':
            heappush(heap[i], j)

for i in xrange(k):
    timediff1 = []
    timediff2 = []
    for j in xrange(len(heap)):
        if len(heap[j]) > 0:
            if len(heap[j]) == 1:
                timediff1.append((1, j))
                timediff2.append((1, j))
            else:
                #(heap[j][-1]-heap[j][0])-(heap[j][-1]-heap[j][1])
                #(heap[j][-1]-heap[j][0])-(heap[j][-2]-heap[j][0])
                timediff1.append((heap[j][1] - heap[j][0], j))
                timediff2.append((heap[j][-1] - heap[j][-2], j))
    timediff1 = sorted(timediff1, key=lambda x: x[0], reverse=True)
    timediff2 = sorted(timediff2, key=lambda x: x[0], reverse=True)
    # print timediff1, timediff2, heap
    if timediff1[0][0] > timediff2[0][0]:
        heappop(heap[timediff1[0][1]])
    else:
        heap[timediff2[0][1]].pop()
    # print heap

ans = 0
for i in heap.keys():
    if len(heap[i]) > 0:
        if len(heap[i]) == 1:
            ans += 1
        else:
            ans += (heap[i][-1] - heap[i][0] + 1)

print ans
