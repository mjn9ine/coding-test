n = int(input())

board = []
row_sum = 0
# 각 행의 합은 input받는 과정에서 미리 처리하고 가장 큰 값을 row_sum에 저장해준다.
for _ in range(n):
    data = list(map(int, input().split()))
    row_sum = sum(data) if row_sum < sum(data) else row_sum
    board.append(data)
# 각 열의 합 구해주고 그 중 가장 큰 값을 구해준다.
column_sum = 0
for i in range(n):
    temp_sum = 0
    for j in range(n):
        temp_sum += board[j][i]
    column_sum = column_sum if column_sum > temp_sum else temp_sum
# 두 대각선의 합 구하기.
# \모양 대각선
cross_sum_1 = 0
# /모양 대각선
cross_sum_2 = 0
for i in range(n):
    cross_sum_1 += board[i][i]
    cross_sum_2 += board[i][n - 1 - i]

print(max(row_sum, column_sum, cross_sum_1, cross_sum_2))

