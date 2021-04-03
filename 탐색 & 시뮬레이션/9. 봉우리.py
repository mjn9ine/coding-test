n = int(input())

grid_map = [list(map(int, input().split())) for _ in range(n)]

# all 이용하기 위한 리스트 변형
# grid_map.insert(0, [0] * n)
# grid_map.append([0] * n)
#
# for x in grid_map:
#     x.insert(0, 0)
#     x.append(0)

cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        # all 이용해서 좀 더 간단하게 구현 가능.
        # 대신 리스트를 주어진 대로 변형해줘야함.
        # if all(grid_map[i][j] > grid_map[i + dx[k]][j + dy[k]] for k in range(4)):
        #     cnt += 1
        # 내 풀이
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                if grid_map[i][j] <= grid_map[ni][nj]:
                    break
        else:
            cnt += 1

print(cnt)
