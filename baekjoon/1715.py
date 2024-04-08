import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

result = 0
if n == 1:
    result = 0
elif n == 2:
    result = heap[0] + heap[1]
elif n > 2:
    while(len(heap) > 1):
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        tmp = n1 + n2
        result += tmp
        heapq.heappush(heap, tmp)

print(result)

