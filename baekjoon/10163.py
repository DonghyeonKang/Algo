# 색종이
# 입력
size = int(input())
papers = []
width = [0]
for i in range(size):
  papers.append(list(map(int, input().split(" "))))
  width.append(0)

# 배열 구성
paperArray = [[0 for col in range(1001)] for row in range(1001)]
count = 1
xtmp = 0
ytmp = 0
for i in papers:
  x = i[0]
  y = i[1]
  for j in range(i[3]):
    for k in range(i[2]):
      paperArray[x + xtmp][y + ytmp] = count
      xtmp += 1
    xtmp = 0
    ytmp += 1
  ytmp = 0
  count += 1

# 출력
for i in range(1001):
    for j in range(1001):
        if paperArray[i][j] != 0:
            width[paperArray[i][j]] += 1

for i in range(1, len(width)):
  print(width[i])
