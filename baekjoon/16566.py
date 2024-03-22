import sys

n, m, k = map(int, sys.stdin.readline().split())
parent = [i for i in range(n)]

cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
chulsoo = list(map(int, sys.stdin.readline().split()))

def bs(num):
    start = 0
    end = len(cards)

    while(start <= end):
        mid = (start + end) // 2
        if cards[mid] <= num:
            start = mid + 1 
        else:
            end = mid - 1
    return start

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(a, b):
    x, y = find(a), find(b)
    if x<y: parent[x] = y
    else: parent[y] = x

for i in chulsoo:
    idx = bs(i)
    idx = find(idx)
    print(cards[idx])
    union(idx, idx + 1)
    