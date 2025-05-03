# 최소힙
import sys
import heapq

n = int(sys.stdin.readline())
minHeap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    # 0 이면 출력
    if(x == 0):
        if len(minHeap) == 0:
            print(0)
        else:
            print(heapq.heappop(minHeap)) # 왼쪽에서 pop
    else: # 0 아니면 insert
        heapq.heappush(minHeap, x)