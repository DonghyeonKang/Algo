import sys
sys.setrecursionlimit(10 ** 4)

n = int(sys.stdin.readline())

def backtracking(row, ups, downs, cols):
    if row == n:
        return 1
    result = 0
    
    for col in range(n):
        curr_up = row + col
        curr_down = row - col
        if curr_down not in downs and curr_up not in ups and col not in cols:
            ups.append(curr_up)
            downs.append(curr_down)
            cols.append(col)
            result += backtracking(row + 1, ups, downs, cols)
            ups.remove(curr_up)
            downs.remove(curr_down)
            cols.remove(col)
    return result

print(backtracking(0, [], [], []))