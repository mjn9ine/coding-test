def Count(len):
    cnt = 1
    ep = stall[0]
    for i in range(1, n):
        if stall[i] - ep >= len:
            cnt += 1
            ep = stall[i]

    return cnt

n, c = map(int, input().split())

stall = []

for _ in range(n):
    tmp = int(input())
    stall.append(tmp)

stall.sort()
lt = 1
rt = stall[n - 1]

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)