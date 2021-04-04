def isPalindrome(x):
    if x == x[::-1]:
        return True
    else:
        return False

grid = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    # i가 0, 1, 2까지만 도는 이유는 인덱스가 3일 경우는 행으로 5개 연속으로 불가하기 때문이다.
    for j in range(7):
        temp_list = grid[j][i:i + 5]
        if isPalindrome(temp_list):
            cnt += 1

        for k in range(2):
            if grid[i + k][j] != grid[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)