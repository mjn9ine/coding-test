n, m = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

lt, rt = 0, n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if num_list[mid] == m:
        print(mid + 1)
        break
    elif num_list[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1