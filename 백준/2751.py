# import sys
# sys.setrecursionlimit(3000)

# def quick_sort(data):
#     if len(data) <= 1:      
#         return data
    
#     pivot = data[len(data) // 2]
#     less, equal, more = [], [], []
#     for num in data:
#         if num < pivot:
#             less.append(num)
#         elif num > pivot:
#             more.append(num)
#         else:
#             equal.append(num)
#     return quick_sort(less) + equal + quick_sort(more)

# if __name__ == "__main__":
#     cnt = int(sys.stdin.readline())
#     data = []
#     for i in range(cnt):
#         data.append(int(sys.stdin.readline()))
#     result = quick_sort(data)
#     for i in result:
#         print(i)

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

sorted_data = sorted(data)
for i in range(n):
    print(sorted_data[i])