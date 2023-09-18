# 평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.
# 이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
import sys

n = int(sys.stdin.readline())    # input test case
t = [] 
for i in range(n):  # input int num k, n
    tmp = []
    for j in range(2):
        tmp.append(int(sys.stdin.readline()))
    t.append(tmp)

a = [[0 for _ in range(14)] for _ in range(15)]

# 0호 라인
for i in range(15):
    a[i][0] = 1

# 1층 라인
for i in range(14):
    a[0][i] = i + 1

# 나머지 채우기
for i in range(1, 14):
    for j in range(1, 15):
        a[j][i] = sum(a[j - 1][:i + 1])

for i in t:
    print(a[i[0]][i[1] - 1])