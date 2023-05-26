# 모험가 길드 
# 길드는 n명으로 이루어져 있고, 모두 공포도 x를 가진다. 
# 공포도가 x인 모험가는 x명의 파티월을 이루어 여행을 떠나야한다. 
# 여행을 떠날 수 있는 최대 파티의 개수를 구하라. 
# 단, 모든 모험가가 여행을 떠나야만 하는 것은 아니다. 

# 가장 작은 숫자부터 그룹을 만든다. 
# 1. 정렬을 한다. 
# 2. list의 0번 인덱스 값만큼 슬라이싱을 list 길이보다 0번 인덱스의 값보다 작을때까지 반복한다. 

n = int(input())
player = list(map(int, input().split()))
player.sort(reverse=True)

party = 0
while(len(player) > 0):
    # 종료
    if len(player) < player[0]:
        break

    # 슬라이싱
    player = player[player[0]:]

    # 파티원 수 증가
    party += 1

print(party)