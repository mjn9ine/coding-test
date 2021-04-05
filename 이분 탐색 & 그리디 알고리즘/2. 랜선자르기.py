def Count(len):
    cnt = 0
    for x in lopes:
        cnt += (x // len)

    return cnt
k, n = map(int, input().split())

lopes = []
res = 0
largest = 0
for _ in range(k):
    tmp = int(input())
    lopes.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
