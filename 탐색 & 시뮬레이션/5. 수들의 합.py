n, m = map(int, input().split())

num_list = list(map(int, input().split()))
lt, rt = 0, 1
tot = num_list[0]
cnt = 0
# 아래의 방법은 시간초과되었다.
# for i in range(n):
#     tmp = num_list[i]
#     if tmp == m:
#         cnt += 1
#         continue
#     for j in range(i + 1, n):
#         tmp += num_list[j]
#         if tmp < m:
#             continue
#         elif tmp > m:
#             break
#         else:
#             cnt += 1
#             break

while True:
    if tot < m:
        if rt < n:
            tot += num_list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= num_list[lt]
        lt += 1
    else:
        tot -= num_list[lt]
        lt += 1
print(cnt)