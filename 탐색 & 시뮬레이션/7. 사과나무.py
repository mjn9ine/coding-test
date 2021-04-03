n = int(input())

farm = [list(map(int, input().split())) for _ in range(n)]

s = e = n // 2
ans = 0

for i in range(n):
    for j in range(s, e + 1):
        ans += farm[i][j]

    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(ans)
