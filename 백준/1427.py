# 소트 인사이드

n = list(map(int, list(input())))
n.sort(reverse=True)
n = list(map(str, n))
print("".join(n))