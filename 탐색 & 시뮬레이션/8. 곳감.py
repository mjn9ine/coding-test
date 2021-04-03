n = int(input())

garden = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for _ in range(m):
    r, d, x = map(int, input().split())
    for _ in range(x):
        if d == 0:
            garden[r - 1].append(garden[r - 1].pop(0))
        elif d == 1:
            garden[r - 1].insert(0, garden[r - 1].pop())

s, e = 0, n - 1
ans = 0

for i in range(n):
    for j in range(s, e + 1):
        ans += garden[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(ans)
