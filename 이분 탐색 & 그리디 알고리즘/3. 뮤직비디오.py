def Count(capacity):
    cnt = 1
    sum = 0
    for x in run_time:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x

    return cnt

n, m = map(int, input().split())

run_time = list(map(int, input().split()))

lt = 1
rt = sum(run_time)
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ans)