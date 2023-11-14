# 입력 값을 입력받는다. 
# 회의 시간 리스트를 끝나는 시간 순으로 정렬한다. 
# 리스트의 0번째 인덱스 값은 result list 에 넣는다. 
# loop 를 졸며 아래를 반복한다. 
#   i 번째 회의 시간의 끝나는 시간이 result 의 마지막 회의 시간의 끝나는 시간보다 크면 
#       result 리스트에 append 한다. 
# result 리스트의 결과를 출력한다. 

n = int(input())
timetable = []

for i in range(n):
    timetable.append([int(x) for x in input().split()])

timetable.sort(key=lambda x:(x[1], x[0]))

result = []
result.append(timetable[0])

for i in timetable[1:]:
    if result[len(result) - 1][1] <= i[0]:
        result.append(i)

print(len(result))