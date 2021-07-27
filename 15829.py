# 1. 50점
# l = int(input())
# data = list(input())
# sum = 0
# for i in range(l):
#     sum = sum + (ord(data[i]) % 96)*(31**i) % 1234567891
# print(sum)

# 2. 블로그 참고해서 but 다른 언어
# l = int(input())
# data = list(input())
# sum = 0
# for i in range(l):
#     tmp = ((ord(data[i]) % 96)% 1234567891) * ((31**i) % 1234567891)
#     if tmp > 1234567891:
#         tmp = tmp % 1234567891
#     sum = sum + tmp   # 이게 문제
# print(sum)

# 3. 정답 ?? 왜 되는거지? -> 값 확인 
# l = int(input())
# data = list(input())
# sum = 0
# for i in range(l):
#     sum = (sum + (ord(data[i]) % 96)*(31**i)) % 1234567891
# print(sum)

# 4. 정답
l = int(input())
data = list(input())
sum = 0
for i in range(l):
    sum = sum + (ord(data[i]) % 96)*(31**i) % 1234567891    # 이게 문제
    if sum > 1234567891:
        sum = sum % 1234567891
print(sum)
