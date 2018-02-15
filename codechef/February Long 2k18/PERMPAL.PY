from collections import Counter, defaultdict

t = int(raw_input())

for _ in xrange(t):
    s = raw_input()
    pos = defaultdict(list)
    ans = {}
    for i in xrange(len(s)):
        pos[s[i]].append(i+1)
    count = Counter(s)
    # print pos
    odd = 0
    ans = {}
    for i in count.values():
        if i % 2:
            odd += 1
    if odd > 1:
        print -1
    else:
        start = 0
        end = len(s)-1
        index = -1
        for i in count.keys():
            if not count[i] % 2:
                for j in xrange(count[i]/2):
                    ans[start] = pos[i].pop()
                    ans[end] = pos[i].pop()
                    start += 1
                    end -= 1
            else:
                index = i
        if index != -1:
            for i in xrange((count[index]-1)/2):
                ans[start] = pos[index].pop()
                start += 1
                ans[end] = pos[index].pop()
                end -= 1
            ans[start] = pos[index].pop()
        for i in ans.values():
            print i,
        print
