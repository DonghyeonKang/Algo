n = int(input())
nlist = [i for i in range(1, n + 1)]

def recursive(idx, soon, visited):
    if visited[idx] == 1:
        return
    else:
        visited[idx] = 1
        soon.append(idx)
        if len(soon) == n:
            print(*soon)
            return
    for i in nlist:
        recursive(i, soon.copy(), visited.copy())
    return

for i in range(1, n + 1):
    soon = []
    v = [0 for _ in range(n + 1)]
    recursive(i, soon.copy(), v.copy())
