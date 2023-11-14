
# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없다. 
# 단, 인덱스가 다르면 값이 달라도 다른 값으로 취급한다. 
# 예) 2,4,5,4,6 배열에 m이 8이고 k가 3이면 6,6,6,5,6,6,6,5의 합인 46이 큰수의 법칙에 따른 값이다. 

# N M K 입력 받음.
# 배열 입력 받음.
# 가장 큰 2개의 수를 찾아 저장한다
# 2중 for 문으로 k 만큼 반복해서 가장 큰 수를 더한다. 
# 그리고 두 번째로 큰 수를 더한다. 
# 이를 M번 만큼 반복한다. 

# n, m, k = map(int, input().split(" "))
# arr = list(map(int, input().split(" ")))

# idx = 0
# tmp = 0
# bignum = []

# for i, number in enumerate(arr):
#     if tmp < number:
#         tmp = number
#         idx = i
# del arr[idx]
# bignum.append(tmp)

# tmp = 0
# for i, number in enumerate(arr):
#     if tmp < number:
#         tmp = number
#         idx = i
# bignum.append(tmp)

# result = 0
# cnt = 0
# for i in range(m // (k+1) + 1):
#     for j in range(k):
#         result += bignum[0]
#         cnt += 1
#         if cnt > k:
#             break
#     result += bignum[1]
#     cnt += 1
#     if cnt > k:
#         break

# 1. 값과 배열을 입력받는다. 
# 2. 정렬을 한 뒤 가장 큰 값, 2번째로 큰 값을 구한다. 
# 3. 가장 큰 값과 더해질 값을 수식으로 정의하여 결과값을 구한다. 

n, m, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

arr.sort()
big = arr[n - 1]
low = arr[n - 2]

result = big * m // (k + 1) * k + low * m // (k + 1)
print(result)