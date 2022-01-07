# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
n1 = int(input())
array = []
result = []

for i in range(n1):
    array.append(input().split())
    n2 = int(array[i].pop(0))
    array[i].sort()
    sum = 0
    average = 0
    count = 0
    for j in array[i]:
        sum += int(j)
    average = sum / n2
    for k in array[i]:
        if int(k) > average:
            count += 1
    result.append(100 * float(count / n2))

for i in result:
    print('%.3f' % i, '%', sep = '')

# 1. 너무 직관적임. 효율성이 떨어진다. 리팩트 필요