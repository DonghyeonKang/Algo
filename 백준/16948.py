from collections import deque

n = int(input())
lo = list(map(int, input().split()))
frl = [lo[0],lo[1]]
tol = [lo[2],lo[3]]

board = [[-1 for _ in range(n)] for _ in range(n)]
board[frl[1]][frl[0]] = 0
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(x, y, board):
    q = deque()
    q.append((x, y))

    while(q):
        x, y = q.popleft()
        for dx, dy in d:
            if x + dx >= 0 and x + dx < n and y + dy >= 0 and y + dy < n and board[y + dy][x + dx] == -1:
                q.append((x + dx, y + dy))
                board[y + dy][x + dx] = board[y][x] + 1

bfs(frl[0], frl[1], board)
print(board[tol[1]][tol[0]])
