import heapq
import sys

n = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
classes.sort()

heap = [classes[0][1]]
for i in range(1, n):
    if classes[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1])

print(len(heap))