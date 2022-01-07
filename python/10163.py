# 입력
size = int(input())
papers = []
width = [0]
for i in range(size):
  tmp = list(map(int, input().split(" ")))
  for j in range(len(tmp)):
    if tmp[0] > tmp[2]:
      tmpnum = tmp[0]
      tmp[0] = tmp[2]
      tmp[2] = tmpnum
    if tmp[1] > tmp[3]:
      tmpnum = tmp[1]
      tmp[1] = tmp[3]
      tmp[3] = tmpnum
  papers.append(tmp)
  width.append(0)

# 배열 구성
paperlist = [[0 for col in range(1001)] for row in range(1001)]
count = 1
for i in papers:
    for j in range(i[3]):
        for k in range(i[2]):
            paperlist[j][k] = count
    count += 1

# 출력
for i in range(1001):
    for j in range(1001):
        if paperlist[i][j] != 0:
            width[paperlist[i][j]] += 1

for i in range(1, len(width)):
  print(width[i])
print(count)