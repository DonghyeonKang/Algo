import sys 
from collections import deque

n, m = map(int, sys.stdin.readline().split())
t = sys.stdin.readline().split()

p = []
for i in range(m):
    arr = sys.stdin.readline().split()
    p.append(arr[1:])
check = [0 for _ in range(n)]
visited = [1 for _ in range(m)]

queue = deque()
for i in t[1:]:
    queue.append(i)

while(queue):
    person = queue.popleft()
    check[int(person) - 1] = 1

    # person 이 있는 파티 방문, 모든 사람 큐에 저장
    for i in range(len(p)):
        if person in p[i]:
            visited[i] = 0
            for j in p[i]:
                if check[int(j) - 1] == 0:

                    check[int(j) - 1] = 1
                    queue.append(j)
print(sum(visited))