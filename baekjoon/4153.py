# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

alist = []
while(1):
    tmplist = list(map(int, input().split()))
    if(tmplist[0] + tmplist[1] + tmplist[2] == 0):
        break
    tmplist.sort()
    alist.append(tmplist)

for i in range(len(alist)):
    if((alist[i][0]**2 + alist[i][1]**2) == alist[i][2]**2): print('right')
    else: print('wrong')

