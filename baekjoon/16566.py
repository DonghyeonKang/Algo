import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
c = sys.stdin.readline().rstrip().split()
c.sort()
ks = sys.stdin.readline().rstrip().split()
nodes = []

def bs(num):
    global nodes
    start = 0
    end = len(nodes)

    while(start > end):
        mid = (start + end) // 2
        if nodes[mid] == num:
            break
        elif nodes[mid] < num:
            start = mid + 1 
        elif nodes[mid] > num:
            end = mid - 1

    return nodes.pop(mid)

for i in range(len(ks)):
    print(bs(ks[i]))
    