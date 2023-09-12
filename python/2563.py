board = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
paper = []
for i in range(n):
    paper.append(input().split())

for i in range(n):
    for j in range(100):
        for k in range(100):
            if j >= int(paper[i][0]) and j < int(paper[i][0]) + 10 and k >= int(paper[i][1]) and k < int(paper[i][1]) + 10:
                board[j][k] = 1

sum = 0
for i in range(100):
    for j in range(100):
        sum += board[i][j]

print(sum)
