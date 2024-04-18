import sys
n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]

def isPalindrome(depth, l):
    if depth > 1:
        return False

    start = 0
    depth += 1
    end = len(l) - 1
    while(start < end):
        if l[start] == l[end]:
            start += 1
            end -= 1
        elif l[start] != l[end]:
            f1 = isPalindrome(depth, l[start + 1:end + 1])                
            f2 = isPalindrome(depth, l[start:end])
            if f1 == 0 or f2 == 0:
                return 1 # 유사 회문
            else:
                return 2 # 회문이 아님
    return 0 # 회문

for i in l:
    print(isPalindrome(0, i))