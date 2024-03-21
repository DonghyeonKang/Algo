# 잃어버린 괄호

expression = input()

minus = expression.split("-")
if minus[0] == '':
    minus[1] = '-' + minus[1]
    del minus[0]

nums = []
for i in minus:
    plus = i.split("+")
    if plus[0] == '':
        del plus[0]
    tmp = 0
    for j in plus:
        tmp += int(j)
    nums.append(tmp)

sum = nums[0]
for i in nums[1:]:
    sum -= int(i)
print(sum)